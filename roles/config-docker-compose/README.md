config-docker-compose
=====================

The config-docker-compose role is associated with installing docker compose packages.

Effectively, the `docker-compose.yml` task will install packages for docker compose.

Requirements
------------

* config-docker role


Role Variables
--------------

Defaults file has example of variables that can be used.

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**docker_install**|  Used to determine if Docker should be installed. | yes | False |

Dependencies
------------
There are no strict dependencies for this role beyond ansible and docker. If Docker is not installed the role will attempt to call the config-docker role to install docker. 

Example Playbooks
----------------

```
- hosts: bastion
  roles:
    - role: config-docker-compose
```

Example Inventory
----------------

```
docker_install: True
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
