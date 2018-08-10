# Infra-Ansible

Infra-Ansible was created as a supporting repo to [casl-ansible](https://github.com/redhat-cop/casl-ansible), and to house infrastructure provisioning playbooks and roles - such as DNS, DHCP, etc. This repo has since grown to provide automation for an even broader scope, and for components typically found in a modern data center.

**Note:** This repository is meant for non-container based implementations and infrastructure components. Anything container (and OpenShift) related should be considered submitted to the [casl-ansible](https://github.com/redhat-cop/casl-ansible) repo.



This includes tasks like the following (but not limited to) automated:
- Ansible prep and [Ansible Tower](https://github.com/redhat-cop/infra-ansible/tree/master/roles/ansible/tower) install + admin of Tower content.
- [admin and provisioning of OpenStack Platform](https://github.com/redhat-cop/infra-ansible/tree/master/roles/osp) ([networks](https://github.com/redhat-cop/infra-ansible/tree/master/roles/osp/admin-network), [storage](https://github.com/redhat-cop/infra-ansible/tree/master/roles/osp/admin-volume), [tenants](https://github.com/redhat-cop/infra-ansible/tree/master/roles/osp/admin-project), [instances](https://github.com/redhat-cop/infra-ansible/tree/master/roles/osp/admin-instance), etc).
- provisioning of [DHCP](https://github.com/redhat-cop/infra-ansible/tree/master/roles/dhcp), [DNS (bind)](https://github.com/redhat-cop/infra-ansible/tree/master/roles/config-dns-server) and [HAproxy](https://github.com/redhat-cop/infra-ansible/tree/master/roles/load-balancers/manage-haproxy) infrastructure.
- [DNS](https://github.com/redhat-cop/infra-ansible/tree/master/roles/dns) record management (nsupdate, Route53)
- generic [bastion deployment](https://github.com/redhat-cop/infra-ansible/tree/master/playbooks/provision-bastion) (including docker, authentication, GUIs, etc)
- [provisioning](https://github.com/redhat-cop/infra-ansible/tree/master/playbooks/provision-satellite-server) and [admin](https://github.com/redhat-cop/infra-ansible/tree/master/roles/config-satellite) of Satellite 6 servers.
- management and admin of storage solutions ([NFS](https://github.com/redhat-cop/infra-ansible/tree/master/roles/nfs-server), [iSCSI](https://github.com/redhat-cop/infra-ansible/tree/master/roles/config-iscsi-client), [LVMs](https://github.com/redhat-cop/infra-ansible/tree/master/roles/config-lvm), etc.)
- [libvirt](https://github.com/redhat-cop/infra-ansible/tree/master/roles/config-libvirt) installs and [VM management](https://github.com/redhat-cop/infra-ansible/tree/master/roles/virt-install) ([PXE booting](https://github.com/redhat-cop/infra-ansible/tree/master/roles/config-pxe), [vlans](https://github.com/redhat-cop/infra-ansible/tree/master/roles/config-vlans)/[bonds](https://github.com/redhat-cop/infra-ansible/tree/master/roles/config-bonding)/[routes](https://github.com/redhat-cop/infra-ansible/tree/master/roles/config-routes))
- user management with [IdM](https://github.com/redhat-cop/infra-ansible/tree/master/roles/idm) and local users + IdM/IPA integrated hosts
- RHEL [subscription](https://github.com/redhat-cop/infra-ansible/tree/master/roles/rhsm) management
- 3rd party tooling, such as [Atlassian](https://github.com/redhat-cop/infra-ansible/tree/master/roles/user-management) SaaS suite
