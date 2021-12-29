import urllib.parse

from enum import Enum

class Environment(Enum):
    PRODUCTION = "serlo.org"
    STAGING = "serlo-staging.dev"

class EnvironmentConfig:
    def __init__(self, env=Environment.STAGING):
        self.env = env

    def get_url(self, scheme="https", subdomain="", path="/", query=""):
        parts = (scheme, self.get_netloc(subdomain), path, "", query, "")

        return urllib.parse.urlunparse(parts)

    def get_auth(self):
        if self.env == Environment.STAGING:
            return ("serloteam", "serloteam")

        return None

    def get_netloc(self, subdomain):
        return ".".join([subdomain, self.domain]) if subdomain else self.domain

    @property
    def domain(self):
        return self.env.value
