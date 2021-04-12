manage-organizations
===============

This role manages Organizations for Ansible Tower, to be used with Ansible Tower runs.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

Check the top level [README](../README.md) for additional/common variables.

The variables used must be defined in the Ansible Inventory using the `ansible_tower.organizations` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.organizations.name|Name of the organization|yes||
|ansible_tower.organizations.description|Description of the organization|no||
|ansible_tower.organizations.rrule|Add a recurrence rule, AKA RRULE|yes||
|ansible_tower.organizations.enabled|enable/disable your organization|no|yes|
|ansible_tower.organizations.unified_job_template|Name of template to run, which will translate to an integer ID|yes||


**_Note:_** Organization configuration will **only** happen if the `ansible_tower.organizations` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.


## Example Inventory

```yaml
---

ansible_tower:
  admin_password: "admin01"
  organizations:
  - name: "Demo Organization"
    description: "My Organization runs My Job Template on a Recurrency Rule timer running at 2020-12-22 at 11 a.m US/Eastern"
    rrule: "DTSTART;TZID=US-Eastern:20201222T110000Z RRULE:FREQ=WEEKLY;INTERVAL=1;COUNT=1"
    unified_job_template: "Demo Job Template"


ansible_tower:
  admin_password: "admin01"
  organizations:
  - name: "My Organization"
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: manage-organizations
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
