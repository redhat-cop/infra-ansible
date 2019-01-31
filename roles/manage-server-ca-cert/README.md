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



Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
