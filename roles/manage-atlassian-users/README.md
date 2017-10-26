Create Atlassian Users Role
=========

An ansible role that manages atlassian users.


Role Variables
--------------

This is a sample of a YAML file containing the variables.

```
---
atlassian_url: https://test.atlassian.net
atlassian_username: admin
atlassian_password: admin
atlassian_users:
  - firstname: Test
    lastname: 123
    password: password123
    email: test@example.com
    groups:
      - a
      - b
atlassian_groups:
  - abc
```

Here are the description of each variables:

- `atlassian_url`: the url of the site we want to manage users in
- `atlassian_username`: username of an admin of that site
- `atlassian_password`: password of the user that has admin priviledge
- `atlassian_users`: a list of dictionaries with user data
- `atlassian_groups`: a list of groups to be managed (can be an empty list)

Due to the sensitive nature of the variables it's best to use ansible-vault to create the `vars.yml`

Steps:
1. `$ ansible-vault create vars.yml` it will ask for a password and it will be needed when we're running the playbook later
2. Specify the variables in the file and save it

Running the Playbook
--------------------

`$ ansible-playbook -e "@path/to/vars.yml" playbooks/manage-users/manage-atlassian-users.yml --ask-vault-pass` and enter the password you've previously set for vars.yml

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: manage-atlassian-users }
