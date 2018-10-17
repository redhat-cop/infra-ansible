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

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
