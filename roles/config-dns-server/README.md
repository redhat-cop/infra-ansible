# The rhc-ose ansible dns-server role


This role installs and configures bind/named for use with multiple views and zones. 


## Example Playbook

```

  - hosts: dns-servers
    roles:
    - role: dns-server
      named_config_recursion: 'no'
      named_config_dnssec_enable: 'no'
      named_config_dnssec_validation: 'no'
      named_config_dnssec_lookaside: 'auto'
      named_config_allow_transfer:
      - "192.168.10.11"
      - "192.168.10.12"
      named_config_views:
      - name: "private"
        acl_entry: 
        - "172.16.0.0/16"
        - "172.17.0.0/16"
        zone:
        - dns_domain: first.example.com
        - dns_domain: second.example.com
        - dns_domain: forward.example.com
          type: forward
          forwarders:
          - 192.168.10.11
          - 192.168.10.12
      - name: "public"
        zone:
        - dns_domain: first.example.com
        - dns_domain: second.example.com
        default_forwarders:
        - 8.8.8.8
        - 8.8.4.4
```
