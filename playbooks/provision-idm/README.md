# IdM Provisioning playbook

This playbooks runs through the steps to provision a VM, set it up, configure DNS records, and install IdM.
Currently it is configured to provision OpenStack resources, but other providers can easily be added. 


## Prerequisites
You must have a working DNS server which accepts "nsupdate" connections for the IdM VMs forward and reverse DNS records to be added/updated to the existing DNS zones. You will need the DNS zone key names, key secrets, and key algorithms.

## Example run
You will need to modify the example inventory provided in `inventory/idm` to fit your desired configuration, including information from your DNS server such as the key names, secrets, and more. 

```
> ansible-playbook -i inventory/idm playbooks/provision-idm/idm.yml
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

