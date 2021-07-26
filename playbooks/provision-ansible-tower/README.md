# Ansible Tower Provisioning playbook

This playbooks runs through the steps to provision a VM, set it up (subscriptions, updates, etc.), and install Ansible Tower.
Currently it is configured to provision OpenStack resources, but other providers can easily be added.

## Prerequisites
Access to an Ansible Tower software and license.

One of the two:
- a set of running instance(s)
- a IaaS that allow for provisioning through these playbooks


## Example

### Inventory

Please see the **sample** inventory in the inventory area:

- [ansible-tower](../../inventory/ansible-tower)

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
