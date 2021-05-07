launch-tower-jobs
===============

This role launches jobs for Ansible Tower after all other configuration has completed

## Requirements

A running Ansible Tower with admin permission level access.

## Role Variables

Check the top level [README](../README.md) for additional/common variables.

The variables used must be defined in the Ansible Inventory using the `ansible_tower.launch_jobs` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.launch_jobs.job_template|Name of the job template|yes||
|ansible_tower.launch_jobs.extra_vars|extra_vars can be added if prompt on launch is enabled on the job template|no||
|ansible_tower.launch_jobs.job_type|Job type can be run or check if prompt on launch is enabled on the job template|no|Run|
|ansible_tower.launch_jobs.inventory|Inventory can be specificed if prompt on launch is enabled on the job template|no||
|ansible_tower.launch_jobs.wait|Wait for job to complete before moving on to the next job|no|false|
|ansible_tower.launch_jobs.timeout|Timeout for requests from tower API|no|30|
|ansible_tower.launch_jobs.retries|If wait is enabled, number of retries|no|10|
|ansible_tower.launch_jobs.delay|If wait is enabled, delay between retries|no|6|
|ansible_tower.launch_jobs.tags|Tags to use from the job template playbook|no|all|
|ansible_tower.launch_jobs.skip_tags|Tags to skip from the job template playbook|no|none|
|ansible_tower.launch_jobs.inventory_limit_pattern|Pattern of hosts to limit|no|none|
|ansible_tower.launch_jobs.scm_branch|If branch override is enabled, specify a different branch to run|no|defined by job template|
|ansible_tower.launch_jobs.verbosity|Change the verbosity for the job run from 0 (least) to 5 (most)|no|1|
|ansible_tower.launch_jobs.workflow_job_template|Set if workflow_job_template|no|false|

## Example Inventory

ansible_tower:
  launch_jobs:
    - name: Launch a job with inventory and credential and wait 30 seconds for job to complete
      job_template: "My Job Template"
      inventory: "My Inventory"
      credential: "My Credential"
      wait: true
      retries: 5
      delay: 6
    - name: Launch a workflow job template
      job_template: "My Workflow Job Template"
      workflow_job_template: true

