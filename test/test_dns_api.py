# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0 - 1.2), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.2
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from environment import HOST, API_TOKEN
from purity_fb import *
import time
from utils import *


class TestDnsApi(unittest.TestCase):
    """ DnsApi unit test stubs """

    def setUp(self):
        self.purity_fb = PurityFb(HOST)
        self.purity_fb.disable_verify_ssl()
        res = self.purity_fb.login(API_TOKEN)
        self.assertTrue(res == 200)
        self.dns = self.purity_fb.dns
        self.old_dns_config = self.dns.list_dns().items[0]

    def tearDown(self):
        self.old_dns_config.name = None
        self.dns.update_dns(dns_settings=self.old_dns_config)
        # sleep 5 seconds for the DNS update to take effect
        time.sleep(5)

    def test_list_dns(self):
        """
        Test case for list_dns
        """
        print('LIST DNS configuration\n')
        res = self.dns.list_dns()
        check_is_list_of(res.items, Dns)

    def test_update_dns(self):
        """
        Test case for update_dns
        """
        new_dns_config = Dns(domain='mydomain',
                             nameservers=['1.2.3.1', '1.2.3.2'],
                             search=['test.rest.python.client.com'])
        res = self.dns.update_dns(dns_settings=new_dns_config)
        check_is_list_of(res.items, Dns)
        res = self.dns.list_dns()
        updated_dns = res.items[0]
        self.assertEqual(new_dns_config.domain, updated_dns.domain)
        self.assertEqual(new_dns_config.nameservers, updated_dns.nameservers)
        self.assertEqual(new_dns_config.search, updated_dns.search)


if __name__ == '__main__':
    unittest.main()