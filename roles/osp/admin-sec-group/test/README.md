Test Directory
=========

Requirements
--------------
1. A valid OpenStack RC file, with the proper access rights to an OpenStack tenant, needs to be sourced before running this test
1. The `openstack` python shade packages to allow for interactions with the platform.


Sample Run
--------------
**Note:** Make sure to source the OpenStack RC file (with proper access rights) before running this test


`ansible-playbook -i inventory test.yml`


Verify
-------------
with the following commands:

`openstack security group show ingress-sec-group`
`openstack security group show egress-sec-group`


