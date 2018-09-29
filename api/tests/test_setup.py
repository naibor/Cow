# Test suit for application setup code
import json

from tests import BaseTestCase

class AppBoilerPlateTestCase(BaseTestCase):
    """
    A set of test for application setup code
    """

    def test_root_redirects_to_docs(self):
        """Testing application root redirects to API docs
        """

        response = self.test_client.get(
            "/"
        )
        self.assertEqual(response.status_code, 302)
        response = self.test_client.get(
            "/",
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Deja-moo", response.data.decode())

    def test_app_throws_404_error_in_json(self):
        """Testing that the application returns 404 errors in
        json for none existent routes/endpoints
        """

        response = self.test_client.get(
            "/non/existent/route",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.data.decode())
        self.assertEqual(
            response_data["message"],
            "The requested URL was not found on the server. " + \
            "If you entered the URL manually please check your spelling and try again."
        )
