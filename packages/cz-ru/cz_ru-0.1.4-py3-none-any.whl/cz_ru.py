import os
import re

from commitizen import defaults
from commitizen.cz.base import BaseCommitizen
from commitizen.cz.utils import multiple_line_breaker, required_validator
from commitizen.defaults import Questions
from commitizen.cz.exceptions import CzException

__all__ = ["CzRu"]


def parse_scope(text):
    if not text:
        return ""

    scope = text.strip().split()
    if len(scope) == 1:
        return scope[0]

    return "-".join(scope)


def parse_subject(text):
    if isinstance(text, str):
        text = text.strip(".").strip()

    return required_validator(text, msg="Краткое описание обязательно.")


class CzRu(BaseCommitizen):
    bump_pattern = defaults.bump_pattern
    bump_map = defaults.bump_map
    bump_map_major_version_zero = defaults.bump_map_major_version_zero
    commit_parser = r"^((?P<change_type>feat|fix|refactor|perf|BREAKING CHANGE)(?:\((?P<scope>[^()\r\n]*)\)|\()?(?P<breaking>!)?|\w+!):\s(?P<message>.*)?"
    change_type_map = {
        "feat": "Feat",
        "fix": "Fix",
        "refactor": "Refactor",
        "perf": "Perf",
    }
    changelog_pattern = defaults.bump_pattern

    def questions(self) -> Questions:
        questions: Questions = [
            {
                "type": "list",
                "name": "prefix",
                "message": "Выберите тип изменений, которые вы вносите",
                "choices": [
                    {
                        "value": "fix",
                        "name": "fix: Исправление бага. Соответствует ПАТЧ-версии в SemVer",
                        "key": "x",
                    },
                    {
                        "value": "feat",
                        "name": "feat: Новый функционал. Соответствует МИНОРНОЙ версии в SemVer",
                        "key": "f",
                    },
                    {
                        "value": "docs",
                        "name": "docs: Изменения, касающиеся документации",
                        "key": "d",
                    },
                    {
                        "value": "style",
                        "name": "style: Изменения, не затрагивающие смысл кода (пробелы, форматирование, пропущенная пунктуация и т.д.)",
                        "key": "s",
                    },
                    {
                        "value": "refactor",
                        "name": "refactor: Изменение в коде, которое не исправляет баг и не добавляет новый функционал",
                        "key": "r",
                    },
                    {
                        "value": "perf",
                        "name": "perf: Изменение в коде, улучшающее производительность",
                        "key": "p",
                    },
                    {
                        "value": "test",
                        "name": "test: Добавление недостающих или исправление существующих тестов",
                        "key": "t",
                    },
                    {
                        "value": "build",
                        "name": "build: Изменения, затрагивающие систему сборки или внешние зависимости (примеры области: pip, docker, npm)",
                        "key": "b",
                    },
                    {
                        "value": "ci",
                        "name": "ci: Изменения в конфигурации и скриптах CI (пример области: GitLabCI)",
                        "key": "c",
                    },
                ],
            },
            {
                "type": "input",
                "name": "scope",
                "message": "В какой области внесены изменения? (название класса или файла): (нажмите [enter], чтобы пропустить)\n",
                "filter": parse_scope,
            },
            {
                "type": "input",
                "name": "subject",
                "filter": parse_subject,
                "message": "Напишите лаконичную сводку изменений, используя неопределённо-личную форму: (в нижнем регистре, без точки)\n",
            },
            {
                "type": "input",
                "name": "body",
                "message": "Добавьте дополнительный контекст изменений: (нажмите [enter], чтобы пропустить)\n",
                "filter": multiple_line_breaker,
            },
            {
                "type": "confirm",
                "message": "Это изменение ОБРАТНО НЕСОВМЕСТИМО? Соответствует МАЖОРНОЙ версии в SemVer",
                "name": "is_breaking_change",
                "default": False,
            },
            {
                "type": "input",
                "name": "footer",
                "message": "Примечания. Информация об обратно несовместимых изменениях, а также задачах, которые этот коммит закрывает: (нажмите [enter], чтобы пропустить)\n",
            },
        ]
        return questions

    def message(self, answers: dict) -> str:
        prefix = answers["prefix"]
        scope = answers["scope"]
        subject = answers["subject"]
        body = answers["body"]
        footer = answers["footer"]
        is_breaking_change = answers["is_breaking_change"]

        if scope:
            scope = f"({scope})"
        if body:
            body = f"\n\n{body}"
        if is_breaking_change:
            footer = f"BREAKING CHANGE: {footer}"
        if footer:
            footer = f"\n\n{footer}"

        message = f"{prefix}{scope}: {subject}{body}{footer}"

        return message

    def example(self) -> str:
        return (
            "fix: исправлены незначительны опечатки в коде\n"
            "\n"
            "подробности об исправленных опечатках в описании задачи\n"
            "\n"
            "закрывает задачу #12"
        )

    def schema(self) -> str:
        return (
            "<type>(<scope>): <subject>\n"
            "<BLANK LINE>\n"
            "<body>\n"
            "<BLANK LINE>\n"
            "(BREAKING CHANGE: )<footer>"
        )

    def schema_pattern(self) -> str:
        PATTERN = (
            r"(?s)"  # To explicitly make . match new line
            r"(build|ci|docs|feat|fix|perf|refactor|style|test|chore|revert|bump)"  # type
            r"(\(\S+\))?!?:"  # scope
            r"( [^\n\r]+)"  # subject
            r"((\n\n.*)|(\s*))?$"
        )
        return PATTERN

    def info(self) -> str:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dir_path, "cz_ru_info.txt")
        with open(filepath, encoding=self.config.settings["encoding"]) as f:
            content = f.read()
        return content

    def process_commit(self, commit: str) -> str:
        pat = re.compile(self.schema_pattern())
        m = re.match(pat, commit)
        if m is None:
            return ""
        return m.group(3).strip()


class InvalidAnswerError(CzException): ...
