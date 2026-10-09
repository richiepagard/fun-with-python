import unittest

from get_url_subdomain.get_subdomain import subdomain_extractor


class TestSubdomainExtractor(unittest.TestCase):
    """
    Test cases for the subdomain extractor tool.
    Class for testing the subdomain extraction functionality.

    Arguments:
        unittest (module): The unittest module for testing.
    """
    def setUp(self):
        """
        Set up test URLs for the subdomain extractor tests.
        Preparing URLs for different scenarios.
        """
        self.normal_https = 'https://subdomain.example.com'
        self.messy_https = 'HtTPs://subdomain.example.com'
        self.normal_http = 'http://example.com'
        self.messy_http = 'htTp://example.com'
        self.normal_www = 'www.example.com'
        self.messy_www = 'WwW.example1.example2.example3.com'

    def test_subdomain_extractor_https(self):
        """
        Test subdomain extraction from HTTPS URLs.
        """
        self.assertEqual(subdomain_extractor(self.normal_https.lower()), 'subdomain')
        self.assertEqual(subdomain_extractor(self.messy_https.lower()), 'subdomain')

    def test_subdomain_extractor_http(self):
        """
        Test subdomain extraction from HTTP URLs.
        """
        self.assertEqual(subdomain_extractor(self.normal_http.lower()), 'example')
        self.assertEqual(subdomain_extractor(self.messy_http.lower()), 'example')

    def test_subdomain_extractor_www(self):
        """
        Test subdomain extraction from WWW URLs.
        """
        self.assertEqual(subdomain_extractor(self.normal_www.lower()), 'www')
        self.assertEqual(
            subdomain_extractor(self.messy_www.lower()),
            "subdomains are: ['www', 'example1', 'example2'], but the main subdomain is: www"
        )


if __name__ =='__main__':
    unittest.main()
