manage-settings
===============

This role manages Ansible Tower settings, ensuring that Ansible Tower configuration settings can be part of your playbook.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used must be defined in the Ansible Inventory using the `ansible_tower.settings` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.settings|Ansible Tower settings dictionary|yes||


**_Note:_** Settings configuration will **only** happen if the `ansible_tower.settings` portion of the dictionary is defined. These settings will be merged with the existing settings of Ansible Tower.


## Example Inventory

```yaml
---

ansible_tower:
  settings:
    AWX_PROOT_SHOW_PATHS:
      - /var/lib/awx/.ssh
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: manage-settings
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
