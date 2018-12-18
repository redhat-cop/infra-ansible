manage_local_user_password role
=========

This role updates the password for the provided user.

## Requirements
This role needs to be executed by a user with 'become' privileges

## Role Variables

The following variables controls the functionality of `manage_local_user_password` role

| Name | Purpose|Required|
|---|---|---|
|user_name|Identify the username that should be update|Yes|
|clear_text_password|Provide the plain text password that the user's account should be set to|No|

When `clear_text_password` is set, the local password will be updated for the `user_name` provided.


### Example 1 Inventory: update non-root-user  

```
[all:vars]

user_name: user1
clear_text_password: Pa55word

[servers]
server1.test.lab
server2.test.lab
```

### Example Playbook

```
- hosts: all
  become: yes

  roles:
    - manage_local_user_password ```

### Example Execution

```
ansible-playbook -i inventory  playbook.yml -e "user_name=user1 clear_text_password=BetterPa55word "  ```

### Manual tests
Execute either 'Example' inventory above

#### Test password update
`ssh user1@server1.test.lab /usr/bin/hostnamectl`

###### Enter the new password when prompted, hostnamectl executes.
