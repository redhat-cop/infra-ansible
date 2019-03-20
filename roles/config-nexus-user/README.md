# Overview

Allows for the creation/modification of a user account in Sonatype Nexus

# Usage

Create an inventory:
```
[local]
localhost ansible_connection=local
```

Create a playbook:
```
---
# This test assumes a locally running Nexus3 app.
# The easiest way to acheive that is via `docker run -it -p 8081:8081 sonatype/nexus3

- name: 'Change admin password'
  hosts: ocp-nexus
  vars:
    nexus_api_base_path: '/service/rest/v1'
    nexus_user: admin
    nexus_password: 'admin123'
    nexus_protocol: http
    nexus_url: 'localhost:8081'
    nexus_server_poll_retries: 100
    nexus_server_poll_delay_in_seconds: 10
  tasks:
  - name: Start nexus container
    command: 'docker run -d -p 8081:8081 sonatype/nexus3'
  - name: "Ensure the Nexus Server is Up"
    uri:
      url: "{{ nexus_protocol }}://{{ nexus_url }}/service/metrics/healthcheck"
      method: GET
      status_code: 200
      user: "{{ nexus_user }}"
      password: "{{ nexus_password }}"
      force_basic_auth: yes
    register: nexus_server_check_result
    until: nexus_server_check_result is success
    retries: '{{ nexus_server_poll_retries }}'
    delay: '{{ nexus_server_poll_delay_in_seconds }}'
  - include_role: 
      name: config-nexus-user
    vars:
      nexus_user: 'admin'
      nexus_password: 'MyTestPassword'
```
