manage-objects-via-api
========================

This role is used to manage OpenShift objects via OpenShift API. Role is expected to be run on Ansible Host running within OpenShift cluster, that's a target for object management

## Requirements

  - Ansible Host running within targetted OpenShift cluster


## Role Variables


| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|openshift_manage_objects.name|Name of OpenShift object to be processed|yes||
|openshift_manage_objects.kind|Kind of object to be processed|yes||
|openshift_manage_objects.namespace|OpenShift Namespace in which object to be processed resides|yes||
|openshift_manage_objects.api_version|API version used for object|yes||
|openshift_manage_objects.state|Desired state of OpenShift object|no|"present"|


## Example Inventory

```yaml
---
openshift_manage_objects:
   - name: argo-app-abc
     kind: Application
     namespace: argocd-apps
     api_version: argoproj.io/v1alpha1
     state: absent
```

## Example Playbook

```yaml
---

- hosts: openshift-api
  roles:
  - role: manage-openshift-objects-via-api
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
