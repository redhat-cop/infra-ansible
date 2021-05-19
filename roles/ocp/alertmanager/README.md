alertmanager
=========

This role will update the alertmanager secret in OpenShift to a working configuration.

Requirements
------------

- An admin password for the ocp cluster
- Credentials and configuration details for an smtp host
- Appropriate variables setup in playbook


Role Variables
--------------

See `Example Playbook` below for more specific details on global vars. At a high level, the following variables need to be defined:

- **Vault**
  - `k8s_admin_user`: The user id of a valid cluster admin user
  - `k8s_admin_password`: The password of a valid cluster admin user
  - `smtp_pass`: The password of the smtp_host user
- **Vars Files**
  - `base_domain`: A valid base domain
  - `smtp_host`: An smtp host to send mail from
  - `smtp_port`: The port to connect to on the smtp host
  - `smtp_user`: The user id for smtp authentication
  - `mail_to`: Who you will send alerts to
- **Passed as extra var or environment variable**
  - `token`: The vault token used to obtain secrets

Dependencies
------------

The following python modules are required:

```
google-auth
hvac
htpasswd
Jinja2
kubernetes
openshift
```

Example vault entries
---------------------

```
vault kv put secret/ocp4/kubeadmin pass=XXXXX-XXXXX-XXXXX-XXXXX
vault kv put secret/ocp4/googleSmtp pass=My$ecretp@ssw0rd
```

Example Playbook
----------------

```
---
- hosts: localhost
  vars:
    cluster_name: "ocp4"
    base_domain: "example.com"
    smtp_host: ""
    smtp_port: "587"
    smtp_user: "me@gmail.com"
    smtp_from: "admin@{{base_domain}}"
    mail_to: "me@gmail.com"
    k8s_admin_user: "kubeadmin"
    # It's good practice to store login credentials in a secure vault and not
    # directly in playbooks.
    k8s_admin_password: "{{ lookup('hashi_vault', 'secret=secret/ocp4/kubeadmin:pass token={{ vtoken }} url=http://vault.example.com:8200') }}"
    smtp_pass: "{{ lookup('hashi_vault', 'secret=secret/ocp4/googleSmtp:pass token={{ vtoken }} url=http://vault.example.com:8200') }}"
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
            name: alertmanager

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
