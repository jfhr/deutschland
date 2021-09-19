"""
    Auswärtiges Amt OpenData Schnittstelle

    Dies ist die Beschreibung für die Schnittstelle zum Zugriff auf die Daten des Auswärtigen Amtes im Rahmen der OpenData Initiative.  Deaktivierung Die Schnittstelle kann deaktiviert werden, in dem Fall wird ein leeres JSON zurückgegeben.  Fehlerfall:  Im Fehlerfall wird ein leeres JSON Objekt zurückgegeben.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import travelwarning
from travelwarning.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_healthcare(self):
        """Test case for get_healthcare

        Gibt die Merkblätter des Gesundheitsdienstes zurück  # noqa: E501
        """
        pass

    def test_get_representatives_country(self):
        """Test case for get_representatives_country

        Gibt eine Liste der deutschen Vertretungen im Ausland zurück  # noqa: E501
        """
        pass

    def test_get_representatives_germany(self):
        """Test case for get_representatives_germany

        Gibt eine Liste der ausländischen Vertretungen in Deutschland zurück  # noqa: E501
        """
        pass

    def test_get_single_travelwarning(self):
        """Test case for get_single_travelwarning

        Gibt einen Reise- und Sicherheitshinweis zurück  # noqa: E501
        """
        pass

    def test_get_state_names(self):
        """Test case for get_state_names

        Gibt das Verzeichnis der Staatennamen zurück  # noqa: E501
        """
        pass

    def test_get_travelwarning(self):
        """Test case for get_travelwarning

        Gibt alle Reise- und Sicherheitshinweise zurück  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
