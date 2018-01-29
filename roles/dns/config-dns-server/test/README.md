# Tests for DNS server

In this directory, you will find an example inventory and test playbook to test this role. Note the following:

1. Update the inventory, in particular IPs and usernames, to match you needs
2. Currently, the test will have to be run in 2 parts (see issue https://github.com/redhat-cop/infra-ansible/issues/115 )

```
  1. > ansible-playbook -i inventory test.yml -l dns-server
  2. > ansible-playbook -i inventory test.yml -l forward-server
```

3. Add records to the configured views/zones (using nsupdate) and test that the records exist, e.g.:

```
  > dig @192.168.10.15 server.first.example.com
  > dig @192.168.10.15 server.forward.example.com
```
