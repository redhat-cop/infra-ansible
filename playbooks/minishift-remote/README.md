# Minishift Remote playbook

This playbook can be executed against an existing host or used to provision a new machine to be utilized as a remote target for Minishift.


## Prerequisites

One of the two options:

* A running host with docker installed and a user who can elevate to root access
* IaaS that allows for provisioning through these playbooks

## Example run

An example inventory can be found in the [inventory/minishift-remote](../../inventory/minishift-remote) directory. 

```
> ansible-playbook -i ../../inventory/minishift-remote main.yml
```


## Inventory Options

| Name | Description | Default|
|---|---|---|
|provision_infrastructure|Whether to provision infrastructure|`True`|
|hosting_infrastructure|IaaS infrastructure used to host Minishift| `openstack`| 
|rhsm_register|Register RHEL machine if utilized| `False` |
|docker_install|Install and configure Docker on remote machine| `true`|
|install_prerequisites|Install dependencies used by Minishift | 80, 443, 2376, 4001 |

Additional options can also be found in the [minishift-remote](../../roles/minishift-remote) role to further tailor the execution.