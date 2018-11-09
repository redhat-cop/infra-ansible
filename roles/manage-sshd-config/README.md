manage_sshd_config role
=========

This role updates `/etc/ssh/sshd_config` to deny ssh password authentication for root.

## Requirements
This role needs to be executed by a user with 'become' privileges

## Role Variables

The following variables controls the functionality of `manage_sshd_config` role

| Name | Purpose|Required|
|---|---|---|
|update_sshd_config|This dictionary provides the lines that need to be changed in the `/etc/ssh/sshd_config` files|No|

### Example Inventory: update /etc/ssh/sshd_config  

```
[all:vars]
update_sshd_config:
  PermitRootLogin: "without-password"

[servers]
server1.test.lab
server2.test.lab
```

### Example Playbook

```
- hosts: all
  become: yes

  roles:
    - manage_sshd_config
```

### Example Execution

```
ansible-playbook -i inventory  playbook.yml
```

### Manual tests
Execute 'Example' inventory above

#### Test password access denied
`ssh root@server1.test.lab `

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
