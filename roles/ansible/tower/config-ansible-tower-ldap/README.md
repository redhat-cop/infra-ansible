config-ansible-tower-ldap
=========================

This role is used to configure Ansible Tower LDAP for integration with a LDAP service.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used to configure Ansible Tower LDAP are outlined in the table below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.install.ldap.ca_cert|CA Certificate used for LDAP integration|no||
|ansible_tower.install.ldap.uri|ldaps URL for LDAP server|yes||
|ansible_tower.install.ldap.bind_dn|Bind DN used for LDAP integration|yes||
|ansible_tower.install.ldap.bind_password|Bind DN password for LDAP integration|yes||
|ansible_tower.install.ldap.user_search_dn|Search DN for LDAP integration|yes||
|ansible_tower.install.ldap.user_dn_template|User DN template to map users|yes||
|ansible_tower.install.ldap.group_search_dn|Group Search DN to find users part of a group|yes||
|ansible_tower.install.ldap.require_group|Required LDAP group for users to appear|yes||
|ansible_tower.install.ldap.admin_group|LDAP group used to identify Tower Admins|yes||
|ansible_tower.install.ldap.organization_map|see below|yes||
|ansible_tower.install.ldap.team_map|see below|yes||


**_Note:_** LDAP configuration will **only** happen if the `ansible_tower.ldap` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.

### Organization Map

The Organization Map as mentioned in the above LDAP configuration is used to map users/groups to specific Organizations within Ansible Tower. More information on Ansible Tower Organizations can be found [here](https://docs.ansible.com/ansible-tower/latest/html/userguide/organizations.html). For example, the following dictionary will map groups of users to the "Admin Org" and "Support Org":


```yaml
ansible_tower:
  ldap:
    organization_map:
    - name: "My Admin Org"
      admin_group: "cn=tower-admins,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
      user_groups:
      - "cn=tower-users,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
    - name: "My Support Org"
      admin_group: "cn=tower-admins,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
      user_groups:
      - "cn=tower-users,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
      - "cn=tower-support,cn=groups,cn=accounts,dc=test,dc=example,dc=com"

```

### Team Map

The Team Map as mentioned in the above LDAP configuration is used to map users/groups to specific Teams within Ansible Tower. More information on Ansible Tower Teams can be found [here](https://docs.ansible.com/ansible-tower/latest/html/userguide/teams.html). For example, the following dictionary will map groups of users to the "First Team" and "Second Team":

```yaml
ansible_tower:
  ldap:
    team_map:
    - name: "My First Team"
      organization: "First Org"
      user_groups:
      - "cn=users1,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
      - "cn=users2,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
    - name: "My Second Team"
      organization: "Second Org"
      user_groups:
      - "cn=users1,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
```

## Example Inventory

```yaml
---

ansible_tower:
  admin_password: 'admin'
  ldap:
    ca_cert: "{{ inventory_dir }}/../files/ca.crt"
    uri: "ldaps://idm.test.example.com:636"
    bind_dn: "uid=bind-user,cn=users,cn=accounts,dc=test,dc=example,dc=com"
    bind_password: "my-bind-secret"
    user_search_dn: "cn=users,cn=accounts,dc=test,dc=example,dc=com"
    user_dn_template: "uid=%(user)s,cn=users,cn=accounts,dc=test,dc=example,dc=com"
    group_search_dn: "cn=groups,cn=accounts,dc=test,dc=example,dc=com"
    require_group: "cn=tower-users,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
    admin_group: "cn=tower-admins,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
    organization_map:
    - name: "My Admin Org"
      admin_group: "cn=tower-admins,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
      user_groups:
      - "cn=tower-users,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
    - name: "My Support Org"
      admin_group: "cn=tower-admins,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
      user_groups:
      - "cn=tower-users,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
      - "cn=tower-support,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
    team_map:
    - name: "My First Team"
      organization: "First Org"
      user_groups:
      - "cn=users1,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
      - "cn=users2,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
    - name: "My Second Team"
      organization: "Second Org"
      user_groups:
      - "cn=users1,cn=groups,cn=accounts,dc=test,dc=example,dc=com"
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: config-ansible-tower-ldap
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
