# OpenShift Container Platform (OCP) related playbooks

These playbooks are mean to assist with creating OpenShift Platform objects in an automated way. Please checkout the `ocp/admin-*` roles for management of individual features of the platform, while playbooks with various combinations of these roles are managed in this directory.


## Prerequisites

1. HashiCorp Vault (for secret management)
2. A vSphere cluster or ESXIi host with vCenter (only required for the IPI install role)
3. All required secrets stored in vault (vCenter password, kubeadmin password, ssh keys, etc...)


## Roles

- [Network bonding](roles/ocp/bonding)
- [NFS storage](roles/ocp/registry-nfs-storage)
- [HTPasswd users](roles/ocp/htpasswd-users)
- [Alertmanager](roles/ocp/alertmanager) 
