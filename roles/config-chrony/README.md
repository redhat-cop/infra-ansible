<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b3d183f912aa0b784b5ef83dd1e27551e5f2b08e
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

<<<<<<< HEAD
<<<<<<< HEAD
```
# Variables to set.
=======
=======
>>>>>>> b3d183f912aa0b784b5ef83dd1e27551e5f2b08e
| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**chrony_allow_subnet**|  required to allow your network subnet to access the ntp service | no | N/A |

<<<<<<< HEAD
>>>>>>> Fixed readme issues and syntax configuration where requested.
=======
>>>>>>> b3d183f912aa0b784b5ef83dd1e27551e5f2b08e

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

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> Update to README file.
=======
Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
>>>>>>> Fixed readme issues and syntax configuration where requested.
=======
Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
>>>>>>> b3d183f912aa0b784b5ef83dd1e27551e5f2b08e
