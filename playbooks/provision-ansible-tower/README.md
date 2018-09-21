# Ansible Tower Provisioning playbook

This playbooks runs through the steps to provision a VM, set it up (subscriptions, updates, etc.), and install Ansible Tower.
Currently it is configured to provision OpenStack resources, but other providers can easily be added. 

## Prerequisites
Access to an Ansible Tower source and license.

## Example run
You will need to modify the example inventory provided in `inventory/ansible-tower` to fit your desired configuration, then run:

```
> ansible-playbook -i inventory/ansible-tower playbooks/provision-ansible-tower/main.yml --tags='install,all'
```

**_Note:_** The `--tags='install,all'` is important as otherwise the automation will attempt to configure Ansible Tower without it actually being installed. This will fail!

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

