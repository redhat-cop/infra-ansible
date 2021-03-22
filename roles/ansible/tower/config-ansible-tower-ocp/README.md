config-ansible-tower-ocp
========================

This role is used to deploy and configure an Ansible Tower running as containers in OpenShift. This role is based on the existing Red Hat official sources to deploy Tower in OCP - [ansible-tower-openshift-setup-3.8.1-1](https://releases.ansible.com/ansible-tower/setup_openshift/ansible-tower-openshift-setup-3.8.1-1.tar.gz)

## Requirements

  - A running OpenShift Cluster and installed 'oc' client in the Ansible host


## Role Variables

The variables used to install Ansible Tower on OpenShift are outlined in the table below. 

**Note:** Authentication shall be based on either username/token. You can specify username and password and role will automatically retrieve token. Note that if a token is specified, the username/password will be ignored.

**Note:** As Tower Installer is based on Ansible playbooks, you may want to customize specific parts of it. You can copy over specific files by pointing to zip archive which contains new files along with the directory structure.

**Note:** Tower installer supports PostgreSQL deployment done in two way, EmptyDir and PVC based. If you choose EmptyDir (openshift_pg_emptydir=true) be aware that PostgreSQL storage is not going to be persisted in any way. If you choose PVC, and the PVC doesn't exist, this playbook will automatically create a PVC(and underlying PV) based on default configuration of you clusters PV plugin. If PVC does exist, playbook will use it.


| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower_download_url|URL of Ansible Tower installer artifact repository|no|`https://releases.ansible.com/ansible-tower/setup_openshift/ansible-tower-openshift-setup-{{ ansible_tower_version }}.tar.gz`|
|ansible_tower_version|Version of Ansible Tower Openshift installer|no|3.8.1-1|
|ansible_tower_remote_src|Is the Ansible Tower installer fetched from a remote source|no|true|
|openshift_host|OpenShift API url|no|CRC on local host|
|openshift_project|Project where to deploy Tower|no|'tower'|
|openshift_user|User to login into openshift|no|"test"|
|openshift_password|OpenShift user password|no(either that or token)||
|openshift_token|OpenShift token|no(either that or password)||
|openshift_skip_tls_verify| Should installer skip TLS verifcation of Openshift API|no|false|
|openshift_pg_emptydir|Flag for Postgre to use EmptyDir for storage(not recommended for Production)|no|true|
|openshift_pg_pvc_name|Persistent Volume Claim to be used for PostgreSQL storage|no|postgresql|
|openshift_pg_pvc_size|Size of PVC that's going to be created for PostgreSQL storage|no|10Gi|
|openshift_pg_pvc_wait_retries|How many attempts should have been taken on PVC readiness check|no|5|
|openshift_pg_pvc_wait_delay|The delay between each attempt on making PVC readiness check (in seconds)|no|30|
|admin_user|Tower admin username|no|"admin"|
|admin_password|Tower admin user password|no|"admin"|
|admin_email|Tower admin user e-mail address|no|root@localhost|
|secret_key|Tower secret key|no|"abcdefghijkx"|
|pg_hostname|PostgreSQL hostname to be used with Tower|no|"postgre"|
|pg_username|PostgreSQL username to be used with Tower|no|"pgu"|
|pg_database|PostgreSQL database to be used with Tower|no|"tower"|
|pg_port|PostgreSQL TCP port to be used with Tower|no|5432|
|pg_sslmode|SSL mode to be used in communication between Tower and PostgreSQL|no|prefer|
|postgress_activate_wait|Time in seconds in which role will wait for PostgreSQL to become available during installation of Tower|no|120|
|ansible_customization_file|Tower Installer may have some bugs in specific versions, this variable points to archive which holds an overlay if any Installer changes are needed|no|N/A|
|tower_vars_overrides|(Dict) Used to override settings in the Tower Installer group_vars/all file. See "Tower Overrides" below for details.|no||
|clean_up|Flag to indicate if the role should perform clean-up at the end|no|'True' - will perform clean-up|

## Example Inventory

```yaml
---

# Initial Tower Config
admin_user: 'admin'
admin_password: 'admin'
secret_key: 'abcdefghijkx'

# Deploy into OpenShift
openshift_host: "https://api.crc.testing:6443"
openshift_skip_tls_verify: "true"
openshift_project: "test-tower"
openshift_user: "kubeadmin"
openshift_password: "XXXXX"

```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: config-ansible-tower-ocp
```

## Tower Overrides

Variables in the installer playbook are found in several places and may change in future releases of the Tower installer:

- inventory 
- group_vars/all 
- roles/kubernetes/defaults/main.yml

Most variables are set through the included [inventory.j2](templates/inventory.j2) template. However, there are some advanced use cases which require overriding the `group_vars/all` file inside of the bundled Tower installer. This role is designed to allow new variables to be set through the inventory using the `tower_vars_overrides` dict.

For example, the Ansible Tower documentation recommends adding [custom virtual environments](https://docs.ansible.com/ansible-tower/3.8.1/html/administration/openshift_configuration.html#build-custom-virtual-environments) requires extending the ansible-tower-ocp base image and uploading the container image to your own repository. You can then override the `group_vars/all` file using a dict like the one below:

```yaml
tower_vars_overrides:
  kubernetes_awx_image: registry.redhat.io/ansible-tower-38/ansible-tower-rhel7
  kubernetes_awx_version: 3.8.1
  foo: bar
```

Note that existing variables will be replaced. New variables, such as `foo: bar` in the example above, will be appended to the end of the `group_vars/all` file if it does not already exist as a top level variable. Use with caution when replacing variables outside of the documented use cases.

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
