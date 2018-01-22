#!/usr/bin/python3

DOCUMENTATION = '''  
---
module: json-to-idm
short_description: Takes a json variable and converts it to the correct IDM variables.
'''

EXAMPLES = '''  
- name: Convert json to idm format.
  json-to-idm:
    json_input: "{{ json_list }}"
  register: result
'''

from ansible.module_utils.basic import *
import json
import datetime


def convert_format(json_input):
    users, groups = [], []
    for user in json.loads(json_input):
        user_data = {}
        try:
            user_data['first_name'] = user['first_name']
            user_data['last_name'] = user['last_name']
            user_data['email'] = user['email']
            user_data['user_name'] = user['email'].split("@")[0]
            user_data['group'] = user['group'].split(', ')
            if 'expiration_date' in user and user['expiration_date'] != '':
                try:
                    user_data['expiration_date'] = datetime.datetime.strptime(user['expiration_date'],
                                                                              '%Y-%m-%d').strftime('%Y%m%d%H%M%S')
                except ValueError:
                    user_data['expiration_date'] = ''
        except KeyError:
            continue
        users.append(user_data)
        for my_group in user_data['group']:
            if not any(group['name'] == my_group for group in groups):
                            groups.append({'name': my_group, 'members': [user_data['user_name']]})
            else:
                for group in groups:
                    if group['name'] == my_group:
                        group['members'].append(user_data['user_name'])
    return users, groups


# Takes the outputted json from the list_all function and returns it as the expected
# Ansible format.
def return_json(data):
    users, user_groups = convert_format(data['json_input'])
    has_changed = False
    meta = {"status": "Pulled data", "users": users, "user_groups": user_groups}
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
