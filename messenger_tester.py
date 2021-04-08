#!/usr/bin/env/python

#imports
import json
import os
import sqlite3
import tempfile
import unittest

import messenger
import settings


class MessengerBaseTestCase(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary database and create the needed table"""
        messenger.app.config.from_object(settings)
        self.db_fd, messenger.app.config['DATABASE'] = tempfile.mkstemp()
        messenger.app.config['TESTING'] = True
        self.app = messenger.app.test_client()

        with sqlite3.connect(messenger.app.config['DATABASE']) as conn:
            sql_path = os.path.join(messenger.app.config['APP_ROOT'], 'db_init.sql')
            with open(sql_path, 'r') as sql_file:
                cmd = sql_file.read()
                c = conn.cursor()
                c.execute(cmd)
                conn.commit()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(messenger.app.config['DATABASE'])

    # Helper functions for testing login/logout
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

