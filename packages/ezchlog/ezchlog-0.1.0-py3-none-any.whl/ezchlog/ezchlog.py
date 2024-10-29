from enum import Enum
from pathlib import Path
from re import sub

from .config import Config


class StrChainSub:
    def __init__(self, s: str) -> None:
        self.s = s

    def sub(self, regex: str, replacement: str) -> 'StrChainSub':
        return StrChainSub(sub(regex, replacement, self.s))

    def __str__(self) -> str:
        return self.s


class EzChLog:
    def __init__(self) -> None:
        self.cfg = Config()

    @classmethod
    def get_slug(cls, s: str) -> str:
        return str(
            StrChainSub(s.lower())
            .sub(r'\s+', '_')
            .sub(r'\W', '')
            .sub(r'_+', '_'),
        )[:50].strip().strip('_')  # yapf: disable

    def add(self, *, dry_run: bool, message: str, cat: Enum, ref: str) -> tuple[Path, str]:
        first_line = message.split('\n')[0] if '\n' in message else message
        lines = message.split('\n')[1:] if '\n' in message else []
        if not first_line.startswith('- '):
            first_line = '- ' + first_line
        slug = self.get_slug((f'{ref}-' if ref else '') + first_line) + '.md'
        if ref:
            first_line += f" ({ref})"
        lines.insert(0, first_line)
        md_message = '  \n'.join(line.rstrip() for line in lines)
        log_file = self.cfg.log_dir / cat.name / slug
        log_file.parent.mkdir(parents=True, exist_ok=True)
        if not dry_run:
            with log_file.open('w', encoding='utf-8') as f:
                f.write(md_message + '\n')
        return log_file.relative_to(self.cfg.root_dir), md_message

    def list(self) -> list[Path]:
        return [
            p.relative_to(self.cfg.log_dir)
            for cat in list[Enum](self.cfg.category_class)
            for p in sorted((self.cfg.log_dir / cat.name).glob('*.md'))
        ]  # yapf: disable

    def merge(self, *, dry_run: bool, next_version: str) -> str:
        lines_to_insert = [f"## {next_version}"]
        for cat in list[Enum](self.cfg.category_class):
            new_category = True
            for p in sorted((self.cfg.log_dir / cat.name).glob('*.md')):
                if new_category:
                    lines_to_insert.append(f"### {cat.name}")
                    new_category = False
                lines_to_insert.extend(p.read_text(encoding='utf-8').split('\n'))
                p.unlink()
        if self.cfg.log_file.exists():
            lines = self.cfg.log_file.read_text(encoding='utf-8').strip().split('\n')
        else:
            if not dry_run:
                self.cfg.log_file.write_text(self.cfg.default_changelog, encoding='utf-8')
            lines = self.cfg.default_changelog.strip().split('\n')
        if len(lines_to_insert) >= 2:
            pos = 0
            for i, line in enumerate(lines):
                if line.startswith('## '):
                    pos = i
                    break
            else:
                pos = -1
            if pos == -1:
                lines.append("")
                lines.extend(lines_to_insert)
            else:
                lines_to_insert.append("")
                lines = lines[0:pos] + lines_to_insert + lines[pos:]
        changelog = '\n'.join(lines) + '\n'
        if not dry_run:
            self.cfg.log_file.write_text(changelog, encoding='utf-8')
        return changelog
