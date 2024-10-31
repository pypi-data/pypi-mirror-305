from . import Archive
from .git import load_openssh_public_key_file, add_remotes
from .dsi import BaseDsi, EditionId
from .remote import github_search_commits
from .exceptions import HidosError

# Python standard libraries
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Any, Optional


def version() -> str:
    try:
        from ._version import version  # type: ignore

        return str(version)
    except ImportError:
        return "0.0.0"


def print_dsi(
    branch_name: str,
    editions: bool = False,
    git_dir: Optional[Path] = None,
    unsigned_ok: bool = False,
) -> None:
    arc = Archive(git_dir, unsigned_ok=unsigned_ok)
    succ = arc.get_succession(branch_name)
    if not succ:
        msg = "Branch {} is not a valid digital succession"
        raise Exception(msg.format(branch_name))
    if editions:
        for ed in succ.root.all_subeditions():
            if ed.has_digital_object:
                print("dsi:{} {}".format(ed.dsi, ed.swhid))
    else:
        print("dsi:" + succ.dsi)


def print_successions(
    git_dir: Optional[Path] = None, unsigned_ok: bool = False
) -> None:
    arc = Archive(git_dir, unsigned_ok=unsigned_ok)
    for dsi, branches in sorted(arc.branches().items()):
        print(f"dsi:{dsi}", " ".join(branches))


def create_succession(
    new_branch: str,
    keys_path: Path,
    git_dir: Optional[Path] = None,
    unsigned_ok: bool = False,
) -> int:
    if not keys_path and not unsigned_ok:
        msg = "Public signing key file path required to create a signed succession."
        print(msg, file=sys.stderr)
        return 2
    try:
        arc = Archive(git_dir, unsigned_ok=unsigned_ok)
    except HidosError:
        msg = (
            "Git directory not found!\n" +
            "You need to use option --git-dir or be inside a git working directory."
        )
        print(msg, file=sys.stderr)
        return 1
    keys = load_openssh_public_key_file(keys_path) if keys_path else None
    arc.create_succession(new_branch, keys=keys)
    print_dsi(new_branch, git_dir=git_dir, unsigned_ok=unsigned_ok)
    return 0


def commit_edition(
    src_path: Path,
    branch: str,
    edition: str,
    unlisted_ok: bool = False,
    git_dir: Optional[Path] = None,
    unsigned_ok: bool = False,
) -> int:
    arc = Archive(git_dir, unsigned_ok=unsigned_ok)
    try:
        edid = EditionId(edition)
        if edid[-1] == 0:
            print(f"Edition number must not end in zero: '{edition}'", file=sys.stderr)
            return 1
        if any(i == 0 for i in edid) and not unlisted_ok:
            msg = "An edition number with a component equal to zero is unlisted."
            print(msg, file=sys.stderr)
            print("Use the --unlisted option if this is intentional.", file=sys.stderr)
            return 1
    except ValueError:
        print(f"Invalid edition number: '{edition}'", file=sys.stderr)
        return 1
    arc.commit_edition(src_path, branch, edition)
    return 0


def find_remotes(
    dsi: str,
    add: bool,
    cache: Optional[Path],
    git_dir: Optional[Path] = None,
    unsigned_ok: bool = False,
) -> int:
    found = github_search_commits(BaseDsi(dsi).sha1_git, cache)
    if not found:
        print("No remote repositories found", file=sys.stderr)
        return 1
    if add:
        add_remotes(found, git_dir)
    else:
        for rid, url in found.items():
            print(rid, url)
    return 0


def main(args: Any = None) -> int:
    parser = ArgumentParser(prog="hidos")
    subparsers = parser.add_subparsers(dest="subcmd")
    parser.add_argument("--version", action="version", version=version())
    parser.add_argument("--git-dir", help="Path to the .git repository directory")
    parser.add_argument(
        "--unsigned",
        action="store_true",
        help="Allow unsigned commits (ONLY FOR TESTING)",
    )
    dsi_parser = subparsers.add_parser(
        "dsi", help="Print digital succession identifier"
    )
    dsi_parser.add_argument("branch", help="Git branch of succession")
    dsi_parser.add_argument(
        "--editions", action="store_true", help="List digital object editions"
    )
    list_parser = subparsers.add_parser(
        "list", help="List git branches of digital successions"
    )
    create_parser = subparsers.add_parser(
        "create", help="Create new digital succession"
    )
    create_parser.add_argument("new_branch", help="Name of new branch")
    create_parser.add_argument(
        "-k", "--keys", type=Path, help="Path to SSH public key file (concatenation)"
    )
    commit_parser = subparsers.add_parser(
        "commit", help="Commit file or directory to digital succession"
    )
    commit_parser.add_argument(
        "--unlisted",
        action="store_true",
        help="Allow unlisted editions (allow edition number with a zero)",
    )
    commit_parser.add_argument(
        "src_path", type=Path, help="Path to file or directory to commit"
    )
    commit_parser.add_argument("branch", help="Branch name of digital succession")
    commit_parser.add_argument("edition", help="Edition number of commit")
    find_parser = subparsers.add_parser(
        "find", help="Find remote repositories for digital succession"
    )
    find_parser.add_argument(
        "--add", action="store_true", help="Add remotes to local git repository"
    )
    find_parser.add_argument("--cache", type=Path, help="HTTP cache file location")
    find_parser.add_argument("dsi", help="Digital Succession Identifier")

    noms = parser.parse_args(args)
    shared = dict(git_dir=noms.git_dir, unsigned_ok=bool(noms.unsigned))
    if noms.subcmd == "dsi":
        print_dsi(noms.branch, editions=noms.editions, **shared)
    elif noms.subcmd == "list":
        print_successions(**shared)
    elif noms.subcmd == "create":
        return create_succession(noms.new_branch, noms.keys, **shared)
    elif noms.subcmd == "commit":
        return commit_edition(
            noms.src_path, noms.branch, noms.edition, noms.unlisted, **shared
        )
    elif noms.subcmd == "find":
        return find_remotes(noms.dsi, noms.add, noms.cache, **shared)
    else:
        parser.print_help()
        return 2
    return 0


if __name__ == "__main__":
    exit(main())
