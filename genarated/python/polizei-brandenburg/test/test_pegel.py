"""
    Polizei Brandenburg: App

    Polizei Brandenburg Nachrichten, Hochwasser-, Verkehrs- und Waldbrandwarnungen  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import polizei-brandenburg
from polizei-brandenburg.model.pegel_data import PegelData
globals()['PegelData'] = PegelData
from polizei-brandenburg.model.pegel import Pegel


class TestPegel(unittest.TestCase):
    """Pegel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPegel(self):
        """Test Pegel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Pegel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
