# Overview

This role uses the OpenShift command-line tool to upload a JAR based SonarQube plugin into a running SonarQube instance, then restarts that running SonarQube instance so that the plugin gets loaded.

# Usage

```yaml
- name: Install C++ Community Plugin For SonarQube
  hosts: ocp-sonarqube

  roles:
  - add-sonar-plugin
    vars:
      plugin_url: https://github.com/SonarOpenCommunity/sonar-cxx/releases/download/cxx-1.2.2/sonar-cxx-plugin-1.2.2.1653.jar
      install_location: /opt/sonarqube/extensions/plugins
      namespace: labs-ci-cd
      pod_prefix: sonarqube
```

# Testing
* Deploy a [Labs CI/CD environment](https://github.com/rht-labs/labs-ci-cd)
* Apply the role using the test playbook: `ansible-playbook -i inventory test.yml
* Verify deployment after SonarQube restarts