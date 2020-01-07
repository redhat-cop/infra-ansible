<<<<<<< HEAD
=======
config-chrony
==============

name: config-chrony
The purpose of this role is to install and configure a basic chrony ntp service. 

Requirements
------------

None

Variables
------------------

Defaults file has example of variables that can be used. There is only one variable you should need to specify.

```
# Variables to set.

```
Example Playbook
----------------
    - name: 'Configure chronyd'
      hosts: infra_hosts
      roles:
        - role: config-chrony
      tags: 
       - configure_infra_hosts


License
-------

MIT

>>>>>>> Update to README file.
