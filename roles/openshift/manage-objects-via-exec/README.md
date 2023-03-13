manage-openshift-object-via-exec
========================

This role is used to manage OpenShift object with a help of oc or kubectl. Role is expected to be run on Ansible Host running within OpenShift cluster, that's a target for object action

## Requirements

  - Ansible Host running within targetted OpenShift cluster
  - OC or kubectl installed on Ansible Host

## Role Variables


| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|openshift_manage_objects.name|Name of OpenShift object to be removed|yes||
|openshift_manage_objects.kind|Kind of object to be removed|yes||
|openshift_manage_objects.executable|Name of executable to be used for operation(oc/kubectl)|yes||
|openshift_manage_objects.namespace|OpenShift Namespace in which object to be removed resides|yes||
|openshift_manage_objects.api_version|API version used for object|yes||
|openshift_manage_objects.action| OC/Kubectl action to be executed on specified object|yes||  


## Example Inventory

```yaml
---
openshift_manage_objects:
   - name: argo-app-abc
     executable: oc
     kind: Application
     namespace: argocd-apps
     api_version: argoproj.io/v1alpha1
     action: delete
```

## Example Playbook

```yaml
---

- hosts: openshift-api
  roles:
  - role: manage-openshift-objects-via-exec
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
