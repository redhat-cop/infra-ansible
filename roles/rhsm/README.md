Role Name
=========

This role is used to manage Red Hat subscriptions of the target hosts.

Requirements
------------

1. A valid Red Hat subscription, either directly with redhat.com or through the use of Red Hat Satellite


Role Variables
--------------

See `Example Inventory` below for more specific details. At a high level, the following variables need to be defined:

| variable | info | required? |
|:--------:|:----:|:---------:|
|rhsm_username|Username used to register to access.redhat.com|yes if username/password is used|
|rhsm_password|Password used to register to access.redhat.com|yes if username/password is used|
|rhsm_server_hostname|The Satellite hostname/FQDN used for registration|yes if Satellite registration is used|
|rhsm_activationkey|The Satellite activationkey used for registration|yes if Satellite registration is used|
|rhsm_org_id|The Satellite organization ID used for registration|yes if Satellite registration is used|
|rhsm_pool|The subscription pool name used for registration|no|
|rhsm_repos|A list of repositories to enable|no|
|rhsm_force_register|Set to 'yes' to force a unregister/clean + re-registration|no|


Dependencies
------------

None


Example Playbook
----------------

```
    - hosts: servers
      roles:
      - role: rhsm
```


Example Inventory
----------------


When using Satellite:

```
rhsm_server_hostname: 'sat.example.com'
rhsm_org_id: 'my-org'
rhsm_activationkey: 'my-org-key'

rhsm_repos:
 - "rhel-7-server-rpms"
 - "rhel-7-server-extras-rpms"
```

When using access.redhat.com:

```
rhsm_username: 'my-username'
rhsm_password: 'my-password'

rhsm_repos:
 - "rhel-7-server-rpms"
 - "rhel-7-server-extras-rpms"
```


License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
