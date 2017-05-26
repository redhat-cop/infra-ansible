dhcp-config
=========

This role defines the necessary configuration files to build the site specific data

Requirements
------------

This role expect the dhcpd configuration to be located at /etc/dhcp/dhcp.conf

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

The following variables are defined in the defaults and should be overridden in the var directory
```
# vars file for dhcp-config
dhcp_host_entries:
- host: test1
  fqdn: test1.example.com
  hw_addr: e0:07:1b:ec:fd:ec
  ip_addr: 192.168.10

- host: test2
  fqdn: test2.example.com
  hw_addr: e0:07:1b:fd:a5:70
  ip_addr: 192.168.11


#
# Define the subnet entries
#
dhcp_subnet_entries:
- subnet: 192.168.11.0
  netmask: 255.255.255.0
  range: 192.168.11.50 192.168.11.99
  mask: 255.255.255.0
  router: 192.168.11.1
  broadcast: 192.168.11.255
  dns: 8.8.8.8, 8.8.4.4
  domain_search: example.com 
  domain_name: example.com
  next_server: 192.168.11.33

- subnet: 192.168.12.0
  netmask: 255.255.255.0
  range: 192.168.12.50 192.168.12.99
  mask: 255.255.255.0
  router: 192.168.12.1
  broadcast: 192.168.12.255
  dns: 8.8.8.8, 8.8.4.4
  domain_search: example.com 
  domain_name: example.com
  next_server: 192.168.12.33

dhcp_group_entries:
- group:
  title: '# Test group 1'
  hosts:
  - desc: '# Blade #1 - interface "ens1f0"'
    name: node1
    hw_addr: 00:0a:f7:57:e1:f0
    ip_addr: 192.168.11.121
    fqdn: node3.example.com

  - desc: '# Blade #2 - interface "ens1f0"'
    name: node2
    hw_addr: 00:0a:f7:57:dd:80
    ip_addr: 192.168.11.122
    fqdn: node4.example.com

- group: 
  title: '#Test group 2 '
  hosts:
  - desc: '# Blade #3 - interface "ens1f0"'
    name: node3
    hw_addr: 00:0a:f7:57:dd:80
    ip_addr: 192.168.11.123
    fqdn: node5.example.com

  - desc: '# Blade #4 - interface "ens1f0"'
    name: node4
    hw_addr: 00:0a:f7:57:de:54
    ip_addr: 192.168.11.124
    fqdn: node6.example.com

```
### Example generated output
```

```

Dependencies
------------

role: dhcp

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or ar website (HTML is not allowed). 
