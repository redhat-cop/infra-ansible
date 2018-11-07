#!/usr/bin/env python

'''
Dynamic inventory for pulling data from a Google Sheet.
'''

import os
import sys
import argparse
from configparser import ConfigParser
import gspread
from oauth2client.service_account import ServiceAccountCredentials

config = ConfigParser()

config.read('./config.ini')

try:
    import json
except ImportError:
    import simplejson as json


def get_credentials(cred_file):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(cred_file, scope)
    return gspread.authorize(credentials)


def blank_if_missing(key, value):
    try:
        return key[value]
    except:
        return ''


def list_all(spreadsheet_url, worksheet_name, cred_file):
    wks = open_sheet(spreadsheet_url, worksheet_name, cred_file)
    vals = wks.get_all_values()
    headers = []
    for header in vals[0]:
        headers.append(header)
    del vals[0]
    json_list = []
    for row in vals:
        row_data = dict(zip(headers, row))
        json_list.append(dict((k, v) for k, v in row_data.items() if v))

    new_list = {
        "users_and_groups": {
            "users": [],
            "groups": []
        }
    }

    for user in json_list:
        new_list['users_and_groups']['users'].append({
            "first_name": blank_if_missing(user, 'first_name'),
            "last_name": blank_if_missing(user, 'last_name'),
            "user_name": blank_if_missing(user, 'user_name'),
            "email": blank_if_missing(user, 'email'),
            "expiration_date": blank_if_missing(user, 'expiration_date'),
        })
        if user['role']:
            if not user['role'] in new_list['users_and_groups']['groups']:
                new_list['users_and_groups']['groups'].append({"name": user['role'],
                                           "users": []})
            for group in new_list['users_and_groups']['groups']:
                if group['name'] == user['role']:
                    group['users'].append(user['user_name'])

    return new_list


def return_json(data):
    json_list = list_all(data['spreadsheet_url'], data['worksheet_name'], data['credentials_src'])
    has_changed = False
    meta = {"status": "Pulled data", "json": json_list}
    return has_changed, meta


# Returns the specified worksheet.
def open_sheet(spreadsheet, worksheet, cred_file):
    gc = get_credentials(cred_file)
    wks = gc.open_by_url(spreadsheet).worksheet(worksheet)
    return wks


class GoogleSheetInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = list_all(config['default']['spreadsheet_url'], config['default']['sheet'],
                                      config['default']['credentials_file'])
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory))

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()


# Get the inventory.
GoogleSheetInventory()
