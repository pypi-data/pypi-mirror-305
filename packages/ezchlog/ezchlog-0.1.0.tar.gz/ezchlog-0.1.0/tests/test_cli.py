from argparse import ArgumentParser
from argparse import Namespace
from enum import Enum
from enum import EnumMeta
from pathlib import Path
from unittest.mock import MagicMock
from unittest.mock import patch

from pytest import fixture
from pytest import raises

from ezchlog.cli import Parser
from ezchlog.cli import run_cli


@patch('ezchlog.cli.EzChLog')
@patch('ezchlog.cli.Parser')
def test_run_cli(parser_cls, ezchlog_cls) -> None:
    ezchlog_instance = MagicMock()
    ezchlog_cls.return_value = ezchlog_instance
    parser_instance = MagicMock()
    parser_cls.return_value = parser_instance
    run_cli()
    ezchlog_cls.assert_called_once_with()
    parser_cls.assert_called_once_with(ezchlog_instance)
    parser_instance.parse.assert_called_once_with()


@fixture
def category_class() -> EnumMeta:
    category_class = Enum('Category', names=['toto', 'titi'])  # type: ignore
    return category_class


@fixture
def ezchlog(category_class) -> MagicMock:
    cfg = MagicMock(category_class=category_class, category_default=next(iter(category_class)).name)
    ezchlog = MagicMock(cfg=cfg)
    return ezchlog


def test_parser_init(ezchlog) -> None:
    parser = Parser(ezchlog)
    assert parser
    assert parser.log is ezchlog
    assert isinstance(parser.parser, ArgumentParser)


@patch('ezchlog.cli.Parser.merge_action')
@patch('ezchlog.cli.Parser.list_action')
@patch('ezchlog.cli.Parser.add_action')
@patch('ezchlog.cli.Parser.show_config_action')
def test_parser_parse(show_config_action, add_action, list_action, merge_action, ezchlog, category_class) -> None:
    parser = Parser(ezchlog)
    # showconfig
    parser.parse(args=['-n', 'showconfig'])
    showconfig_ns = Namespace(dry_run=True, action='showconfig', config_key='', func=show_config_action)
    show_config_action.assert_called_once_with(showconfig_ns)
    show_config_action.reset_mock()
    add_action.assert_not_called()
    list_action.assert_not_called()
    merge_action.assert_not_called()
    # add, first case
    parser.parse(args=['add', 'a message', 'titi', '42'])
    add_ns = Namespace(dry_run=False, action='add', message='a message', cat=category_class.titi, ref='42', func=add_action)
    show_config_action.assert_not_called()
    add_action.assert_called_once_with(add_ns)
    add_action.reset_mock()
    list_action.assert_not_called()
    merge_action.assert_not_called()
    # add, second case
    parser.parse(args=['add', '-'])
    add_ns = Namespace(dry_run=False, action='add', message='-', cat=category_class.toto, ref='', func=add_action)
    show_config_action.assert_not_called()
    add_action.assert_called_once_with(add_ns)
    add_action.reset_mock()
    list_action.assert_not_called()
    merge_action.assert_not_called()
    # list
    parser.parse(args=['list'])
    list_ns = Namespace(dry_run=False, action='list', func=list_action)
    show_config_action.assert_not_called()
    add_action.assert_not_called()
    list_action.assert_called_once_with(list_ns)
    list_action.reset_mock()
    merge_action.assert_not_called()
    # merge
    parser.parse(args=['merge', '1.2.3'])
    merge_ns = Namespace(dry_run=False, action='merge', version='1.2.3', func=merge_action)
    show_config_action.assert_not_called()
    add_action.assert_not_called()
    list_action.assert_not_called()
    merge_action.assert_called_once_with(merge_ns)
    merge_action.reset_mock()


def test_parser_showconfig(capsys) -> None:
    parser = MagicMock()
    parser.log.cfg = [
        ('some_key', 'some_value'),
        ('other_key', 42),
    ]
    Parser.show_config_action(self=parser, opts=MagicMock(config_key=''))
    captured = capsys.readouterr()
    assert captured.out == "some_key = some_value\nother_key = 42\n"
    Parser.show_config_action(self=parser, opts=MagicMock(config_key='other_key'))
    captured = capsys.readouterr()
    assert captured.out == "42\n"


