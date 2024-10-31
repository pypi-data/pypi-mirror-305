from requests_cache import CachedSession

# Python standard library
import os
from datetime import datetime
from hashlib import blake2b
from pathlib import Path
from typing import Optional


class SWHAClient:
    BASE_URL = "https://archive.softwareheritage.org/api/1/"

    def __init__(self, session: CachedSession, offline: bool = False):
        self.session = session
        self.offline = offline
        self.bearer_token: Optional[str] = None

    def read_bearer_token(self, path: Path) -> None:
        with open(path) as f:
            self.bearer_token = f.read().strip()

    def get_origins(self, rev_sha1_git: str) -> set[str]:
        ret = self._get_shwa_origins(rev_sha1_git)
        ret.update(self._get_github_origins(rev_sha1_git))
        return ret

    def _get_shwa_origins(self, sha1_git: str) -> set[str]:
        ret = set()
        if self.bearer_token or self.offline:
            swhid = f"swh:1:rev:{sha1_git}"
            url = SWHAClient.BASE_URL + f"graph/leaves/{swhid}/"
            url += "?direction=backward&edges=rev:rev,rev:snp,snp:ori"
            url += "&resolve_origins=true"
            headers = {"Authorization": f"Bearer {self.bearer_token}"}
            resp = self.session.get(url, headers=headers, only_if_cached=self.offline)
            if resp.status_code != 404:
                resp.raise_for_status()
                ret.update(resp.content.decode().splitlines())
        return ret

    def _get_github_origins(self, rev_sha1_git: str) -> set[str]:
        ret = set()
        url = "https://api.github.com/search/commits"
        query = {"q": "hash:" + rev_sha1_git}
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "hidos",
        }
        resp = self.session.get(
            url, params=query, headers=headers, only_if_cached=self.offline
        )
        if resp.status_code != 404:
            resp.raise_for_status()
            for it in resp.json().get("items", []):
                full_name = it.get("repository", {}).get("full_name")
                if full_name:
                    ret.add("https://github.com/" + full_name + ".git")
        return ret

    def get_revision_archive_dates(self, origins: set[str]) -> dict[str, datetime]:
        ret: dict[str, datetime] = dict()
        merge: dict[datetime, set[str]] = dict()
        for origin in origins:
            for t, revs in self._get_revision_visit_times(origin).items():
                merge.setdefault(t, set())
                merge[t] |= revs
        for t, revs in merge.items():
            for rev_hex in revs:
                if rev_hex not in ret or t < ret[rev_hex]:
                    ret[rev_hex] = t
        return ret

    def _get_revision_visit_times(self, origin: str) -> dict[datetime, set[str]]:
        ret: dict[datetime, set[str]] = dict()
        url = SWHAClient.BASE_URL + f"origin/{origin}/visits/?per_page=1024"
        resp = self.session.get(url, only_if_cached=self.offline)
        if resp.status_code != 404:
            resp.raise_for_status()
            for visit in resp.json():
                t = datetime.fromisoformat(visit["date"])
                ret.setdefault(t, set())
                ret[t] |= self._get_snapshot_revisions(visit["snapshot"])
        return ret

    def _get_snapshot_revisions(self, snp_hex: str) -> set[str]:
        url = SWHAClient.BASE_URL + f"snapshot/{snp_hex}/"
        resp = self.session.get(url, only_if_cached=self.offline)
        resp.raise_for_status()
        data = resp.json().get("branches", {}).values()
        return set(d["target"] for d in data if d.get("target_type") == "revision")


def github_search_commits(hexsha: str, cache: Optional[Path]) -> dict[str, str]:
    if cache is None:
        cs = CachedSession("hidos_http_cache", use_cache_dir=True)
    else:
        cs = CachedSession(cache)
    swha = SWHAClient(cs)
    bearer_token_path = os.environ.get("SWHA_BEARER_TOKEN_PATH")
    if bearer_token_path:
        swha.read_bearer_token(Path(bearer_token_path))
    ret = dict()
    for url in swha.get_origins(hexsha):
        key = blake2b(digest_size=4)
        key.update(url.encode())
        ret[key.hexdigest()] = url
    return ret
