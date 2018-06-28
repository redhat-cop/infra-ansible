# IdM Provisioning playbook

This playbooks runs through the steps to provision a VM, set it up, configure DNS records, and install IdM.
Currently it is configured to provision OpenStack resources, but other providers can easily be added. 


## Prerequisites
You must have a working DNS server which will be able to access your IdM VM in order to setup forward and reverse DNS records. You will need the DNS zone key names, key secrets, and key algorithms. If you used the provision-dns-server playbook in [infra-ansible](https://github.com/redhat-cop/infra-ansible/tree/master/playbooks/provision-dns-server), there is a print_dns_key flag you can pass to have it print out these values.

## Example run
You will need to modify the example inventory provided in `inventory/idm` to fit your desired configuration, including information from your DNS server such as the key names, secrets, and more. 

```
> ansible-playbook -i inventory/idm playbooks/provision-idm/idm.yml
```

