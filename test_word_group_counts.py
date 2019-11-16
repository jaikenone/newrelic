import pytest
import subprocess


def test_stdin():
    result = subprocess.getoutput(
        ['echo "this is the life" | ./word_group_counts']
    )
    expected = "Top 100 results for stdin\n" \
        "---------------------------------\n" \
        "1 - this is the\n" \
        "1 - is the life\n" \
        "---------------------------------\n"
    assert result == expected

def test_stdin_not_enough_words():
    result = subprocess.getoutput(
        ['echo "Nothing" | ./word_group_counts -j']
    )
    assert result == "{}"

def test_from_file(script_runner):
    ret = script_runner.run('word_group_counts','test_file1.txt', '-t', '1', '-j')
    assert ret.success
    assert ret.stdout == '{"i went to": 3}\n'
    assert ret.stderr == ''

def test_from_mulitple_files(script_runner):
    ret = script_runner.run('word_group_counts','test_file1.txt', 'test_file2.txt', '-t', '1', '-j')
    assert ret.success
    assert ret.stdout == '{"i went to": 3}\n{"house of usher": 2}\n'
    assert ret.stderr == ''

def test_missing_file(script_runner):
    ret = script_runner.run('word_group_counts','missing_file.txt', '-t', '1', '-j')
    assert ret.success
    assert ret.stdout == "[Errno 2] No such file or directory: 'missing_file.txt'\n"
    assert ret.stderr == ''