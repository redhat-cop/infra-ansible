wait-for-objects-via-exec
========================

This role is used to hold processing until specific OpenShift objects gets in specified state, either using oc or kubectl. Role is expected to be run on Ansible Host running within OpenShift cluster, that's a target for object action

## Requirements

  - Ansible Host running within targetted OpenShift cluster
  - OC or kubectl installed on Ansible Host

## Role Variables


| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|openshift_wait_for_objects.name|Name of OpenShift object to be removed|yes||
|openshift_wait_for_objects.kind|Kind of object to be used|yes||
|openshift_wait_for_objects.executable|Name of executable to be used for operation(oc/kubectl)|yes||
|openshift_wait_for_objects.namespace|OpenShift Namespace in which object to be removed resides|yes||
|openshift_wait_for_objects.state|Target state for the object|yes||
|openshift_wait_for_objects.timeout| Timeout |yes||


## Example Inventory

```yaml
---
openshift_wait_for_objects:
   - name: argo-app-abc
     executable: oc
     kind: Application
     namespace: argocd-apps
     state: 'condition=Ready'
     timeout: 300
```

## Example Playbook

```yaml
---

- hosts: openshift-api
  roles:
  - role: wait-for-objects-via-api
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
