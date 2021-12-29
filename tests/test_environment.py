from unittest import TestCase

from serlo.environment import Environment, EnvironmentConfig

class EnvironmentConfigTest(TestCase):

    def test_get_url(self):
        env_config = EnvironmentConfig(Environment.STAGING)

        self.assertEqual(env_config.get_url(subdomain="api", path="/graphql"),
                         "https://api.serlo-staging.dev/graphql")
        self.assertEqual(env_config.get_url(scheme="http"),
                         "http://serlo-staging.dev/")

        env_config = EnvironmentConfig(Environment.PRODUCTION)

        self.assertEqual(env_config.get_url(subdomain="api", path="/graphql"),
                         "https://api.serlo.org/graphql")

    def test_get_auth(self):
        self.assertEqual(EnvironmentConfig(Environment.STAGING).get_auth(),
                         ("serloteam", "serloteam"))
        self.assertIsNone(EnvironmentConfig(Environment.PRODUCTION).get_auth())
