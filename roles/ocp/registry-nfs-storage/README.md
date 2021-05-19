Role Name
=========

This role will add nfs storage for the internal registry in OpenShift.

Requirements
------------

- Appropriate variables setup in playbook
- An admin password for the ocp cluster


Role Variables
--------------

See `Example Playbook` below for more specific details on global vars. At a high level, the following variables need to be defined:

- **Vault**
  - `k8s_admin_password`: The password of a valid cluster admin user
- **Vars files**
  - `nfs_server`: The nfs host
  - `nfs_path`: The export path on the nfs host
  - `pv_capacity`: The max capacity a pvc is allowed to request
  - `pvc_storage_request`: The size request for this pvc
- **Passed as extra var or environment variable**
  - `token`: The vault token used to obtain secrets

Dependencies
------------

The following python modules are required:

```
hvac
Jinja2
kubernetes
openshift
```

Example vault addition for users/passwords
------------------------------------------

```
vault kv put secret/ocp4/kubeadmin pass=XXXXX-XXXXX-XXXXX-XXXXX
```


Example Playbook
----------------

```
---
- hosts: localhost
  vars:
    cluster_name: "ocp4"
    base_domain: "example.com"
    k8s_admin_user: "kubeadmin"
    # It's good practice to store login credentials in a secure vault and not
    # directly in playbooks.
    k8s_admin_password: "{{ lookup('hashi_vault', 'secret=secret/ocp4/kubeadmin:pass token={{ vtoken }} url=http://vault.example.com:8200') }}"
  module_defaults:
    group/k8s:
      host: https://api.{{cluster_name}}.{{base_domain}}:6443
      verify_ssl: false
  tasks:
    - name: Log in to cluser

      block:
        - name: Log in (obtain access token)
          k8s_auth:
            username: "{{ k8s_admin_user }}"
            password: "{{ k8s_admin_password }}"
          register: k8s_auth_results
        - include_role:
            name: nfs-storage

      always:
      - name: Log out (revoke access token)
        when: k8s_auth_results.k8s_auth.api_key is defined
        k8s_auth:
          state: absent
          api_key: "{{ k8s_auth_results.k8s_auth.api_key }}"
```

**Note:** The playbook must define all required variables before running this playbook


License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
