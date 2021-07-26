config-ansible-tower-license
=========================

This role is used to provide an Ansible Tower instance with a license

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

Check the top level [README](../README.md) for additional/common variables.

The variables used to configure the Ansible Tower license are outlined in the table below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.install.license_file|Path to valid Ansible Tower license content|yes||


## Example Inventory
```yaml
ansible_tower:
  admin_username: "admin"
  admin_password: "admin123"
  install:
    license_file: "{{ inventory_dir }}/../files/example-license.json"
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: config-ansible-tower-license
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
