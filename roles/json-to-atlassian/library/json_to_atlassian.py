#!/usr/bin/python3

DOCUMENTATION = '''  
---
module: json-to-atlassian
short_description: Takes a json variable and converts it to the correct IDM variables.
'''

EXAMPLES = '''  
- name: Convert json to atlassian format.
  json-to-atlassian:
    json_input: "{{ json_list }}"
  register: result
'''

from ansible.module_utils.basic import *
import json
import datetime


def convert_format(json_input):
    atlassian_users, atlassian_groups = [], []
    for user in json.loads(json_input):
        user_data = {}
        if 'atlassian_account' in user and user['atlassian_account'] == 'yes':
            try:
                user_data['firstname'] = user['first_name']
                user_data['lastname'] = user['last_name']
                user_data['email'] = user['email']
                if 'atlassian_groups' in user and user['atlassian_groups'] != '':
                    user_data['groups'] = user['atlassian_groups'].split(", ")
                    for group in user_data['groups']:
                        if group not in atlassian_groups:
                            atlassian_groups.append(group)
                atlassian_users.append(user_data)
            except KeyError:
                continue
    return atlassian_users, atlassian_groups


# Takes the outputted json from the list_all function and returns it as the expected
# Ansible format.
def return_json(data):
    atlassian_users, atlassian_groups = convert_format(data['json_input'])
    has_changed = False
    meta = {"status": "Pulled data", "atlassian_users": atlassian_users, "atlassian_groups": atlassian_groups}
    return has_changed, meta


# Main Ansible module definition
def run_module():
    fields = {
        "json_input": {"required": True, "type": "json"},
        "state": {
            "default": "present",
            "choices": ['present'],
            "type": "str"
        }
    }
    choice_map = {
        "present": return_json,
    }
    module = AnsibleModule(argument_spec=fields)
    has_changed, result = choice_map.get(module.params['state'])(module.params)
    module.exit_json(changed=has_changed, meta=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
