manage-server-ca-cert
=====================

Role used to copy CA certificates to a target server and make them trusted

Requirements
------------

A Red Hat based Linux OS (RHEL, CentOS, Fedora)

Role Variables
--------------

| Variable | Description | Required | Defaults | Notes |
|:--------:|:-----------:|:--------:|:--------:|:-----:|
|**list_of_additional_ca_certs**|List of CA certificates to be installed|no|(empty list)|**Note:** if no certs are provided, the role will not do anything - useful if the role is part of a bigger playbook|
|**server_ca_location**|Location to copy the CAs to on the target server|no|/etc/pki/ca-trust/source/anchors/||


**Note:** `list_of_additional_ca_certs` is currently a list of local files, but this could be enhanced in the future to support URLs and actual cert content as well. 


Example Playbook
----------------

    - hosts: all
      roles:
         - role: manage-server-ca-cert

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
