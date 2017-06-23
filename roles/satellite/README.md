Satellite
=========

This role takes care of installing Red Hat Satellite.

Requirements
------------

- Host needs to be subscribed and the correct repos enabled before running this role.

Role Variables
--------------

satellite_organization: <organization name> 
satellite_location: <location of the Satellite server>
satellite_username: <admin username to be set>
satellite_password: <admin password to be set>


Example Playbook
----------------

- name: 'Configure Satellite'
  hosts: satellite_servers
  roles:
  - role: satellite


