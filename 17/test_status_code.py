import unittest
from my_python_repos import r, response_dict


class TestMyPythonRepos(unittest.TestCase):

    def test_status_code(self):
        self.assertEqual(r.status_code, 200)

    def test_total_repo(self):
        self.assertGreater(response_dict['total_count'], 20000)

    def test_returned_repo(self):
        self.assertEqual(len(response_dict['items']), 30)