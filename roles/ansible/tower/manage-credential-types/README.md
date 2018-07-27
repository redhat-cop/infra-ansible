manage-credential-types
=======================

This role manages custom credential types for Ansible Tower, ensuring the credential type(s) provided in the Ansible inventory exists with the properties specified in the Inventory

Requirements
------------

Ansible version >= 2.4

Role Variables
--------------

The variables used to maintain the Credential Types must be defined in the Ansible Inventory using the `ansible_tower_credential_types` dictionary as explained below.

Credential Types dictionary skeleton variables
----------------------------------------------

```yaml
ansible_tower_credential_types:
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
      id: "<REPLACE WITH CORRESPONDIG CREDENTIAL TYPE ID>"
```