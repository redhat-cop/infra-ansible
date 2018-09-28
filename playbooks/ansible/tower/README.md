# Ansible Tower Playbooks

This playbook directory has the playbook(s) necessary to manage your Ansible Tower.

## Prerequisites

Currently, the playbook(s) in here do not manage the instances (a.k.a.: VMs) themselves, so you need to ensure you already have running instances (and subscribed if applicable) before running these playbook(s) with a valid inventory.

## Example

### Inventory

Please see the inventory in the respective role for more details:

- [tower](../../../roles/ansible/tower/README.md)


### Playbook execution

Initial run needs the `tags='install,all'` set to ensure all necessary software is installed:

```bash
> ansible-playbook -i inventory configure-ansible-tower.yml --tags='install,all'
```

Any consecutive runs can be done without the tags to speed up execution:
```bash
> ansible-playbook -i inventory configure-ansible-tower.yml
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
