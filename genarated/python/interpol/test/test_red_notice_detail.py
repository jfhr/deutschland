"""
    Interpol: Interpol Red Notices API

    Interpol Red Notices Website API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import interpol
from interpol.model.red_notice_detail_arrest_warrants import RedNoticeDetailArrestWarrants
from interpol.model.red_notice_detail_embedded import RedNoticeDetailEmbedded
from interpol.model.red_notice_detail_links import RedNoticeDetailLinks
globals()['RedNoticeDetailArrestWarrants'] = RedNoticeDetailArrestWarrants
globals()['RedNoticeDetailEmbedded'] = RedNoticeDetailEmbedded
globals()['RedNoticeDetailLinks'] = RedNoticeDetailLinks
from interpol.model.red_notice_detail import RedNoticeDetail


class TestRedNoticeDetail(unittest.TestCase):
    """RedNoticeDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRedNoticeDetail(self):
        """Test RedNoticeDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RedNoticeDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
