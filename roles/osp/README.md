# OpenStack Platform roles

This sub-directory contains a variety of roles to support installation, configuration and administration of an OpenStack Platform.

## Roles

### Installation
> **Note:** These roles rely on packstack for the installation, mostly meant for a PoC type of environment - i.e.: not production

- packstack-install

### Configuration
> **Note:** These roles rely on a packstack installed environment, however, the nature of the implementation(s) should be generic of nature and hence may as well work on other types of installs.

- packstack-post

### Administration

These are roles used to administer an OpenStack environment, such as add projects/tenants, network setup/modifications, instances, volumes, etc. The implementations are generic and should work on any OpenStack environment. However, note that these have been tested with Red Hat OpenStack Platform version 11, and hence only guaranteed to work with this version.

- admin-image: Manage Images used for booting instances.
- admin-instance: Manage an Instance within the OSP environment.
- admin-keystone-domain: Manage an authentication keystone domain within the OSP environment.
- admin-network: Manage a tenant network and subnet(s).
- admin-nova-flavor: Manage available instance flavors in the OSP environment.
- admin-nova-service: Manage Nova service enable/disable on a host.
- admin-project: Manage projects/tenants within the OSP environment.
- admin-sec-group: Manage Security Group(s) within a project/tenant.
- admin-user: Manage local users within the OSP environment.
- admin-volume-type: Manage available volume types within the OSP environment.
- admin-volume: Manage volumes within a project/tenant.

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
