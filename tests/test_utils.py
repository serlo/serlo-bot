from unittest import TestCase

from serlo.utils import get_domain, get_subdomain

def test_get_domain():
    assert get_domain("https://de.serlo.org/") == "serlo.org"
    assert get_domain("https://serlo.org/") == "serlo.org"
    assert get_domain("https://org/") == "org"

def test_get_subdomain():
    assert get_subdomain("https://de.serlo.org/") == "de"
    assert get_subdomain("https://serlo.org/") == ""
