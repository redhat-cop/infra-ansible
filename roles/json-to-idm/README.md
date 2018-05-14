json-to-idm
===========

This role/module works to convert a json input into two variables ready to be used for the `manage-users` role for IdM management.

You can use this in combination with the `fetch-data-gsheets` role to pull data from a Google Sheet and then set the correct variables to be used for IdM.

The inputted json should look like this (these key values are important):
```json
...
{
    "first_name": "Ella",
    "last_name": "Vader",
    "email": "ella.vader@example.com",
    "expiration_date": "2018-02-13",
    "group": "test_group_1, test_group_2"
},
...
```
The expiration date is optional.

Requirements
------------

* Python 3

Role Variables
--------------


* `json_input`: This is the input variable which will be converted into the two output variables (as facts) `atlassian_users` & `atlassian_groups`.

Dependencies
------------


Example Playbook
----------------
Info on the credentials.json can be found in the fetch-data-gsheets README.

```yaml
- hosts: localhost
  vars:
    credentials_src: /my/path/to/credentials.json
    spreadsheet_url: https://docs.google.com/spreadsheets/d/insert_spreadsheet_extension
    worksheet_name: Sheet1
    ipa_admin_user: admin
    ipa_admin_password: 'my_password'
    ipa_host: idm.example.com
  roles:
    - fetch-data-gsheets
    - json-to-idm
    - manage-users
```


