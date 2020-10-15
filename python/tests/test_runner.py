""" Test the main executable """
# Standard library
import pathlib
from io import StringIO

# Third party
import pytest

# Local
from skeletons.runner import (
        parse_args,
        check_environment,
        check_args,
        save)

proj_dir = pathlib.Path(__file__).parent.parent.absolute()
def test_parse_args():
    """ Test argument parsing """

    # Test defaults
    args = parse_args("".split())
    assert not args.ifile_name or args.ofile_name
    assert args.log_level

    # Test any complicated argument parsing

def test_check_environment(monkeypatch):
    """ Test runtime environment checks """
    monkeypatch.delenv("PYTHONPATH")
    with pytest.raises(SystemExit):
        check_environment()

def test_check_args(caplog, tmpdir, monkeypatch):
    """ Test checks on parsed arguments """

    # Check existing input file
    argv = ["-i", f"{proj_dir}/data/input.json"]
    check_args(parse_args(argv))

    # Check non-existent input file
    caplog.clear()
    argv = ["-i", "foo.bar"]
    with pytest.raises(SystemExit):
        check_args(parse_args(argv))
    assert caplog.records[0].message == 'Cannot find input file: foo.bar'

    # Check non-existent output file
    ofile = tmpdir.join("foo.bar")
    argv = ["-o", ofile.strpath]
    check_args(parse_args(argv))

    # Check existing output file
    ofile = tmpdir.join("output.txt")
    ofile.write("Test")
    argv = ["-o", ofile.strpath]

    monkeypatch.setattr('sys.stdin', StringIO('Y\n'))
    check_args(parse_args(argv))

    monkeypatch.setattr('sys.stdin', StringIO('N\n'))
    with pytest.raises(SystemExit):
        check_args(parse_args(argv))
    ## Check unacceptable user input
    monkeypatch.setattr('sys.stdin', StringIO('A\nB\nC\nN'))
    with pytest.raises(SystemExit):
        check_args(parse_args(argv))

def test_save(tmpdir):
    """ Test saving results """
    ofile = tmpdir.join("output.txt")
    save(ofile.strpath, [1,2])
    assert ofile.readlines()
