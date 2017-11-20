# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase


# Create your tests here.
class ProjectTest(TestCase):
    def setUp(self):
        print "in setup"

    def test_get_project_list(self):
        print "testing"

    def tearDown(self):
        print "in tearDown"
