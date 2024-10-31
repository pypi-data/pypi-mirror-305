import pytest

from hidos.remote import SWHAClient

from requests_cache import CachedSession

import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
REQUESTS_CACHE_DIR = Path(__file__).parent / "requests_cache"
BEARER_TOKEN_PATH = Path(__file__).parent / "swha_bearer_token.txt"


def setup_client(cache_name):
    cs = CachedSession(
        REQUESTS_CACHE_DIR / cache_name,
        backend='filesystem',
        allowable_codes=(200, 404),
        stale_if_error=True,
    )
    client = SWHAClient(cs, offline=True)
    token_path = BEARER_TOKEN_PATH
    if not BEARER_TOKEN_PATH.exists():
        # this is testing offline using cached reponses
        # the real bearer token was only need to get real reponses for the cache
        token_path = "/dev/null"
    client.read_bearer_token(token_path)
    return client


def test_dsgl_spec_doc():
    init_rev = "5466a30a368d3f5520cf9f0a867d4958e11d319f"
    c = setup_client("dsgl_spec")
    repo0 = "https://github.com/document-succession/VGajCjaNP1Ugz58Khn1JWOEdMZ8.git"
    repo1 = "https://gitlab.com/perm.pub/successions.git"
    assert set([repo0, repo1]) == c.get_origins(init_rev)

    assert {} == c.get_revision_archive_dates(set([repo0]))

    with open(DATA_DIR / "dsgl_archive_dates.json") as f:
        expect = {k: datetime.fromisoformat(s) for k, s in json.load(f).items()}

    assert expect == c.get_revision_archive_dates(set([repo0, repo1]))


def test_what_baseprint_doc():
    # base_dsi = "HKSI5NPzMFmgRlb4Vboi71OTKYo"
    init_rev = "1ca488e4d3f33059a04656f855ba22ef5393298a"
    c = setup_client("what_baseprint")
    expect = set([
        'https://gitlab.com/perm.pub/successions/',
        'https://github.com/digital-successions/HKSI5NPzMFmgRlb4Vboi71OTKYo.git',
        'https://gitlab.com/perm.pub/successions.git',
        'https://gitlab.com/castedo/study-docs.git',
    ])
    assert expect == c.get_origins(init_rev)
