# IdM Server playbook

This playbooks runs through the steps to provision a VM, set it up, configure DNS records, and install IdM.
Currently it is configured to provision OpenStack resources, but other providers can easily be added.


## Prerequisites

For hosting infrastructure, you will need one of the two:
- a set of running instance(s)
- a IaaS that allow for provisioning through these playbooks

You must have a working DNS server which accepts "nsupdate" connections for the IdM VMs forward and reverse DNS records to be added/updated to the existing DNS zones. For this, you will need the DNS zone key names, key secrets, and key algorithms.

## Example

### Inventory

Please see the **sample** inventory in the inventory area:

- [IdM-server](../../inventory/idm-server/README.md)


You will need to modify this sample inventory to fit your desired configuration, including information from your DNS server such as the key names, secrets, and more.


### Playbook execution

Depending on how this is being hosted, the initial may need the `tags='install'` set to ensure all necessary software is installed:

```bash
> ansible-playbook -i inventory main.yml --tags='install'
```

Any consecutive runs can be done without the 'install' tag to speed up execution:
```bash
> ansible-playbook -i inventory main.yml
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
