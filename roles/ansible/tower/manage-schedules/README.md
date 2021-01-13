manage-schedules
===============

This role manages Schedules for Ansible Tower, to be used with Ansible Tower runs.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used must be defined in the Ansible Inventory using the `ansible_tower.schedules` list as explained below.


| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.schedules.name|Name of the schedule|yes||
|ansible_tower.schedules.description|Description of the schedule|no||
|ansible_tower.schedules.rrule|Add a recurrence rule, AKA RRULE|yes||
|ansible_tower.schedules.enabled|enable/disable your schedule|no|yes|
|ansible_tower.schedules.unified_job_template|Name of template to run, which will translate to an integer ID|yes||


**_Note:_** Schedule configuration will **only** happen if the `ansible_tower.schedules` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.


## Example Inventory

```yaml
---

ansible_tower:
  admin_password: "admin01"
  schedules:
  - name: "Demo Schedule"
    description: "My Schedule runs My Job Template on a Recurrency Rule timer running at 2020-12-22 at 11 a.m US/Eastern"
    rrule: "DTSTART;TZID=US-Eastern:20201222T110000Z RRULE:FREQ=WEEKLY;INTERVAL=1;COUNT=1"
    unified_job_template: "Demo Job Template"


ansible_tower:
  admin_password: "admin01"
  schedules:
  - name: "My Schedule"
```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: manage-schedules
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
