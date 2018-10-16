## The infra-ansible manage-dns-records roles


This role allows the caller to populate DNS records based on input data. The caller may choose to use hostvars to access information from other hosts (e.g.: hostname and ip address) to create records.

Both additions and removals are supported by this role, by the use of the `dns_data` inventory variable (see example in README one level up).


Example Playbook
----------------
```yaml
  - hosts: dns-servers
    roles:
    - role: dns
```
