Manage AWS Networks Role
=========

An ansible role that allows you to manage existing or new AWS Virtual Private Clouds (VPCs) and subnets

Requirements
------------

Python > 2.6
boto3, botocore packages

Role Variables
--------------

## AWS Networks 

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**aws_networks.name**| Name of VPC to create | yes | N/A |
|**aws_networks.cidr_blocks**| List of CIDR blocks. The first CIDR provided will be used as the primary. | yes | N/A |
|**aws_networks.tags**| Dict of tags that you want applied to the resource.|no|N/A|
|**aws_networks.region**| AWS region to deploy VPC in | yes | N/A |
|**aws_networks.enable_dns_hostnames**| Whether to enable hostname support | no | true |
|**aws_networks.enable_dns_support**| Whether to enable dns support | no | true |
|**aws_networks.enable_multi**| Whether to allow for duplicate VPC's to be created | no | false |
|**aws_networks.purge_cidrs**| Remove CIDRS that are associated with the VPC but not specified in aws_networks.cidr_blocks. | no | false |
|**aws_networks.state**| Whether the network should exist or not | no | present |

## AWS Subnets

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**aws_subnets.region**|  AWS region to deploy subnet in| yes | N/A |
|**aws_subnets.vpc_name**| Name of the VPC that you want to deploy your subnet in  | yes | N/A |
|**aws_subnets.name**| Name/Description of subnet  | yes | N/A |
|**aws_subnets.state**| Whether the subnet should exist or not  | no | present |
|**aws_subnets.cidr_block**| CIDR block that you would like to use for the subnet | yes | N/A |
|**aws_subnets.availability_zone**| Availability zone to place the subnet in  | no | N/A |
|**aws_subnets.enable_public_ip**| Whether instances launched into this subnet should get a public IP by default | no | false |
|**aws_subnets.tags**| Dict of tags that you want applied to the resource  | no | N/A |
|**aws_subnets.purge_tags**| Whether or not to remove tags that are not in the tag list  | no | true |

Example Playbook
----------------

```
- hosts: aws-provisioner
  roles:
  - aws/manage-networks
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
