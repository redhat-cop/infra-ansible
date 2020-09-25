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
|**aws_keypairs.region**| The AWS region to use | no | null |
|**aws_keypairs.state**| Create or delete keypair | no | present |

>**NOTE:** This role expects your AWS credentials to be provided as either `aws_key` and `aws_secret` variables or as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables. Unless the region variable is set in your inventory, the `aws_region` variable will also have to be provided.

Example Playbook
----------------

```
- hosts: aws-provisioner
  roles:
  - aws/manage-keypairs
```
Example Inventory
-----------------
```
---
ec2_key_name: ec2-example-key-1
ec2_public_key: |
  ssh-rsa AAAAB3NzaC1....
aws_keypairs:
  - name: "{{ ec2_key_name }}"
    public_key: "{{ ec2_public_key }}"
    region: ap-northeast-1
  - name: "{{ ec2_key_name }}"
    key_location: /tmp
    key_name: ec2-example-key-2
    region: ap-northeast-2
  - name: "{{ ec2_key_name }}"
    public_key: "{{ ec2_public_key }}"
    region: us-east-2
    state: absent
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
