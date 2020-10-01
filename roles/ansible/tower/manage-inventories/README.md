manage-inventories
==================

This role manages inventories for Ansible Tower, to be used with Ansible Tower runs.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used must be defined in the Ansible Inventory using the `ansible_tower.inventories` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.inventories.name|Name of the inventory|yes||
|ansible_tower.inventories.description|Description of the inventory|no|nothing ('')|
|ansible_tower.inventories.organization|Organization to associate the inventory with|yes||
|ansible_tower.inventories.variables|"all" variables for inventory|no||
|ansible_tower.inventories.hosts|List of host vars (see below)|no||
|ansible_tower.inventories.groups|List of group vars (see below)|no||
|ansible_tower.inventories.sources|List of sources (see below)|no||

**_Note:_** Inventories configuration will **only** happen if the `ansible_tower.inventories` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.


### Hosts

The list of hosts as mentioned in the above inventories configuration is used to associate host specific inventory variables. More info about host_vars can be found [here](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#host-variables). This list is defined as:


```yaml
ansible_tower:
  inventories:
  - name: test1
    hosts:
    - name: "localhost"
      variables: |-
        ---
        ansible_connection: local
    - name: "remote1"
      variables: |-
        ---
        ansible_user: username
  - name: test2
    hosts:
    - name: "localhost"
      variables: |-
        ---
        ansible_connection: local
    - name: "remote2"
      variables: |-
        ---
        ansible_user: username
```

### Groups

The list of groups as mentioned in the above inventories configuration is used to associate group specific inventory variables. More info about group_vars can be found [here](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#group-variables). This list is defined as:


```yaml
ansible_tower:
  inventories:
  - name: test1
    groups:
    - name: "my-test1-group1"
      variables: |-
        ---
        foo1: bar1
        foo2: bar2
      hosts:
      - name: "localhost"
    - name: "my-test1-group2"
      variables: |-
        ---
        foo3: bar3
        foo4: bar4
      hosts:
      - name: "host1"
  - name: test2
    groups:
    - name: "my-test2-group1"
      variables: |-
        ---
        foo5: bar5
        foo6: bar6
      hosts:
      - name: "host2"
    - name: "my-test2-group2"
      variables: |-
        ---
        foo7: bar7
        foo8: bar8
      hosts:
      - name: "host3"
```

### Sources
The list of sources as mentioned above is used to import inventory variables from a variety of locations. More info about this can be found [here](https://docs.ansible.com/ansible-tower/latest/html/administration/scm-inv-source.html). For example this can be used to source dynamic inventories from remote locations. Currently, only scm as a source is supported. The list is defined as:

```yaml
ansible_tower:
  inventories:
    - name: test1
      variables: ""
      hosts:
      - name: "localhost"
        variables: |-
          ---
          ansible_connection: local
      organization: "Default"
      groups:
      - name: "my-test1-group1"
        variables: ""
        hosts:
        - name: "localhost"
      sources:
      - name: "test-source1"
        description: "Test Source 1"
        credential: "Test Credential"
        source: "scm"
        source_project: "test-project1"
        source_path: "scripts/test-script1.py"
        source_vars: |-
          ---
          FOO: foo
          BAR: bar
          BAZ: baz
        overwrite: false
        overwrite_vars: false
        update_on_launch: true
        update_on_project_update: false
      - name: "test-source2"
        description: "Test Source 2"
        credential: "Test Credential"
        source: "scm"
        source_project: "test-project2"
        source_path: "scripts/test-script2.py"
        source_vars: ""
```


## Example Inventory

```yaml
---

ansible_tower:
  admin_password: "admin01"
  inventories:
  - name: "Inventory1"
    description: "My Hosts"
    organization: "Default"
    variables: "---"
    hosts:
    - name: "localhost"
      description: ""
      variables: |-
        ---
        ansible_connection: local
    groups:
    - name: "seed_hosts"
      variables: |-
        ---
        foo: bar
      hosts:
      - name: "localhost"
    sources:
    - name: "source1"
      description: "Source 1"
      credential: "Credential"
      source: "scm"
      source_project: "project1"
      source_path: "scripts/script1.py"
      source_vars: |-
        ---
        FIRST: John
        LAST: Doe
      overwrite: false
      overwrite_vars: false
      update_on_launch: true
      update_on_project_update: false
```


## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: manage-inventories
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
