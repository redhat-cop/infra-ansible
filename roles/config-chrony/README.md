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
# The following variable is required to allow your network subnet to access the ntp service. Default value is 127.0.0.1.

chrony_allow_subnet: 192.168.0.1

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

