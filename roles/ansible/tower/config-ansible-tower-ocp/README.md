config-ansible-tower-ocp
========================

This role is used to deploy and configure an Ansible Tower running as containers in OpenShift. This role is based on the existing Red Hat official sources to deploy Tower in OCP - [ansible-tower-openshift-setup-latest](https://releases.ansible.com/ansible-tower/setup_openshift/ansible-tower-openshift-setup-latest.tar.gz)

## Requirements

  - A running OpenShift Cluster and installed 'oc' client in the Ansible host


## Role Variables

The variables used to install Ansible Tower on OpenShift are outlined in the table below. 

**Note:** Authentication shall be based on either username/token. You can specify username and password and role will automatically retrieve token. Note that if a token is specified, the username/password will be ignored.

**Note:** As Tower Installer is based on Ansible playbooks, you may want to customize specific parts of it. You can copy over specific files by pointing to zip archive which contains new files along with the directory structure.

**Note:** Tower installer supports PostgreSQL deployment done in two way, EmptyDir and PVC based. If you choose EmptyDir be aware that PostgreSQL storage is not going to be persisted in any way. If you choose PVC, and the PVC doesn't exist, this playbook will automatically create a PVC(and underlying PV) based on default configuration of you clusters PV plugin. If PVC does exist, playbook will use it.


| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower_download_url|URL of Ansible Tower installer artifact repository|no|`https://releases.ansible.com/ansible-tower/setup_openshift/ansible-tower-openshift-setup-{{ ansible_tower_version }}.tar.gz`|
|ansible_tower_version|Version of Ansible Tower Openshift installer|no|latest|
|ansible_tower_remote_src|Is the Ansible Tower installer fetched from a remote source|no|true|
|ansible_tower_postdeployment_pause| Time in minutes for which role will wait for Tower to settle down after deployment|no|5|
|ansible_tower.install.openshift.host|OpenShift API url|no|CRC on local host|
|ansible_tower.install.openshift.project|Project where to deploy Tower|no|'tower'|
|ansible_tower.install.openshift.user|User to login into openshift|no|"test"|
|ansible_tower.install.openshift.password|OpenShift user password|no(either that or token)||
|ansible_tower.install.openshift.token|OpenShift token|no(either that or password)||
|ansible_tower.install.openshift.skip_tls_verify| Should installer skip TLS verifcation of Openshift API|no|false|
|ansible_tower.install.openshift.pg_emptydir|Flag for PostgreSQL to use EmptyDir for storage(not recommended for Production)|no|true|
|ansible_tower.install.openshift.pg_pvc_name|Persistent Volume Claim to be used for PostgreSQL storage|no|postgresql|
|ansible_tower.install.openshift.pg_pvc_size|Size of PVC that's going to be created for PostgreSQL storage|no|10Gi|
|ansible_tower.install.openshift.pg_pvc_wait_retries|How many attempts should have been taken on PVC readiness check|no|5|
|ansible_tower.install.openshift.pg_pvc_wait_delay|The delay between each attempt on making PVC readiness check (in seconds)|no|30|
|ansible_tower.install.secret_key|Tower secret key|no|"abcdefghijkx"|
|ansible_tower.install.pg.host|PostgreSQL hostname to be used with Tower|no||
|ansible_tower.install.pg.username|PostgreSQL username to be used with Tower|no|"pgu"|
|ansible_tower.install.pg.password|PostgreSQL username to be used with Tower|no|"pgu"|
|ansible_tower.install.pg.database|PostgreSQL database to be used with Tower|no|"tower"|
|ansible_tower.install.pg.port|PostgreSQL TCP port to be used with Tower|no|5432|
|ansible_tower.install.pg.sslmode|SSL mode to be used in communication between Tower and PostgreSQL|no|"prefer"|
|ansible_tower.install.pg.activate_wait|Time in seconds in which role will wait for PostgreSQL to become available during installation of Tower|no|120|

### Advanced Inventory Configuration 

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_customization_file|Tower Installer may have some bugs in specific versions, this variable points to archive which holds an overlay if any Installer changes are needed|no|N/A|
|ansible_customization_remote_src|Used to indicate if the above ansible_customization_file is a remote src or not|no|false|
|tower_vars_overrides|(Dict) Used to override settings in the Tower Installer group_vars/all file. See "Tower Overrides" below for details.|no||
|clean_up|Flag to indicate if the role should perform clean-up at the end|no|'True' - will perform clean-up|

## Example Inventory

```yaml
---

ansible_tower:
  admin_password: 'admin'
  install:
    secret_key: 'abcdefghijkx'
    openshift:
      host: "https://api.crc.testing:6443"
      project: "test-tower"
      skip_tls_verify: "true"
      user: "kubeadmin"
      password: "XXXXX"

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
