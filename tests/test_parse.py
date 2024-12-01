from pathlib import Path

from markdown_it.utils import read_fixture_file
import mdformat
import mdformat._cli
import pytest

FIXTURE_PATH = Path(__file__).parent / "fixtures.md"
fixtures = read_fixture_file(FIXTURE_PATH)


@pytest.mark.parametrize(
    "line,title,text,expected", fixtures, ids=[f[1] for f in fixtures]
)
def test_fixtures__api(line, title, text, expected):
    output = mdformat.text(text, extensions={"tables"})
    print(output)
    assert output.rstrip() == expected.rstrip(), output


@pytest.mark.parametrize(
    "line,title,text,expected", fixtures, ids=[f[1] for f in fixtures]
)
def test_fixtures__cli(line, title, text, expected, tmp_path):
    file_path = tmp_path / "test_markdown.md"
    file_path.write_text(text, encoding="utf-8")
    assert mdformat._cli.run([str(file_path)]) == 0
    md_new = file_path.read_text(encoding="utf-8")
    assert md_new == expected


FIXTURES_COMPACT_PATH = Path(__file__).parent / "fixtures-compact.md"
fixtures_compact = read_fixture_file(FIXTURES_COMPACT_PATH)


@pytest.mark.parametrize(
    "line,title,text,expected", fixtures_compact, ids=[f[1] for f in fixtures_compact]
)
def test_fixtures_compact__api(line, title, text, expected):
    output = mdformat.text(
        text, extensions={"tables"}, options={"compact_tables": True}
    )
    print(output)
    assert output.rstrip() == expected.rstrip(), output


@pytest.mark.parametrize(
    "line,title,text,expected", fixtures_compact, ids=[f[1] for f in fixtures_compact]
)
def test_fixtures_compact__cli(line, title, text, expected, tmp_path):
    file_path = tmp_path / "test_markdown.md"
    file_path.write_text(text, encoding="utf-8")
    assert mdformat._cli.run([str(file_path), "--compact-tables"]) == 0
    md_new = file_path.read_text(encoding="utf-8")
    assert md_new == expected
