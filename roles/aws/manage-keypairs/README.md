Manage AWS Keypairs Role
========================

An ansible role that allows you to manage existing or new AWS keypairs 

Requirements
------------

Python > 2.6
boto3, botocore packages

Role Variables
--------------

## restrictions

There are two scenarios in which this role can be used for. The first is providing an already created keys public key for upload to the keypair which you are creating. The second is for a newly created keypair, which you will then receive the private key for.

In scenario one, you will only want to private a name and public_key for an item. For the second scenario, you will want to provide a name, key_location and (optionally) a key_name.


## aws_keypairs

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**aws_keypairs.name**| Name of keypair to create | yes | N/A |
|**aws_keypairs.public_key**| Value of the public key to populate the keypair with | no | N/A |
|**aws_keypairs.key_location**| Path to the location you would like to save your key at. | no |N/A|
|**aws_keypairs.key_name**| Name of the file that your private key will be saved to | no | N/A |

Example Playbook
----------------

```
- hosts: aws-provisioner
  roles:
  - aws/manage-keypairs
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
