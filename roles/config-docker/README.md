Set of Roles
============

The ansible roles found in this directory are associated with configuring a docker set up.

Effectively, the `docker.yml` task will install packages for docker and add users to the docker user group. In the `docker.yml` file, only docker is listed under the with_items for packages to be installed, but any number of packages can be included within the task file or you can modify it to take in a set of packages from the inventory.

Requirements
------------

1. Docker installed on the host machine.
2. A set of users to populate


Role Variables
--------------
There are no high priority role variables with a default docker user variables of
```
docker_username: root
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
    - role: config-timezone
```

Example Inventory
----------------

```
docker_install: True
docker_compose_install: True
docker_username: bob
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
