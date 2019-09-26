manage-ssh-private-keys
=======================

This role manages SSH private keys on remote hosts

## Requirements

Sufficient permissions on the remote host to create directories and files


## Role Variables

The variables used must be defined in the Ansible Inventory using the `ssh_private_keys` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ssh_private_keys.src|Local private key filename to copy|yes||
|ssh_private_keys.dest|Remote file name for the ssh private key|yes||
|ssh_private_keys.owner|Remote owner of the ssh private key|yes||
|ssh_private_keys.group|Remote group of the ssh private key|yes||
|ssh_private_keys.mode|Remote file mode for the private ssh key|no|0400|
|ssh_private_keys.create_dest_dir|Create the remote directory if it doesn't exist|no|false|
|ssh_private_keys.directory_mode|Remote directory mode for the parent directory|no|0700|


## Example Inventory

```yaml
---

ssh_private_keys:
  - src: /home/user1/.ssh/id_rsa_user1
    dest: /var/lib/awx/.ssh/id_rsa_user1
    owner: awx
    group: awx
    create_dest_dir: true
    directory_mode: 0750
  - src: /home/user2/.ssh/id_rsa_user2
    dest: /home/user2/.ssh/id_rsa_user2
    owner: user2
    group: user2
    mode: 0600
```

## Example Playbook

```yaml
---

- hosts: all
  roles:
  - role: manage-ssh-private-keys
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
