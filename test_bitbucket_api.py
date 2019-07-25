"""
Unit tests for the bitbucket api library
"""

import bitbucket_api
import unittest
from unittest import mock, TestCase

class TestBitckbucketApi(TestCase):

    def test_get_bitbucket_username(self):
        """
        Test for get_bitbucket_username
        """
        with mock.patch('builtins.input', return_value='user101'):
            actual = bitbucket_api.get_bitbucket_username()
            self.assertEqual(actual, 'user101')
