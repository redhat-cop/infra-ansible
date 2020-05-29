# Red Hat Single Sign-On playbook

This playbooks runs through the steps to provision a VM, set it up, install Red Hat Single Sign-On in Standalone Mode, create a default console management user, and deploy a sample Realm.
This playbook is currently configured to provision OpenStack resources.


## Prerequisites

For hosting infrastructure, you will need one of the two:
- a set of running instance(s)
- a IaaS that allow for provisioning through these playbooks

You must have a valid Red Hat Subscription in order to be able to activate the necessary repositories that contain the required packages.

## Example

### Inventory

Please see the **sample** inventory in the inventory area:

- [rh-sso](../../inventory/rh-sso)


You will need to modify this sample inventory to fit your desired configuration, including information from your Red Hat Subscription and the default management user credentials.


### Playbook execution

Depending on how this is being hosted, the initial may need the `tags='install'` set to ensure all necessary software is installed:

```bash
> ansible-playbook -i inventory main.yml --tags='install'
```

Any consecutive runs can be done without the 'install' tag to speed up execution:
```bash
> ansible-playbook -i inventory main.yml
```
