import git
from git.cmd import Git
from git.objects import Blob, Tree, Commit
from git.repo.base import Repo

from .exceptions import SignedCommitVerifyFailedWarning
from .dsi import BaseDsi

# Python standard libraries
import binascii, os, tempfile
from warnings import warn
from pathlib import Path
from typing import Union

# git hash-object -t tree /dev/null
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"

# Persistable/Plain-Old-Data type, a subset of JSON data.
# No float due to rounding errors of float (de)serialization.
POD = Union[None, str, int, list['POD'], dict[str, 'POD']]


def b64url_from_sha1(hexstr: str) -> str:
    warn("Use BaseDsi instead of b64url_from_sha1", DeprecationWarning)
    return str(BaseDsi.from_sha1_git(hexstr))


def sha1_from_b64url(b64url: str) -> str:
    warn("Use BaseDsi instead of sha1_from_b64url", DeprecationWarning)
    return BaseDsi(b64url).sha1_git


def git_path_in_tree(path: str, tree: Tree) -> bool:
    try:
        tree.join(path)
        return True
    except KeyError:
        return False


def git_read_tree_update_files(repo: Repo, treehash: str, work_dir: Path) -> None:
    work_dir = work_dir.resolve()
    os.makedirs(work_dir)
    g = Git(work_dir)
    # also need to set --work-tree git option to get work_dir to work
    g.set_persistent_git_options(git_dir=repo.git_dir, work_tree=work_dir)
    with tempfile.TemporaryDirectory() as tmp:
        g.update_environment(GIT_INDEX_FILE=os.path.join(tmp, "index"))
        # call git read-tree with -m -u options
        g.read_tree(treehash, m=True, u=True)


def add_to_tree(
    repo: Repo, tree: Union[Tree, str], path_in_tree: str, src_path: Path
) -> Tree:
    index = git.IndexFile.from_tree(repo, tree)
    if src_path.is_dir():
        src_path = src_path.resolve()
        g = Git(src_path)  # src_path is working dir
        # also need to set --work-tree git option to get git add to work
        g.set_persistent_git_options(git_dir=repo.git_dir, work_tree=src_path)
        temp_index = git.IndexFile.from_tree(repo, EMPTY_TREE)
        with g.custom_environment(GIT_INDEX_FILE=temp_index.path):
            g.add(".")
            subtree = g.write_tree()
        index.write()
        with g.custom_environment(GIT_INDEX_FILE=index.path):
            g.read_tree(subtree, prefix=path_in_tree)
        index.update()
    else:
        blob_hash = repo.git.hash_object("-w", "--", src_path)
        blob = Blob(
            repo,
            binascii.a2b_hex(blob_hash),
            mode=Blob.file_mode,
            path=path_in_tree,
        )
        index.add([blob])
    return index.write_tree()


def verify_commit(commit: Commit, allowed_signers: Path) -> bool:
    try:
        g = Git()
        g.set_persistent_git_options(
            git_dir=commit.repo.git_dir,
            c=f"gpg.ssh.allowedSignersFile={allowed_signers}",
        )
        g.verify_commit(commit.hexsha)
        return True
    except git.exc.GitCommandError as e:
        warn(str(e), SignedCommitVerifyFailedWarning)
    return False
