Set of Roles
============

The ansible roles found in this directory are associated with configuring a docker set up.

Effectively, the `docker.yml` task will install packages for docker and add users to the docker user group.

Requirements
------------

1. Docker installed on the host machine.
2. A username for configuring docker access


Role Variables
--------------
docker_install is used to control if Docker should be installed or not. docker_username is used to configure which user should have access to use docker (and hence be part of the 'docker' group).

```
docker_username: root
docker_install: True
```


Dependencies
------------
There are no strict dependencies for this role beyond ansible and docker.

Example Playbooks
----------------

```
- hosts: bastion
  roles:
    - role: config-docker
```

Example Inventory
----------------

```
docker_install: True
docker_username: bob
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
