"""
    Auswärtiges Amt OpenData Schnittstelle

    Dies ist die Beschreibung für die Schnittstelle zum Zugriff auf die Daten des Auswärtigen Amtes im Rahmen der OpenData Initiative.  Deaktivierung Die Schnittstelle kann deaktiviert werden, in dem Fall wird ein leeres JSON zurückgegeben.  Fehlerfall:  Im Fehlerfall wird ein leeres JSON Objekt zurückgegeben.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import travelwarning
from travelwarning.model.response_warning_response import ResponseWarningResponse
globals()['ResponseWarningResponse'] = ResponseWarningResponse
from travelwarning.model.response_warning import ResponseWarning


class TestResponseWarning(unittest.TestCase):
    """ResponseWarning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseWarning(self):
        """Test ResponseWarning"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseWarning()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
