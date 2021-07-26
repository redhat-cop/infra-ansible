Manage AWS Security Groups Role
===============================

An ansible role that allows you to manage existing or new AWS Security Groups

Requirements
------------

Python > 2.6
boto3, botocore packages

Role Variables
--------------

## AWS Security Groups

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**aws_security_groups.vpc_name**| Name of the VPC that you want to deploy your security group in  | yes | N/A |
|**aws_security_groups.name**| Name of security group  | yes | N/A |
|**aws_security_groups.state**| Whether the security group should exist or not  | no | present |
|**aws_security_groups.description**| Description of your security group | yes | N/A |
|**aws_security_groups.purge_incoming_rules**| Whether to purge ingress rules not found in your rules list  | no | true |
|**aws_security_groups.purge_outgoing_rules**| Whether to purge egress rules not found in your rules list | no | true |
|**aws_security_groups.purge_tags**| Whether or not to remove tags that are not in the tag list  | no | true |
|**aws_security_groups.incoming_rules**| List of inbound rules to include in your security group| yes | N/A |
|**aws_security_groups.outgoing_rules**| List of outbound rules to include in your security group| yes | N/A |
|**aws_security_groups.tags**| Dictionary of tags to apply to your security group | no | N/A |

Example Playbook
----------------

```
- hosts: aws-provisioner
  roles:
  - aws/manage-security-groups
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

