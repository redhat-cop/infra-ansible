config-chrony
==============

name: config-chrony
The purpose of this role is to install and configure a basic chrony ntp service. 

Requirements
------------

No specific system requirements.

Variables
------------------

Defaults file has example of variables that can be used. There is only one variable you should need to specify.

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**chrony_allow_subnet**|  required to allow your network subnet to access the ntp service | no | N/A |


Example Playbook
----------------

```
- name: 'Configure chronyd'
  hosts: infra_hosts
  roles:
    - config-chrony
  tags: 
    - configure_infra_hosts
```

License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.