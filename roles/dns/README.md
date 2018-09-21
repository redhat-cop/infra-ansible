Set of Roles
============

The ansible roles found in this directory has to do with managing DNS infrastructure.

Requirements
------------

1. For named/bind install/configuration:  
  1. Root level access to a running Linux flavor (Fedora, CentOS, Red Hat Enterprise Linux)
1. For DNS zones and records, one or more of the following:
  1. Access to nsupdate enabled infrastructure (i.e.: above mentioned bind).
  1. Access to AWS Route53 with DNS admin access enabled.


Role Variables
--------------

See `Example Inventory` below for more specific details. The following variable needs to be defined:

- `dns_data`: A dictionary with DNS data (views, zones, records)



Example Playbooks
----------------

```
- hosts: new-dns-servers
  roles:
  - role: cofig-dns-server
  - role: manage-dns-zones
  - role: manage-dns-records
```

```
- hosts: existing-nsupdate-servers
  roles:
  - role: manage-dns-records
```

```
- hosts: route53-servers
  roles:
  - role: manage-dns-zones
  - role: manage-dns-records
```



Example Inventory
----------------

**_Note:_** The values below that have a "Default: " notation are optional config values

```
print_dns_keys: True

dns_data:
  named_global_config:
    recursion: 'no'               # Default: 'yes'
    dnssec_enable: 'yes'          # Default: 'no'
    dnssec_validation: 'yes'      # Default: 'no'
    dnssec_lookaside: 'no'        # Default: 'auto'
    allow_query:                  # Default: 'any'
    - 192.168.20.0/32
    - 192.168.30.0/24
    allow_transfer:               # Default: 'any'
    - 192.168.10.11/32
    - 192.168.10.12/32
  views:
  - name: private
    named:
      recursion: 'yes'
      acl_entry:
      - 192.168.10.0/24
    default_forwarders:
    - 8.8.8.8
    zones:
    - dns_domain: first.example.com
      state: present
      named: True
      route53:
        aws_access_key: "ADFGIASDF343FMSDFF5431A"
        aws_secret_key: "EqFDGSDFGEWwergdsg4315L679DsA065wU+X1mPRtRLQ4Hve"
        vpc_id: vpc-9dcde6f8
        vpc_region: eu-west-1
      nsupdate:
      - server: "192.168.48.26"
        key_name: "private-first.example.com"
        key_secret: "EhZfRtlHgy7xTIi2LeVSGsBj99Sb8IGB6K30ovg13dE="
        key_algorithm: "hmac-sha256"
      entries:
      - type: A
        record: master
        value: 172.16.10.20
        ttl: 60
        state: present
      - type: A
        record: node1
        value: 172.16.10.21
        ttl: 60
        state: present
    - dns_domain: second.example.com
      state: present
      nsupdate:
      - server: "192.168.48.26"
        key_name: "private-second.example.com"
        key_secret: "+UYdpSzdQyZ20V9/2Ud9RjHFz9Pouqn4aXP3V9X/gq4="
        key_algorithm: "hmac-sha256"
      entries:
      - type: A
        record: master
        value: 172.17.9.20
        state: absent
      - type: A
        record: master
        value: 172.17.10.20
        state: present
      - type: A
        record: node1
        value: 172.17.10.20
        state: present
    - dns_domain: third.example.com
      state: present
      named: True
      type: forward
      forwarders:
      - 192.168.48.27
  - name: public
    zones:
    - dns_domain: first.example.com
      route53:
        aws_access_key: "ADFGIASDF343FMSDFF5431A"
        aws_secret_key: "EqFDGSDFGEWwergdsg4315L679DsA065wU+X1mPRtRLQ4Hve"
      entries:
      - type: A
        record: master
        value: 10.9.10.20
        state: present
      - type: A
        record: node1
        value: 10.9.10.21
        state: present
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
