Minishift Remote
=========

Ansible role to provision and setup a remote target for [Minishift](https://github.com/minishift/minishift).

Requirements
------------

Access to an existing machine that can supports the use of `docker` and `firewalld` along with a user that can elevate themselves to root.

Role Variables
--------------

This role contains a number of variables to customize the deployment of Clair. The following are some of the most important that may need to be configured

| Name | Description | Default|
|---|---|---|
|docker_group|Group name for Docker|`docker`|
|minishift_dependencies|Dependencies required to be present prior to configuring and starting Minishift| `docker, firewalld`| 
|minishift_remote_user|Name of the user Minishift should connect as| Current user executing provisioning (`ansible_user`) |
|minishift_user_ssh_public_key_file|Location of the public key file that should be allowed to connect to minishift| SSH key file used during ansible execution (`ansible_ssh_private_key_file`) or `~/.ssh/id_rsa.pub`|
|minishift_firewalld_ports|Firewall ports to open | 80, 443, 2376, 4001 |
|download_minishift|Download binary of Minishift | `true` |
|minishift_install_dir|Location where Minishift binary should be downloaded | `/usr/local/bin` |
|minishift_tmp_dir|Temporary directory where Minishift archive should be downloaded and stored | `/tmp` |
|minishift_host_ip| IP address OpenShift should use for the master API and routes | `ansible_eth0.ipv4.address` variable |
|minishift_url| Location of the Minishift distribution |  |
|minishift_extra_start_args|Extra arguments to pass to the Minishift start command |  |

Dependencies
------------

* [container-storage-setup](../container-storage-setup)
* [config-docker](../config-docker)

Example Playbook
----------------

```
- name: Configure Minishift Remote
  hosts: minishift_remote
  roles:
    - role: config-minishift-remote
```

The playbook can be executed using the following command:

```
ansible-playbook -i inventory test.yml -e 'minishift_host_ip=127.0.0.1'
```

The above command specifies the IP address that should Minishift should be configured to make use of

## License

Apache License 2.0

## Author Information

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.