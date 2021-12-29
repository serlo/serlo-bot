import json
import requests

from bs4 import BeautifulSoup

from .environment import Environment, EnvironmentConfig
from .utils import get_domain, get_subdomain

class SerloBot:
    def __init__(self, env=Environment.STAGING):
        self.env = EnvironmentConfig(env)
        self.session = SerloSession(self.env)

    def login(self, username, password):
        login_page = self.session.get(
                self.env.get_url(subdomain="en", path="/api/auth/login"),
                headers = {"Referer": self.env.get_url(subdomain="en")})

        login_page.raise_for_status()
        login_html = BeautifulSoup(login_page.text, "html.parser")
        form = login_html.find("form", id="login")

        csrf = form.select('input[name="csrf"]')[0]["value"]
        challenge = form.select('input[name="login_challenge"]')[0]["value"]

        after_login = self.session.post(login_page.url, data={
            "csrf": csrf,
            "login_challenge": challenge,
            "email": username,
            "password": password,
            "submit": "Login",
            "remember": ["0", "1"]
        })

        after_login.raise_for_status()

    def api_call(self, query, variables={}):
        headers = { "Content-Type": "application/json" }
        access_token = self.get_access_token()
        if access_token:
            headers["Authorization"] = "Bearer " + access_token

        response = self.session.post(
                self.env.get_url(subdomain="api", path="/graphql"),
                headers = headers,
                json = { "query": query, "variables": variables })

        if response.status_code not in [200,400]:
            response.raise_for_status()

        result = response.json()

        if "errors" in result and result["errors"]:
            raise requests.HTTPError(result["errors"][0]["message"],
                                     response=response)

        return result["data"]

    def get_access_token(self):
        auth_token = self.session.cookies.get("auth-token",
                                              domain=self.env.get_netloc("en"))

        if auth_token == None:
            return None

        try:
            return json.loads(auth_token).get("access_token", None)
        except json.JSONDecodeError:
            return None

class SerloSession(requests.Session):
    def __init__(self, env):
        self.env = env

        super().__init__()

    def prepare_request(self, request):
        if (self.is_serlo_domain(request.url) and
                get_subdomain(request.url) in ["en", "de", "es", "hi", "ta"]):
            request.auth = self.env.get_auth()

        return super().prepare_request(request)

    def should_strip_auth(self, old_url, new_url):
        if self.is_serlo_domain(old_url) and self.is_serlo_domain(new_url):
            return False
        else:
            return super().should_strip_auth(old_url, new_url)

    def is_serlo_domain(self, url):
        return get_domain(url) == self.env.domain
