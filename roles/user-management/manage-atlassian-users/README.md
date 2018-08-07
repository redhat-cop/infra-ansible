Create Atlassian Users Role
=========

An ansible role that manages atlassian users.


Role Variables
--------------

This is a sample of a YAML file containing the variables.

```
---
atlassian:
  url: https://example.atlassian.net
  username: example
  password: example

  user:
    - firstname: Test
      lastname: 123
      password: example
      email: test@example.com
      state: present
      groups:
        - a
        - b

  groups:
    - abc
```

Here are the description of each variables:

- `atlassian.url`: the url of the site we want to manage users in
- `atlassian.username`: username of an admin of that site
- `atlassian.password`: password of the user that has admin priviledge
- `atlassian.user`: a list of dictionaries with user data
- `atlassian.user.groups`: a list of groups the user should be added (can be an empty list)
- `atlassian.user.state`: state can be `present` to create user and `absent` to delete user
- `atlassian.groups`: a list of groups to be managed (can be an empty list)

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
