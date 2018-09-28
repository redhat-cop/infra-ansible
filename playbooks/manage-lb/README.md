# Load Balancer Playbook

This playbook directory has the playbook(s) necessary to manage your load balancers.

## Prerequisites

Currently, the playbook(s) in here don't manage the instances themselves, so you need to ensure you already have running instances (and subscribed if applicable) before running these playbook(s) with a valid inventory.

## Example

### Inventory

Please see the inventory in the respective role for more details:

- [manage-haproxy](../../roles/load-balancers/manage-haproxy/README.md)


### Playbook execution

Initial run needs the `tags='install'` set to ensure all necessary software is installed:

```bash
> ansible-playbook -i inventory lb-vms.yml --tags='install'
```

Any consecutive runs can be done without the 'install' tag to speed up execution:
```bash
> ansible-playbook -i inventory lb-vms.yml
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

