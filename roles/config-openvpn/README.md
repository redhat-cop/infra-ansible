
Set of Roles
============
config-openvpn role

## Notes
- This role installs the CentOS flavor of the OpenVPN Access Server package. This can be overriden by using the `openvpn_rpm` variable in the inventory.

- This role doesn't do much of configuration of the OpenVPN server itself beyond the install. The basic steps to have a working OpenVPN server is:
  - Run this role to install the RPM
  - Login to the CLI of the server
  - Set the password for `openvpn` (> passwd openvpn)
  - Login to the admin web interface with the `openvpn` user (> https://\<server\>:943/admin)
  - Make any tweaks as needed in the OpenVPN admin interface. Normally not much is needed beyond adding users or some kind of authentication mechanism (such as LDAP)
  - Install a license

**Note:** make sure to configure the proper NAT rules and firewall policies externally to the OpenVPN server (if applicable)



Requirements
------------



Role Variables
--------------

Dependencies
------------

*

Example Playbooks
----------------

```
```



Example Inventory
----------------

```
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
