from argparse import ArgumentParser
from argparse import Namespace
from enum import Enum
from os import environ
from pathlib import Path
from subprocess import run
from sys import stdin
from tempfile import NamedTemporaryFile
from textwrap import indent
from typing import Optional
from typing import Union

from .ezchlog import EzChLog


class Parser:
    def __init__(self, ezchlog: EzChLog) -> None:
        self.log = ezchlog
        self.parser = ArgumentParser()
        self.parser.add_argument(
            '-n',
            '--dry-run',
            action='store_true',
            help="Dry-run the action",
        )
        subparsers = self.parser.add_subparsers(
            required=True,
            dest='action',
            help="Choose an action, you can also have more help using ACTION --help",
        )
        parser_show_config = subparsers.add_parser('showconfig')
        parser_show_config.set_defaults(func=self.show_config_action)
        parser_show_config.add_argument(
            dest='config_key',
            nargs='?',
            metavar='key',
            default='',
            help="Only show this config key value.",
        )
        parser_add = subparsers.add_parser('add')
        parser_add.set_defaults(func=self.add_action)
        parser_add.add_argument(
            'message',
            help="Your message. Use '-' to open an editor instead.",
        )
        Category = self.log.cfg.category_class
        CategoryDef = getattr(Category, self.log.cfg.category_default)
        category_names = [cat.name for cat in list[Enum](Category)]
        parser_add.add_argument(
            'cat',
            nargs='?',
            metavar='type',
            default=CategoryDef,
            type=lambda s: getattr(Category, s) if s else CategoryDef,
            choices=list(Category),
            help=f"Choose one of {', '.join(category_names)}. Defaut to {CategoryDef.name}.",
        )
        parser_add.add_argument(
            'ref',
            nargs='?',
            default='',
            help="Reference for the log. Default is empty.",
        )
        parser_list = subparsers.add_parser('list')
        parser_list.set_defaults(func=self.list_action)
        parser_merge = subparsers.add_parser('merge')
        parser_merge.add_argument(
            'version',
            help="The next version",
        )
        parser_merge.set_defaults(func=self.merge_action)

    def show_config_action(self, opts: Namespace) -> None:
        def format_value(value: Union[str, bool, int, None], *, with_indent: bool = True) -> str:  # noqa: FBT001
            if with_indent and isinstance(value, str) and '\n' in value:
                return '\n' + indent(value, '  ')
            else:
                return f'{value}'

        if opts.config_key:
            value = dict(self.log.cfg).get(opts.config_key)
            print(format_value(value, with_indent=False))  # noqa: T201
        else:
            for key, value in self.log.cfg:
                print(f'{key} = {format_value(value)}')  # noqa: T201

    def open_editor(self, file_ext: str, default_message: str) -> str:
        editor = environ.get('EZCHLOG_EDITOR', environ.get('EDITOR', environ.get('VISUAL', 'vim')))
        if not editor or not stdin.isatty():
            raise Exception(f"Cannot run editor '{editor}'")
        with NamedTemporaryFile(mode='w+', encoding='utf-8', suffix=f'.{file_ext}', delete=False) as f:
            f.write(default_message)
            f.flush()
            try:
                run([editor, f.name])
                f.seek(0)
                return '\n'.join(line for line in f.read().split('\n') if not line.startswith('#'))
            finally:
                Path(f.name).unlink()

    def add_action(self, opts: Namespace) -> None:
        if opts.message == '-':
            opts.message = self.open_editor('md', """
# This a markdown log file.
# Any comment will be removed.
# An empty file will abort.
""")
        message = opts.message.strip()
        if not message:
            raise Exception("Aborted")
        file_path, md_message = self.log.add(dry_run=opts.dry_run, message=message, cat=opts.cat, ref=opts.ref)
        print(file_path)  # noqa: T201
        if opts.dry_run:
            print(md_message)  # noqa: T201

    def list_action(self, opts: Namespace) -> None:
        for p in self.log.list():
            print(p)  # noqa: T201

    def merge_action(self, opts: Namespace) -> None:
        changelog = self.log.merge(dry_run=opts.dry_run, next_version=opts.version)
        if opts.dry_run:
            print(changelog)  # noqa: T201

    def parse(self, args: Optional[list[str]] = None) -> None:
        opts = self.parser.parse_args(args=args)
        opts.func(opts)


def run_cli() -> None:
    Parser(EzChLog()).parse()
