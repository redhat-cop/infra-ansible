config-bonding
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
## The following variable is required to allow your network subnet to access the ntp service.
chrony_allow_subnet:

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

