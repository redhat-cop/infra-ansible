<<<<<<< HEAD
# DNS Server Playbook

This playbook directory has the playbook(s) necessary to manage your DNS server(s).

## Prerequisites

One of the two:
- a set of running instance(s)
- a IaaS that allow for provisioning through these playbooks


## Example

### Inventory

Please see the **sample** inventory in the inventory area:

- [dns-server](../../inventory/dns-server/README.md)

You will need to modify this sample inventory to fit your desired configuration.

### Playbook execution

Depending on how this is being hosted, the initial may need the `tags='install'` set to ensure all necessary software is installed:

```bash
> ansible-playbook -i inventory main.yml --tags='install'
```

Any consecutive runs can be done without the 'install' tag to speed up execution:
```bash
> ansible-playbook -i inventory main.yml
```

=======
# DNS Server Provisioning playbook

This playbooks runs through the steps to provision a VM, set it up (subscriptions, updates, etc.), and install a DNS server on it.
Currently it is configured to provision OpenStack resources, but other providers can easily be added. 

## Example run
You will need to modify the example inventory provided in `inventory/dns-server` to fit your desired configuration, then run:

```
> ansible-playbook -i inventory/dns-server playbooks/provision-dns-server/main.yml --tags='install,all'
```

**_Note:_** The `--tags='install,all'` is important as otherwise the automation will attempt to configure the DNS server without it actually being installed. This will fail!

>>>>>>> Additional role and docs clean-up
License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
<<<<<<< HEAD
=======

>>>>>>> Additional role and docs clean-up
