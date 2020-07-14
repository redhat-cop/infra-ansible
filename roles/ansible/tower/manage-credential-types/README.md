manage-credential-types
=======================

This role manages custom credential types for Ansible Tower, ensuring the credential type(s) provided in the Ansible inventory exists with the properties specified in the Inventory

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used to maintain the Credential Types must be defined in the Ansible Inventory using the `ansible_tower.credential_types` dictionary as explained below.

**_Note:_** Credential Types configuration will **only** happen if the `ansible_tower.credential_types` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.

## Example inventory

```yaml
ansible_tower:
  credential_types:
  - name: "<REPLACE WITH CREDENTIAL TYPE NAME>"
    description: "<REPLACE WITH CREDENTIAL TYPE DESCRIPTION>"
    fields:
    - type: "<REPLACE WITH VALID CREDENTIAL TYPE>"
      id: "<REPLACE WITH CREDENTIAL TYPE ID>"
      label: "<REPLACE WITH CREDENTIAL TYPE LABEL>"
      secret: "<REPLACE WITH 'true' or 'false'>"
    required:
    - id: "<REPLACE WITH CREDENTIAL TYPE ID>"
    injectors_extra_vars:
    - name: "<REPLACE WITH EXTRA VAR NAME>"
      id: "<REPLACE WITH CORRESPONDING CREDENTIAL TYPE ID>"
```

Also check the [README one level up](../README.md#example-inventory) for additional details of an example inventory.  

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: manage-credential-types
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
