config-ansible-tower-ocp-ldap-ca
============================

This role is a helper for `config-ansible-tower-ocp` to create and provision CA certificate secret and ConfigMap which is  used to validate connection with LDAP

## Requirements

  -  running OpenShift Cluster
  -  'oc' client installed on the Ansible host


## Role Variables

The variables used to create and deploy CA secret/ConfigMap  Ansible Tower on OpenShift are outlined in the table below. 

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ocp_ca.src|File path to for CA certificate, file should be named "ldap.pem"|yes||
|ocp_ca.openshift_project|Openshift Project for your tower deployment|no|tower|
|ocp_ca.deployment_name| Deployment name under which Ansible Tower is running on OCP |yes||

## Example Inventory

```yaml
---

ocp_ca:
  - src: "{{ inventory_dir }}../files/ldap.pem"
    secret_project: "{{ openshift_project }}
    deployment_name: ansible-tower
```

## Example Playbook

```yaml
---

- hosts: ansible-tower
  roles:
  - role: config-ansible-tower-ocp-ldap-ca
```
