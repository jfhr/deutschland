"""
    Deutscher Wetterdienst: API

    Aktuelle Wetterdaten von allen Deutschen Wetterstationen  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import dwd
from dwd.model.warning_coast_warnings import WarningCoastWarnings
globals()['WarningCoastWarnings'] = WarningCoastWarnings
from dwd.model.warning_coast import WarningCoast


class TestWarningCoast(unittest.TestCase):
    """WarningCoast unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWarningCoast(self):
        """Test WarningCoast"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WarningCoast()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
