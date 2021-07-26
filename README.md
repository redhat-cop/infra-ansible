# infra-ansible

![Repo Linter](https://github.com/redhat-cop/infra-ansible/workflows/Repo%20Linter/badge.svg)

infra-ansible was created as a supporting repo to [casl-ansible](https://github.com/redhat-cop/casl-ansible), and to house infrastructure provisioning playbooks and roles - such as DNS, DHCP, etc. This repo has since grown to provide automation for an even broader scope, and for components typically found in a modern data center.

**Note:** This repository is meant for non-container based implementations and infrastructure components. Anything container (and OpenShift) related should be considered submitted to the [casl-ansible](https://github.com/redhat-cop/casl-ansible) repo.



This includes tasks like the following (but not limited to) automated:
- Ansible prep and [Ansible Tower](roles/ansible/tower) install + admin of Tower content.
- [admin and provisioning of OpenStack Platform](roles/osp) ([networks](roles/osp/admin-network), [storage](roles/osp/admin-volume), [tenants](roles/osp/admin-project), [instances](roles/osp/admin-instance), etc).
- provisioning of [DHCP](roles/dhcp), [DNS (bind)](roles/dns) and [HAproxy](roles/load-balancers/manage-haproxy) infrastructure.
- [DNS](roles/dns) record management (nsupdate, Route53)
- generic [bastion deployment](playbooks/provision-bastion) (including docker, authentication, GUIs, etc)
- [provisioning](playbooks/provision-satellite-server) and [admin](roles/config-satellite) of Satellite 6 servers.
- management and admin of storage solutions ([NFS](roles/nfs-server), [iSCSI](roles/config-iscsi-client), [LVMs](roles/config-lvm), etc.)
- [libvirt](roles/config-libvirt) installs and [VM management](roles/virt-install) ([PXE booting](roles/config-pxe), [vlans](roles/config-vlans)/[bonds](roles/config-bonding)/[routes](roles/config-routes))
- user management with [IdM](playbooks/provision-idm-server) and local users + IdM/IPA integrated hosts
- RHEL [subscription](roles/rhsm) management
- 3rd party tooling, such as [Atlassian](roles/identity-management) SaaS suite
