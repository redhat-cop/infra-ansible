config-docker-compose
=====================

The config-docker-compose role is associated with installing the docker compose packages.

Requirements
------------

N/A


Role Variables
--------------

Defaults file has example of variables that can be used.

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**docker_compose_install**| Should docker compose be installed? | yes | false |
|**docker_compose_packages**| Packages required for docker compose. | no | See list of packages in [defaults/main.yml](defaults/main.yml) |


Dependencies
------------
config-docker role is required.

Example Playbooks
----------------

``` yaml
- hosts: bastion
  roles:
    - role: config-docker-compose
```

Example Inventory
----------------

```
docker_compose_install: true
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
