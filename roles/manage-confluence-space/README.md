Create Confluence Space Role
=========

An ansible role that manage a confluence space that is a copy of a source space.

Requirements
------------

Confluence server must already be installed on the destination machine.

Role Variables
--------------

## Role Variables

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**atlassian.confluence.source.username**| Username of source confluence space. Defaults to `atlassian.username` if not provided | no | N/A |
|**atlassian.confluence.source.password**| Password for source confluence space. Defaults to `atlassian.password` if not provided | no | N/A |
|**atlassian.confluence.source.key**| Key of source confluence space | yes | N/A |
|**atlassian.confluence.source.url**| Url for source confluence site. Defaults to `atlassian.url` if not provided | no | N/A |
|**atlassian.confluence.destination.username**| Username of destination confluence space. Defaults to `atlassian.username` if not provided | no | N/A |
|**atlassian.confluence.destination.password**| Password for destination confluence space. Defaults to `atlassian.password` if not provided | no | N/A |
|**atlassian.confluence.destination.key**| Key that will be created for destination confluence space | yes | N/A |
|**atlassian.confluence.destination.url**| Url for destination confluence site. Defaults to `atlassian.url` if not provided | no | N/A |
|**atlassian.confluence.destination.name**| Name of confluence space that will be shown in the UI | yes | N/A |
|**atlassian.confluence.destination.description**| Brief description of the confluence space that will be shown in the UI | yes | N/A |


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
```
    - hosts: servers
      roles:
         - { role: manage-confluence-space }

```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
