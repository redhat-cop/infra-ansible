Create Confluence Space Role
=========

An ansible role that manage a confluence space that is a copy of a source space.

Requirements
------------

Confluence server must already be installed on the destination machine.

Role Variables
--------------

All of the following variables needs to be set.

- `confluence_space_destination_url`
- `confluence_space_source_url`
- `confluence_space_source_space_key`
- `confluence_space_name`
- `confluence_space_description`
- `source_confluence_site_username`
- `source_confluence_site_password`
- `destination_confluence_site_username`
- `destination_confluence_site_password`

Due to the sensitive nature of the variables it's best to use ansible-vault to create the `vars.yml`

Steps:
1. `$ ansible-vault create vars.yml` it will ask for a password and it will be needed when we're running the playbook later
2. Specify the variables in the file and save it

Running the Playbook
--------------------

`$ ansible-playbook -e "@path/to/vars.yml" playbooks/manage-confluence-space.yml --ask-vault-pass` and enter the password you've previously set for vars.yml

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: confluence-space-copy }
