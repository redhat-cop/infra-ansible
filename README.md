== The rhc-ose ansible dns role


This role allows the caller to populate DNS records (currently only supports A records) based on input data (see example below). The caller may choose to use hostvars to access information from other hosts (e.g.: hostname and ip address) to create records. 

Both additions and removals are supported by this role, by the use of the "dns_records_rm" and "dns_records_add" variables (see example below).

> NOTE: removal of records is done before additions


Example Playbook
----------------

  - hosts: dns-servers
    roles:
    - role: dns
      dns_records_rm:
      - view: "private"
        zone: "first.example.com"
        entries:
        - type: A
          hostname: server_1
          ip: 192.168.1.1
      dns_records_add:
      - view: "private"
        zone: "first.example.com"
        entries:
        - type: A
          hostname: server_a
          ip: 192.168.1.1
        - type: A
          hostname: server_b
          ip: 192.168.1.2
      - view: "private"
        zone: "second.example.com"
        entries:
        - type: A
          hostname: server_x
          ip: 192.168.2.1

