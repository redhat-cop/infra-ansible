fetch_user_data_gsheets
=======================

This role/module works to extract the user and user group details from Google Sheets. This info is stored in json format as facts which can be used by the manage-users role and any others looking for the users and user_groups variables.

An example spreadsheet would look like this (the order doesn't matter, but the header names do):

| user_name | first_name | last_name | email                 | expiration_date | group      |
|-----------|------------|-----------|-----------------------|-----------------|------------|
| user1     | Brock      | Lee       | brock.lee@example.com |                 | core_users |

Requirements
------------

* Python 3
* pip
* Google service account

Google Service account instructions
-----------------------------------
1. Go to the [Google Developer Console](https://console.developers.google.com/project).
2. Go to the credentials page.
3. Press `Create Credentials` -> `Service account key`.
4. Select `New service account`.
5. Set the Role to `Project -> Editor`. Set the account name and account ID as desired.
6. Create the key with type `json`.
7. Save this .json file to your desired location (the path will need to be referenced later). Note: If storing with your code in a repo, add this file to the `.gitignore`.
8. In the credentials file, find the `client_email` key and copy the matching value. This email is the service account.
9. Add that service account email as an editor into your Google sheet.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.
* `spreadsheet_url`: This is the url of the spreadsheet which the data will get extracted from. It is important to note that the Google Sheet document must give access to the service account (details in requirements section)
* `worksheet_name`: This is the name of the worksheet (page) which contains the user and user group details. For reference, in a default Google Sheet the first worksheet is called Sheet1.
* `credentials_src`: This is the path to the Google service account credentials file (details in requirements section).
    spreadsheet_name: 'TEST_USERS'
    worksheet_name: 'Sheet1'
    credentials_src: 'instance/credentials.json'

Dependencies
------------

The `gspread` and `oauth2client` Python libraries.

Example Playbook
----------------

```yaml
- hosts: localhost
  vars:
    credentials_src: /path/to/.../credentials.json
    spreadsheet_url: https://docs.google.com/spreadsheets/d/xxxxxxxxxxxxxxxxxxxxxxxxx
    worksheet_name: Sheet1
  roles:
    - fetch_user_data_gsheets
```
