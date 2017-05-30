# DHCP

This role installs the dhcp software on the target servers, Opens the proper Firewall rules, and enables the service on to start on boot.

### NOTE
It does not start the service because without a proper /etc/dhcp/dhcp.conf with correctly defined subnets it will fail.   The role dhcp-config will create the file and deploy the configuration.

Dependencies
------------
None:This role needs the dhcp-config role
