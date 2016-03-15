# -*- coding: utf-8 -*-
from psycopg2 import IntegrityError
from openerp.tests.common import TransactionCase


# ---------------------------------------------------------
# Tests
# ---------------------------------------------------------
class TestCreateIssue(TransactionCase):
    def setUp(self):
        super(TestCreateIssue, self).setUp()
        cr, uid, = self.cr, self.uid
        self.issue = self.env['project.issue']

    #test to confirm you can create an issue in the database
    def testCreateIssue(self):
        self.testIssue = self.issue.create({'name':'testIssue1', 'kanban_state': 'normal', 'email_from': 'test@email.com'})

        self.assertEqual(self.testIssue.name, 'testIssue1')
        self.assertEqual(self.testIssue.kanban_state, 'normal')
        self.assertEqual(self.testIssue.email_from, 'test@email.com')

    #test to confirm you cannot create an invalid Issue
    def testIssueIntegrity(self):
        with self.assertRaises(IntegrityError):
            self.testIssue = self.issue.create({'kanban_state': 'normal'})

    #Test to show you can get partner email from issue
    def testEditIssue(self):
        self.testIssue = self.issue.create({'name':'testIssue1', 'kanban_state': 'normal', 'email_from': 'test@email.com'})
        self.assertEquals(self.testIssue.onchange_partner_id(1)['value']['email_from'], 'info@yourcompany.example.com')

    def tearDown(self):
        super(TestCreateIssue, self).tearDown()
