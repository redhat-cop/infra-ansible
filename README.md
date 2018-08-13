# Infra-Ansible

Infra-Ansible was created as a supporting repo to [casl-ansible](https://github.com/redhat-cop/casl-ansible), and to house infrastructure provisioning playbooks and roles - such as DNS, DHCP, etc. This repo has since grown to provide automation for an even broader scope, and for components typically found in a modern data center.

**Note:** This repository is meant for non-container based implementations and infrastructure components. Anything container (and OpenShift) related should be considered submitted to the [casl-ansible](https://github.com/redhat-cop/casl-ansible) repo.



This includes tasks like the following (but not limited to) automated:
- Ansible prep and [Ansible Tower](/tree/master/roles/ansible/tower) install + admin of Tower content.
- [admin and provisioning of OpenStack Platform](/tree/master/roles/osp) ([networks](/tree/master/roles/osp/admin-network), [storage](/tree/master/roles/osp/admin-volume), [tenants](/tree/master/roles/osp/admin-project), [instances](/tree/master/roles/osp/admin-instance), etc).
- provisioning of [DHCP](/tree/master/roles/dhcp), [DNS (bind)](/tree/master/roles/config-dns-server) and [HAproxy](/tree/master/roles/load-balancers/manage-haproxy) infrastructure.
- [DNS](/tree/master/roles/dns) record management (nsupdate, Route53)
- generic [bastion deployment](/tree/master/playbooks/provision-bastion) (including docker, authentication, GUIs, etc)
- [provisioning](/tree/master/playbooks/provision-satellite-server) and [admin](/tree/master/roles/config-satellite) of Satellite 6 servers.
- management and admin of storage solutions ([NFS](/tree/master/roles/nfs-server), [iSCSI](/tree/master/roles/config-iscsi-client), [LVMs](/tree/master/roles/config-lvm), etc.)
- [libvirt](/tree/master/roles/config-libvirt) installs and [VM management](/tree/master/roles/virt-install) ([PXE booting](/tree/master/roles/config-pxe), [vlans](/tree/master/roles/config-vlans)/[bonds](/tree/master/roles/config-bonding)/[routes](/tree/master/roles/config-routes))
- user management with [IdM](/tree/master/roles/idm) and local users + IdM/IPA integrated hosts
- RHEL [subscription](/tree/master/roles/rhsm) management
- 3rd party tooling, such as [Atlassian](/tree/master/roles/user-management) SaaS suite
