# NFS Server playbook

This playbook is for provisioning a server to host NFS shares.

## Example run

```
> ansible-playbook -i inventory/provision-nfs-server/ playbooks/provision-nfs-server/main.yml --tags='install'
```

## Inventory Options

| variable | info |
|:--------:|:----:|
|nfs-shares|List of nfs shares to create, more details at [nfs-server role](https://github.com/redhat-cop/infra-ansible/tree/master/roles/nfs-server)|
|nfs_storage_device|The storage device where the nfs shares will be running.|
|rhsm_username|Subscription manager username|
|rhsm_password|Subscription manager password|
|rhsm_pool|The pool id to register the server with|


