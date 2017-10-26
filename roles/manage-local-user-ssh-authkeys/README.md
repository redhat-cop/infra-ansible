manage_user_ssh_authkeys role
=========

This role updates the authorized_keys for the provided user.

## Requirements
This role needs to be executed by a user with 'become' privileges

## Role Variables

The following variables controls the functionality of `manage_local_user_ssh_authkeys` role

| Name | Purpose|Required|
|---|---|---|
|user_name|Identify the username that should be update|Yes|
|key_url|Provide a link to the authorized_keys file that should be installed for the user|No|
|reset_keyfile|When set to `yes`, the user's `authorized_keys` file will be replaced with values from `key_url`, otherwise it will be augmented with the contents|No|

When `key_url` is set, the authorized_keys file will be used for the `user_name` provided.

### Example Inventory: update user  

```
[all:vars]

user_name: user1
authorized_keyfile: "{{ inventory_dir }}/authorized_keys"
key_url: "{{ lookup('file', authorized_keyfile) }}"
reset_keyfile: yes

[servers]
server1.test.lab
server2.test.lab
```
### Example Playbook

```
- hosts: all
  become: yes

  roles:
    - manage_local_user_ssh_authkeys ```

### Example Execution

```
ansible-playbook -i inventory  test.yml -e "user_name=user1"  ```
```ansible-playbook -i inventory  test.yml -e "user_name=user1 reset_keyfile=no"  ```

### Manual tests
Execute 'Example' inventory above
#### Test ssh key update
`ssh -i id_rsa_user1 user1@server1.test.lab /usr/bin/hostnamectl`

###### No password prompt required therefore using updated authorized_keys file.
