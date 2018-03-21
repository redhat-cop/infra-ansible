## The infra-ansible manage-dns-records roles


This role allows the caller to populate DNS records based on input data (see example below). The caller may choose to use hostvars to access information from other hosts (e.g.: hostname and ip address) to create records.

Both additions and removals are supported by this role, by the use of the `dns_data` variable (see example below).


Example Playbook
----------------
```yaml
  - hosts: dns-servers
    roles:
    - role: dns
      dns_records_rm:
      - view: "private"
        zone: "first.example.com"
        server: "192.168.1.100"
        key_name: "my_private_key"
        key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
        key_algorithm: "hmac-sha256"
        entries:
        - type: A
          record: server_1
          value: 192.168.1.1
      dns_records_add:
      - view: "private"
        zone: "first.example.com"
        server: "192.168.1.100"
        key_name: "my_private_key"
        key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
        key_algorithm: "hmac-sha256"
        entries:
        - type: A
          record: server_a
          value: 192.168.1.1
        - type: A
          record: server_b
          value: 192.168.1.2
      - view: "private"
        server: "192.168.1.100"
        key_name: "my_private_key"
        key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
        key_algorithm: "hmac-sha256"
        zone: "second.example.com"
        entries:
        - type: A
          record: server_x
          value: 192.168.2.1
```
