Set of Roles
==========


config-timezone role

This role can be used to configure the timezone of your system.  
Available timezones can be captured via `timedatectl list-timezones`



Requirements
------------

This role need to be executed by a user with `become` privileges

Role Variables
--------------

Dependencies
------------


Example Playbooks
----------------

```
```



Example Inventory
----------------

```
timezone: America/Denver
```
### Note
If the value is not set the role is skipped


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
