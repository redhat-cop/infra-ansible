update_access role
=========

This role updates the password and authorized_key for the provided user

## Requirements
This role needs to be executed by a user with 'become' privileges

An easy way to create an encrypted password is with the following command:

```
python -c 'import crypt; print crypt.crypt("password", crypt.mksalt(crypt.METHOD_SHA512))'
```

## Role Variables

The following variables controls the functionality of `update_access` role

| Name | Purpose|Required|
|---|---|---|
|user_name|Identify the username that should be update|Yes|
|user_name_password|Provide the encrypted password that the username should be set to|No|
|authorized_keyfile|Provide the path to the keyfile that should be installed for the user|No|

If the `authorized_keyfile` is not set, authorized_keys file update is ignored for the `user_name`

If the `user_name_password` is not set, password update is ignored for the `user_name`


### Example Inventory

```
[all:vars]

user_name: user1
user_name_password: $6$uli6pVSIQvDhxX/2$4vOEE0Jvum6OrNwoU78.wqa29m/je9ub3HXUpL6nqYxDjsqRyEAFSdbDAKxkCd0mgE9p2F/kRAPzAwFI5u8wQ1

authorized_keyfile: "{{ inventory_dir }}/authorized_keys"

[servers]
server1.test.lab
server2.test.lab
```
### Example Playbook

```
- hosts: all
  become: yes

  roles:
    - update_access ```

### Example Execution

```
ansible-playbook -i inventory  test.yml -e "user_name=user1 :w
user_name_password=`python -c 'import crypt; print crypt.crypt("password", crypt.mksalt(crypt.METHOD_SHA512))'`" ```

### Manual test
Execute the 'Example' above and try both of the
#### Test ssh key update
`ssh -i id_rsa_user1 user1@server1.test.lab /usr/bin/hostnamectl`

###### Note: No prompt required therefore using authorized_keys file

#### Test password update
`ssh user1@server1.test.lab /usr/bin/hostnamectl`

##### Enter New password when prompted for new password, command executes with new password
