config-ansible-tower-subscription-manifest
==========================================

This role is used to provide an Ansible Tower instance with a subscription manifest

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

Check the top level [README](../README.md) for additional/common variables.

The variables used to configure the Ansible Tower subscription are outlined in the table below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.install.manifest_file|Path to valid Ansible Tower manifest content|yes||


## Example Inventory
```yaml
ansible_tower:
  admin_username: "admin"
  admin_password: "admin123"
  install:
    manifest_file: "{{ inventory_dir }}/../files/example-manifest.json"
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: config-ansible-tower-subscription-manifest
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
