from collections.abc import Iterator
from enum import Enum
from enum import EnumMeta
from functools import cached_property
from os import environ
from pathlib import Path
from typing import Any
from typing import Optional
from typing import Union

try:
    from tomllib import load  # type: ignore[import-not-found]
except ModuleNotFoundError:
    from tomli import load  # type: ignore

DEFAULT_MAIN_CHANGELOG = 'CHANGELOG.md'
DEFAULT_CHANGELOG_DIR = '_CHANGELOGS'
DEFAULT_CATEGORIES = [
    'Security',
    'Fixed',
    'Changed',
    'Added',
    'Remove',
    'Deprecated',
]
DEFAULT_DEFAULT_CATEGORY = 'Changed'
DEFAULT_CHANGELOG_TEXT = """\
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).
"""


class Config:
    curr_dir: Path
    log_file: Path
    log_dir: Path
    category_list: list[str]
    category_default: str
    default_changelog: str

    def __init__(self) -> None:
        self.curr_dir = Path.cwd().resolve()
        cfg: dict[str, Any] = {}
        if self.ezchlogconf:
            with self.ezchlogconf.open('rb') as f:
                cfg = load(f)
        elif self.pyproject:
            with self.pyproject.open('rb') as f:
                cfg = load(f).get('tool', {}).get('ezchlog', {})
        self.log_file = Path(environ.get('EZCHLOG_LOG_FILE', cfg.get('log_file', DEFAULT_MAIN_CHANGELOG)))
        if not self.log_file.is_absolute():
            self.log_file = self.root_dir / self.log_file
        self.log_dir = Path(environ.get('EZCHLOG_LOG_DIR', cfg.get('log_dir', DEFAULT_CHANGELOG_DIR)))
        if not self.log_dir.is_absolute():
            self.log_dir = self.root_dir / self.log_dir
        category_list: Union[str, list[str]] = environ.get('EZCHLOG_CATEGORY_LIST', cfg.get('category_list', DEFAULT_CATEGORIES))
        self.category_list = category_list.split(' ') if isinstance(category_list, str) else category_list
        self.category_default = environ.get('EZCHLOG_CATEGORY_DEFAULT', cfg.get('category_default', DEFAULT_DEFAULT_CATEGORY))
        self.default_changelog = environ.get('EZCHLOG_DEFAULT_CHANGELOG', cfg.get('default_changelog', DEFAULT_CHANGELOG_TEXT))

    @cached_property
    def ezchlogconf(self) -> Optional[Path]:
        p_root = self.curr_dir
        for p in [p_root] + list(p_root.parents):
            pf = p / '.ezchlog.toml'
            if pf.is_file():
                return pf
        else:
            return None

    @cached_property
    def pyproject(self) -> Optional[Path]:
        p_root = self.curr_dir
        for p in [p_root] + list(p_root.parents):
            pf = p / 'pyproject.toml'
            if pf.is_file():
                return pf
        else:
            return None

    @cached_property
    def git_dir(self) -> Optional[Path]:
        p_root = self.curr_dir
        for p in [p_root] + list(p_root.parents):
            pd = p / '.git'
            if pd.is_dir():
                return pd
        else:
            return None

    @cached_property
    def root_dir(self) -> Path:
        for attr in ('ezchlogconf', 'pyproject', 'git_dir'):
            if (path := getattr(self, attr)):
                return path.parent
        else:
            return self.curr_dir

    @cached_property
    def category_class(self) -> EnumMeta:
        category_class = Enum('Category', names=self.category_list)  # type: ignore
        return category_class

    def __iter__(self) -> Iterator[tuple[str, Union[str, bool, int]]]:
        Category = self.category_class
        category_names = [cat.name for cat in list[Enum](Category)]
        d: dict[str, Union[str, bool, int]] = dict(
            log_dir=str(self.log_dir),
            log_file=str(self.log_file),
            categories=', '.join(category_names),
            category_default=self.category_default,
            default_changelog=self.default_changelog,
        )
        return iter(d.items())
