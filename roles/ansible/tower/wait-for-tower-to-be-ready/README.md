wait-for-tower-to-be-ready
==========================

This role is used to wait for Tower to become ready - i.e.: Tower URL returns a 200OK

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

Check the top level [README](../README.md) for additional/common variables.

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**ansible_tower.install.wait_delay**|Number of seconds between retries|no|5|
|**ansible_tower.install.wait_retries**|Number of retries while waiting for the Tower API to become available|no|6|


## Example Inventory
```yaml
ansible_tower:
  url: 
  admin_username: "admin"
  admin_password: "admin123"
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: wait-for-tower-to-be-ready
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
