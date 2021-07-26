config-docker
=============

The config-docker role is associated with configuring a docker set up.

Effectively, the `docker.yml` task will install packages for docker and add users to the docker user group.

Requirements
------------

* A username for configuring docker access


Role Variables
--------------

Defaults file has example of variables that can be used.

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**docker_install**|  Used to determine if Docker should be installed. | yes | False |
|**docker_username**| Used to configure which user should have access to use docker and be part of the 'docker' group. | yes | False |


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
