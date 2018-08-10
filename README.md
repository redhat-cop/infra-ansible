# Infra-Ansible

Infra-Ansible was created as a supporting repo to [casl-ansible](https://github.com/redhat-cop/casl-ansible), and to house infrastructure provisioning playbooks and roles - such as DNS, DHCP, etc. This repo has since grown to provide automation for an even broader scope, and for components typically found in a modern data center.

**Note:** This repository is meant for non-container based implementations and infrastructure components. Anything container (and OpenShift) related should be considered submitted to the [casl-ansible](https://github.com/redhat-cop/casl-ansible) repo.



This includes tasks like the following (but not limited to) automated:
- Ansible prep and Ansible Tower install + admin of Tower content.
- admin and provisioning of OpenStack Platform (networks, storage, tenants, instances, etc).
- provisioning of DHCP, DNS (bind) and HAproxy infrastructure.
- DNS record management (nsupdate, Route53)
- generic bastion deployment (including docker, authentication, GUIs, etc)
- provisioning and admin of Satellite 6 servers.
- management and admin of storage solutions (NFS, iSCSI, LVMs, etc.)
- libvirt installs and VM management (PXE booting, vlans/bonds/routes)
- user management with IdM and local users + IdM/IPA integrated hosts
- RHEL subscription management
- 3rd party tooling, such as Atlassian SaaS suite
