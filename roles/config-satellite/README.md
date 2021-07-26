Satellite
=========

This role takes care of installing Red Hat Satellite.

Requirements
------------

- Host needs to be subscribed and the correct repos enabled before running this role.

Role Variables
--------------

```
manifest_file_path: <path to the downloaded manifest-....zip file>
satellite_organization: <organization name>
satellite_location: <location of the Satellite server>
satellite_username: <admin username to be set>
satellite_password: <admin password to be set>

satellite_repositories: <list of dicts describing the repos to enable - see example below>

satellite_sync_plan: <name of new sync plan>

satellite_activation_keys: <dict of new keys to add, and a subscription to add to each>

```

Example Playbook
----------------

```
- name: 'Configure Satellite'
  hosts: satellite-server
  roles:
  - role: config-satellite
```

Example Inventory
----------------

```
manifest_file_path: "{{ inventory_dir }}/../files/manifest_4fcc12bd-08bc-46c6-b3e0-09dbfaece2bd.zip"

satellite_organization: "Example Org
satellite_location: "DataCenter"
satellite_username: "admin"
satellite_password: "admin01"

satellite_repositories:
- product: "Red Hat Enterprise Linux Server"
  name: "Red Hat Enterprise Linux 7 Server (RPMs)"
  release_version:
  - "7.3"
  - "7Server"
  base_arch: "x86_64"
- product: "Red Hat OpenShift Container Platform"
  name: "Red Hat OpenShift Container Platform 3.5 (RPMs)"
  release_version: []
  base_arch: "x86_64"

satellite_sync_plan: "MyPlan"

satellite_activation_keys:
  rhel-7
    subscription: "RHEL subscription"
  rhel-7-test:
    subscription: "RHEL subscription"

```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
