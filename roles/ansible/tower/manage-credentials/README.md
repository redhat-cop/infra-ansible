manage-credentials
==================

This role manages custom credential for Ansible Tower, ensuring that other components of the Ansible Tower configuration (e.g.: inventories) have access to what is needed.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used must be defined in the Ansible Inventory using the `ansible_tower.credentials` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.credentials.name|Name to be used for the credential|yes||
|ansible_tower.credentials.description|Description for the credential|no|nothing('')|
|ansible_tower.credentials.organization|Name of the existing org to tie these credentials with|yes||
|ansible_tower.credentials.type|Type of credentials ('machine', 'aws', etc)|yes||
|ansible_tower.credentials.inputs|Additional input parameters|no||


**_Note:_** Credential configuration will **only** happen if the `ansible_tower.credentials` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.

**_Note:_** Credential input will **only** happen if the `ansible_tower.credentials.inputs` portion of the dictionary is defined and complete as per [Tower Credential Types documentation](https://docs.ansible.com/ansible-tower/latest/html/userguide/credentials.html#credential-types).


## Example Inventory

```yaml
---

ansible_tower:
  credentials:
  - name: "Cred1"
    description: "My Credential 1"
    organization: "Default"
    credential_type: "Machine"
  - name: "Cred2"
    description: "My Credential 2"
    organization: "Default"
    credential_type: "Machine"
  - name: "Cred3"
    description: "My Credential 3"
    organization: "Default"
    credential_type: "Ansible Tower"
    inputs:
      host: "localhost"
      username: "my_user"
      password: 'my_password'
      verify_ssl: true
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: manage-credentials
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
