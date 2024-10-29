from enum import Enum
from enum import EnumMeta
from pathlib import Path
from unittest.mock import MagicMock
from unittest.mock import patch

from pytest import fixture

from ezchlog.ezchlog import EzChLog


@patch('ezchlog.ezchlog.Config')
def test_ezchlog_init(config_class) -> None:
    cfg = config_class()
    ezchlog = EzChLog()
    assert ezchlog.cfg == cfg


def test_ezchlog_get_slug() -> None:
    assert EzChLog.get_slug('test') == 'test'
    assert EzChLog.get_slug(
        '(a simple)  message w!th accented letter$: « Café », symbols and too long',
    ) == 'a_simple_message_wth_accented_letter_café_symbols'


@patch('ezchlog.ezchlog.Config')
def test_ezchlog_add_simple(config_class, tmp_path) -> None:
    config_class.return_value = MagicMock(
        log_dir=tmp_path / 'logs',
        root_dir=tmp_path,
    )
    ezchlog = EzChLog()
    cat = MagicMock()
    cat.name = 'changed'
    log_file, msg = ezchlog.add(dry_run=False, message="- simple message", cat=cat, ref="")
    assert log_file == Path('logs') / 'changed' / 'simple_message.md'
    assert msg == "- simple message"
    content = (tmp_path / log_file).read_text(encoding='utf-8')
    assert content == "- simple message\n"


@patch('ezchlog.ezchlog.Config')
def test_ezchlog_add_complex(config_class, tmp_path) -> None:
    config_class.return_value = MagicMock(
        log_dir=tmp_path / 'logs',
        root_dir=tmp_path,
    )
    ezchlog = EzChLog()
    cat = MagicMock()
    cat.name = 'changed'
    log_file, msg = ezchlog.add(dry_run=False, message="complex message\nwith\nother\nlines", cat=cat, ref="42")
    assert log_file == Path('logs') / 'changed' / '42_complex_message.md'
    assert msg == "- complex message (42)  \nwith  \nother  \nlines"
    content = (tmp_path / log_file).read_text(encoding='utf-8')
    assert content == "- complex message (42)  \nwith  \nother  \nlines\n"


@fixture
def category_class() -> EnumMeta:
    category_class = Enum('Category', names=['fix', 'add'])  # type: ignore
    return category_class


@patch('ezchlog.ezchlog.Config')
def test_ezchlog_list(config_class, tmp_path, category_class) -> None:
    config_class.return_value = MagicMock(
        log_dir=tmp_path / 'logs',
        category_class=category_class,
    )
    (tmp_path / 'logs' / 'add').mkdir(parents=True)
    (tmp_path / 'logs' / 'add' / 'toto.md').touch()
    (tmp_path / 'logs' / 'add' / 'a_test.md').touch()
    (tmp_path / 'logs' / 'fix').mkdir(parents=True)
    (tmp_path / 'logs' / 'fix' / 'some_fix.md').touch()
    ezchlog = EzChLog()
    assert ezchlog.list() == [
        Path('fix') / 'some_fix.md',
        Path('add') / 'a_test.md',
        Path('add') / 'toto.md',
    ]


@patch('ezchlog.ezchlog.Config')
def test_ezchlog_merge_empty_version(config_class, tmp_path, category_class) -> None:
    log_dir = tmp_path / 'logs'
    log_file = tmp_path / 'chglogs.md'
    default_changelog = '# Changelogs'
    config_class.return_value = MagicMock(
        log_dir=log_dir,
        log_file=log_file,
        category_class=category_class,
        default_changelog=default_changelog,
    )
    ezchlog = EzChLog()
    expected_content = "# Changelogs\n"
    assert ezchlog.merge(dry_run=False, next_version="1.0.0") == expected_content
    assert log_file.read_text(encoding='utf-8') == expected_content


@patch('ezchlog.ezchlog.Config')
def test_ezchlog_merge_not_existing(config_class, tmp_path, category_class) -> None:
    log_dir = tmp_path / 'logs'
    log_file = tmp_path / 'chglogs.md'
    default_changelog = '# Changelogs'
    config_class.return_value = MagicMock(
        log_dir=log_dir,
        log_file=log_file,
        category_class=category_class,
        default_changelog=default_changelog,
    )
    (log_dir / 'add').mkdir(parents=True)
    (log_dir / 'add' / 'toto.md').write_text("- toto content", encoding='utf-8')
    (log_dir / 'add' / 'a_test.md').write_text("- test content", encoding='utf-8')
    (log_dir / 'fix').mkdir(parents=True)
    (log_dir / 'fix' / 'some_fix.md').write_text("- fix content", encoding='utf-8')
    ezchlog = EzChLog()
    expected_content = """\
# Changelogs

## 1.0.0
### fix
- fix content
### add
- test content
- toto content
"""
    assert ezchlog.merge(dry_run=False, next_version="1.0.0") == expected_content
    assert log_file.read_text(encoding='utf-8') == expected_content
    assert not (log_dir / 'add' / 'toto.md').exists()
    assert not (log_dir / 'add' / 'a_test.md').exists()
    assert not (log_dir / 'fix' / 'some_fix.md').exists()


@patch('ezchlog.ezchlog.Config')
def test_ezchlog_merge_existing(config_class, tmp_path, category_class) -> None:
    log_dir = tmp_path / 'logs'
    log_file = tmp_path / 'chglogs.md'
    default_changelog = '# Changelogs'
    config_class.return_value = MagicMock(
        log_dir=log_dir,
        log_file=log_file,
        category_class=category_class,
        default_changelog=default_changelog,
    )
    log_file.write_text("""\
# Changelogs

## 1.0.0
### fix
- fix content
### add
- test content
- toto content
""", encoding='utf-8')
    (log_dir / 'fix').mkdir(parents=True)
    (log_dir / 'fix' / 'minor_modif.md').write_text("- a minor modif", encoding='utf-8')
    ezchlog = EzChLog()
    expected_content = """\
# Changelogs

## 1.1.0
### fix
- a minor modif

## 1.0.0
### fix
- fix content
### add
- test content
- toto content
"""
    assert ezchlog.merge(dry_run=False, next_version="1.1.0") == expected_content
    assert log_file.read_text(encoding='utf-8') == expected_content
    assert not (log_dir / 'fix' / 'minor_modif.md').exists()
