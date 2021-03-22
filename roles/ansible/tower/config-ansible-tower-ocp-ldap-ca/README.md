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
|openshift_project|OCP project in which Ansible Tower is deployed|no|'tower'|
|ansible_tower.ldap.ca_cert| Path to CA pem file to be uploaded to Ansible Tower - file must be named "ldap.pem" |yes||

## Example Inventory

```yaml
---

ansible_tower:
 ldap:
  - ca_cert: "{{ inventory_dir }}../files/ldap.pem"
```

## Example Playbook

```yaml
---

- hosts: ansible-tower
  roles:
  - role: config-ansible-tower-ocp-ldap-ca
```