def test_parser_add_full(capsys, category_class) -> None:
    parser = MagicMock()
    parser.log.add.return_value = (Path("_CHANGELOGS/titi/a_test_message.md"), "- a test message")
    Parser.add_action(self=parser, opts=MagicMock(dry_run=True, message="a test message", cat=category_class.titi, ref="324"))
    captured = capsys.readouterr()
    assert captured.out == "_CHANGELOGS/titi/a_test_message.md\n- a test message\n"
    parser.open_editor.assert_not_called()
    parser.log.add.assert_called_once_with(dry_run=True, message="a test message", cat=category_class.titi, ref="324")


def test_parser_add_editor(capsys, category_class) -> None:
    parser = MagicMock()
    parser.open_editor.return_value = "  another test message \n "
    parser.log.add.return_value = (Path("_CHANGELOGS/toto/another_test_message.md"), "- another test message")
    Parser.add_action(self=parser, opts=MagicMock(dry_run=False, message="-", cat=category_class.toto, ref=""))
    captured = capsys.readouterr()
    assert captured.out == "_CHANGELOGS/toto/another_test_message.md\n"
    parser.open_editor.assert_called_once_with('md', """
# This a markdown log file.
# Any comment will be removed.
# An empty file will abort.
""")
    parser.log.add.assert_called_once_with(dry_run=False, message="another test message", cat=category_class.toto, ref="")


def test_parser_add_error(capsys, category_class) -> None:
    parser = MagicMock()
    with raises(Exception) as ex:
        Parser.add_action(self=parser, opts=MagicMock(dry_run=False, message=" ", cat=category_class.toto, ref=""))
        assert ex.value == "Aborted"
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
    parser.open_editor.assert_not_called()
    parser.log.add.assert_not_called()


@patch('ezchlog.cli.run')
@patch('pathlib.Path.unlink')
@patch('ezchlog.cli.NamedTemporaryFile')
@patch('sys.stdin.isatty')
@patch('ezchlog.cli.environ', {})
def test_parser_open_editor_vim(isatty, named_temporary_file, unlink, run_process) -> None:
    isatty.return_value = True
    f = MagicMock(name="f")
    f.name = '/tmp/temp_file.md'
    f.read.return_value = "A message\n# some comment\nfrom editor\n# explanation\n"
    named_temporary_file.return_value.__enter__.return_value = f
    parser = MagicMock()
    msg = Parser.open_editor(self=parser, file_ext='md', default_message="# explanation\n")
    assert msg == "A message\nfrom editor\n"
    isatty.assert_called_once()
    named_temporary_file.assert_called_once()
    _, temp_kwargs = named_temporary_file.call_args_list[-1]
    assert temp_kwargs.get('encoding') == 'utf-8'
    assert temp_kwargs.get('suffix') == '.md'
    f.write.assert_called_once_with("# explanation\n")
    f.seek.assert_called_once_with(0)
    f.flush.assert_called_once()
    f.read.assert_called_once()
    run_process.assert_called_once_with(['vim', '/tmp/temp_file.md'])
    unlink.assert_called_once()


@patch('ezchlog.cli.run')
@patch('pathlib.Path.unlink')
@patch('ezchlog.cli.NamedTemporaryFile')
@patch('sys.stdin.isatty')
@patch('ezchlog.cli.environ', {'EDITOR': 'nano', 'VISUAL': 'geany'})
def test_parser_open_editor_editor(isatty, named_temporary_file, unlink, run_process) -> None:
    isatty.return_value = True
    f = MagicMock(name="f")
    f.name = '/tmp/some_file.md'
    f.read.return_value = "A message\n# some comment\nfrom nano\n# explanation\n"
    named_temporary_file.return_value.__enter__.return_value = f
    parser = MagicMock()
    msg = Parser.open_editor(self=parser, file_ext='md', default_message="# explanation\n")
    assert msg == "A message\nfrom nano\n"
    isatty.assert_called_once()
    named_temporary_file.assert_called_once()
    _, temp_kwargs = named_temporary_file.call_args_list[-1]
    assert temp_kwargs.get('encoding') == 'utf-8'
    assert temp_kwargs.get('suffix') == '.md'
    f.write.assert_called_once_with("# explanation\n")
    f.seek.assert_called_once_with(0)
    f.flush.assert_called_once()
    f.read.assert_called_once()
    run_process.assert_called_once_with(['nano', '/tmp/some_file.md'])
    unlink.assert_called_once()


