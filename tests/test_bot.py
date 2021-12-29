from unittest import TestCase

from serlo import SerloBot, Environment

class SerloBotTest(TestCase):

    def test_login(self):
        bot = SerloBot(Environment.STAGING)

        bot.login("inyono", "123456")

        assert bot.get_access_token() != None

    def test_api_call(self):
        self.assertEqual(
            SerloBot().api_call(
                query="""
                    query($id: Int!) {
                        uuid(id: $id) {
                            id
                        }
                    }
                """,
                variables={ "id": 1 }),
            { "uuid": { "id": 1 } })
