from unittest import TestCase

from serlo.utils import get_domain, get_subdomain

class TestUtils(TestCase):
    def test_get_domain(self):
        self.assertEqual(get_domain("https://de.serlo.org/"), "serlo.org")
        self.assertEqual(get_domain("https://serlo.org/"), "serlo.org")
        self.assertEqual(get_domain("https://org/"), "org")

    def test_get_subdomain(self):
        self.assertEqual(get_subdomain("https://de.serlo.org/"), "de")
        self.assertEqual(get_subdomain("https://serlo.org/"), "")
