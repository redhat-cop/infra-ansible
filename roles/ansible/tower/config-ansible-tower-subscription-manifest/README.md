config-ansible-tower-subscription-manifest
=========================

This role is used to provide an Ansible Tower instance with a subscription manifest

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used to configure Ansible Tower LDAP are outlined in the table below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.admin_username|Admin username for the Ansible Tower install|yes||
|ansible_tower.install.manifest_file|Path to valid Ansible Tower manifest content|yes||
|ansible_tower.validate_certs|Wheter or not to validate Ansible Tower SSL Certificate, use `false` when using not trusted certificates |no|true|

**Note:** You should ensure that the ansible_tower.url variable that is being used is not being redirected (i.e. redirected from http -> https, etc.). If there are concerns with how you're getting/setting this URL, you can use the `discover-url-redirect` role found in this repo.

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
