manage_ssh_config_root_access role
=========

This role updates `/etc/sshd_config` to deny ssh password authentication for root.

## Requirements
This role needs to be executed by a user with 'become' privileges

## Role Variables

The following variables controls the functionality of `manage_ssh_config_root_access` role

| Name | Purpose|Required|
|---|---|---|
|update_sshd|This variable when set to True will disable root's ability to login via SSH with a password|No|

### Example Inventory: update /etc/ssh/sshd_config  

```
[all:vars]
update_sshd_config: True

[servers]
server1.test.lab
server2.test.lab
```

### Example Playbook

```
- hosts: all
  become: yes

  roles:
    - manage_ssh_config_root_access
```

### Example Execution

```
ansible-playbook -i inventory  test.yml -e "update_sshd=True"  ```

### Manual tests
Execute 'Example' inventory above

#### Test password access denied
`ssh root@server1.test.lab `

