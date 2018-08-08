==========





Set of Roles
============
Mongodb Ansible

This role installs mongodb on the host machines.





Requirements
------------

The control machine SSH key must be on the `authorized_keys` of the DB server machine. To install mongodb, sudo access is required hence the `become: true` in `prep-demo.yml`.



Role Variables
--------------

- `mongodb_ver`: The version of mongodb you want to install
- `os_family`: The os family of your host machine, see (https://repo.mongodb.org/yum/) for the choices.
- `os_ver`: The os version of your host machine. (e.g: '7' for RHEL 7)

Running the Playbook
--------------------

`$ ansible-playbook playbooks/mongodb-ansible.yml --ask-become-pass`

Further Setup
-------------

To further setup the parameter and create user (including creating a user admin) please see the core module `mongodb_parameter` and `mongodb_user` that is part of the ansible core modules.


Dependencies
------------

*

## Example Playbook

```
```



Example Inventory
----------------

```
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
