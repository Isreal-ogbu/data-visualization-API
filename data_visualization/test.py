import unittest
from Functions import apicall


class APITEST(unittest.TestCase):

    # Tested using python accounts
    def setUp(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        self.result = apicall(url)
    
    # Test to check the server condition before performing further process.
    def testcall(self):
        testcode = self.result.testcondition()
        self.assertEqual(200, testcode)
    
    # Tests to checks the Total number of repositorys returned from the API CALL.
    def test_no_of_repos(self):
        val = self.result.amount_of_repository()
        self.assertEqual(30, val)


if __name__ == "__main__":
    unittest.main()
