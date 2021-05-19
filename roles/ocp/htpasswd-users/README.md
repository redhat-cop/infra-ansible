Role Name
=========

This role will add users with cluster admin privileges to OpenShift.

Requirements
------------

- Appropriate variables setup in playbook
- An admin password for the ocp cluster
- A list of dictionary items for users/passwords to add as cluster admins (See vault example below)


Role Variables
--------------

See `Example Playbook` below for more specific details on global vars. At a high level, the following variables need to be defined:

- **Vault**
  - `k8s_admin_password`: The password of a valid cluster admin user
  - `admin_users`: The password of the smtp_host user
- **Passed as extra var or environment variable**
  - `vtoken`: The vault token used to obtain secrets

Dependencies
------------

The following python modules are required:

```
hvac
htpasswd
Jinja2
kubernetes
openshift
```

Example vault addition for users/passwords
--------------------------------

```
vault kv put secret/ocp4/kubeadmin pass=XXXXX-XXXXX-XXXXX-XXXXX
vault kv put secret/ocp4/adminUsers users='[{"name":"user1","password":"user1_pass"},{"name":"user1","password":"user2_pass"}]'
```


Example Playbook
----------------

```
---
- hosts: localhost
  vars:
    k8s_admin_user: "kubeadmin"
    # It's good practice to store login credentials in a secure vault and not
    # directly in playbooks.
    k8s_admin_password: "{{ lookup('hashi_vault', 'secret=secret/ocp4/kubeadmin:pass token={{ vtoken }} url=http://vault.example.com:8200') }}"
    admin_users: "{{ lookup('hashi_vault', 'secret=secret/ocp4/adminUsers:users token={{ vtoken }} url=http://vault.example.com:8200') }}"
  module_defaults:
    group/k8s:
      host: https://api.{{cluster_name}}.{{base_domain}}:6443
      verify_ssl: false
  tasks:
    - name: Log in to cluser

      block:
        # It's good practice to store login credentials in a secure vault and not
        # directly in playbooks.
        - name: Log in (obtain access token)
          k8s_auth:
            username: "{{ k8s_admin_user }}"
            password: "{{ k8s_admin_password }}"
          register: k8s_auth_results
        - include_role:
            name: htpasswd-users

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
