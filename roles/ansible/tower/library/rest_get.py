#!/usr/bin/python
# Copyright 2018 Red Hat, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-

import requests
import json

"""
An ansible module to wrap the calls to Ansible Tower REST API (and potentially others).
Main purpose is to better handle REST pagination
"""

# pylint: disable=redefined-builtin,wildcard-import,unused-wildcard-import
from ansible.module_utils.basic import *


DOCUMENTATION = '''
---
module: rest_get
short_description: Perform REST Calls to get data and to better handle REST pagination
author: Øystein Bedin
requirements: [ ]
'''
EXAMPLES = '''
- rest_get:
    host_url: "https://tower.example.com"
    api_uri: "/api/v2/projects/"
    rest_user: "user"
    rest_password: "passwd"
'''


def main():
  module = AnsibleModule(
    argument_spec=dict(
      host_url=dict(required=True),
      api_uri=dict(required=True),
      rest_user=dict(required=True),
      rest_password=dict(required=True, no_log=True),
    ),
    supports_check_mode=True,
  )

  # Initialize the output list to empty
  rest_output = []

  # Retrieve the parameters passed in
  host_url         = module.params['host_url']
  api_uri          = module.params['api_uri']
  rest_user        = module.params['rest_user']
  rest_password    = module.params['rest_password']

  # Loop till the 'next' element contains Null/None
  while api_uri != None:
    r = requests.get(
          '{0}{1}'.format(host_url, api_uri),
          auth=(rest_user, rest_password),
          headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          verify=False
        )

    # Fetch the next URI returned by the REST call
    # TODO: better error handling when REST service returns non-200 OK
    api_uri = r.json()['next']

    # Merge the results json to the output list of items
    rest_output = rest_output + r.json()['results']

  module.exit_json(
    changed=False,
    rest_output=rest_output
  )

if __name__ == '__main__':
    main()