@patch('ezchlog.cli.run')
@patch('pathlib.Path.unlink')
@patch('ezchlog.cli.NamedTemporaryFile')
@patch('sys.stdin.isatty')
@patch('ezchlog.cli.environ', {'EZCHLOG_EDITOR': 'emacs', 'EDITOR': 'nano', 'VISUAL': 'geany'})
def test_parser_open_editor_ezchlogeditor(isatty, named_temporary_file, unlink, run_process) -> None:
    isatty.return_value = True
    f = MagicMock(name="f")
    f.name = '/tmp/another_file.rst'
    f.read.return_value = "A message\n# some comment\nfrom emacs\n# will no be kept\n"
    named_temporary_file.return_value.__enter__.return_value = f
    parser = MagicMock()
    msg = Parser.open_editor(self=parser, file_ext='rst', default_message="# will no be kept\n")
    assert msg == "A message\nfrom emacs\n"
    isatty.assert_called_once()
    named_temporary_file.assert_called_once()
    _, temp_kwargs = named_temporary_file.call_args_list[-1]
    assert temp_kwargs.get('encoding') == 'utf-8'
    assert temp_kwargs.get('suffix') == '.rst'
    f.write.assert_called_once_with("# will no be kept\n")
    f.seek.assert_called_once_with(0)
    f.flush.assert_called_once()
    f.read.assert_called_once()
    run_process.assert_called_once_with(['emacs', '/tmp/another_file.rst'])
    unlink.assert_called_once()


@patch('ezchlog.cli.run')
@patch('pathlib.Path.unlink')
@patch('ezchlog.cli.NamedTemporaryFile')
@patch('sys.stdin.isatty')
@patch('ezchlog.cli.environ', {'VISUAL': ''})
def test_parser_open_editor_no_editor(isatty, named_temporary_file, unlink, run_process) -> None:
    isatty.return_value = True
    f = MagicMock(name="f")
    f.name = '/tmp/another_file.md'
    f.read.return_value = "A message\n# some comment\nfrom editor\n# will no be kept\n"
    named_temporary_file.return_value.__enter__.return_value = f
    parser = MagicMock()
    with raises(Exception) as ex:
        Parser.open_editor(self=parser, file_ext='md', default_message="# will no be kept\n")
        assert ex.value == "Cannot run editor ''"
    named_temporary_file.assert_not_called()
    f.write.assert_not_called()
    f.seek.assert_not_called()
    f.flush.assert_not_called()
    f.read.assert_not_called()
    run_process.assert_not_called()
    unlink.assert_not_called()


@patch('ezchlog.cli.run')
@patch('pathlib.Path.unlink')
@patch('ezchlog.cli.NamedTemporaryFile')
@patch('sys.stdin.isatty')
@patch('ezchlog.cli.environ', {})
def test_parser_open_editor_not_a_tty(isatty, named_temporary_file, unlink, run_process) -> None:
    isatty.return_value = False
    f = MagicMock(name="f")
    f.name = '/tmp/another_file.md'
    f.read.return_value = "A message\n# some comment\nfrom editor\n# will no be kept\n"
    named_temporary_file.return_value.__enter__.return_value = f
    parser = MagicMock()
    with raises(Exception) as ex:
        Parser.open_editor(self=parser, file_ext='md', default_message="# will no be kept\n")
        assert ex.value == "Cannot run editor 'vim'"
    named_temporary_file.assert_not_called()
    f.write.assert_not_called()
    f.seek.assert_not_called()
    f.flush.assert_not_called()
    f.read.assert_not_called()
    run_process.assert_not_called()
    unlink.assert_not_called()


def test_parser_list(capsys) -> None:
    parser = MagicMock()
    parser.log.list.return_value = [Path("_CHANGELOGS/titi/a_test_message.md"), Path("_CHANGELOGS/toto/another_test_message.md")]
    Parser.list_action(self=parser, opts=MagicMock(dry_run=False))
    captured = capsys.readouterr()
    assert captured.out == "_CHANGELOGS/titi/a_test_message.md\n_CHANGELOGS/toto/another_test_message.md\n"


def test_parser_merge(capsys) -> None:
    parser = MagicMock()
    parser.log.merge.return_value = "The full\nchangelog"
    Parser.merge_action(self=parser, opts=MagicMock(dry_run=True, version="4.2.3"))
    captured = capsys.readouterr()
    assert captured.out == "The full\nchangelog\n"
    parser.log.merge.assert_called_once_with(dry_run=True, next_version="4.2.3")
