config-nagios-server
====================

name: config-nagios-server
The purpose of this role is to install and configure basic Nagios server configuration. 
The role will install only if the install variable has been set and will install from source.

Requirements
------------
To install Nagios, an internet connection will be require or if no internet connection is available. 
The packages will need to be downloaded manually and added to an internal web server. 
The Nagios url variables will then need to be overwritten to reflect the new download locations.

Variables
------------------

Defaults file has example of variables that can be used. 

| Variable | Description | Required | Defaults |
|:--------:|:-----------:|:--------:|:--------:|
|**install_nagios**|  Determines if you wish to install pre req packages. | no | N/A |
|**nagios_download_dir**| Where downloads and files will be extracted | yes | /tmp |
|**nagios_version**| The version of Nagios source you wish to install | yes | 4.4.5 |
|**nagios_download_name**| The name of the Nagios download file. | yes | "nagios-{{nagios_version}}.tar.gz" |
|**nagios_download_url**| The download url of the nagios source | yes | https://github.com/NagiosEnterprises/nagioscore/archive |
|**nagios_extracted_dir**| The name of the extract directory | yes | "nagioscore-nagios-{{nagios_version}}" |
|**nagios_user**| The default username to login to nagios | yes | nagiosadmin |
|**nagios_password**| The password of the default user | yes | password |
|**nagios_epel_repo_url**| The url of the EPEL repository rpm | yes | https://dl.fedoraproject.org/pub/epel |
|**nagios_epel_repo_rpm**| Name of the Epel RPM | yes | epel-release-latest-7.noarch.rpm |
|**nagios_plugins_url**| The url of the nagios plugins source | yes | "https://github.com/nagios-plugins/nagios-plugins/archive" |
|**nagios_plugins_archive**| The archive name of the nagios plugins source. | yes | "release-2.2.1.tar.gz" |
|**nagios_plugin_version**| The version of the nagios plugins source | yes | 2.2.1 |
|**nagios_plugin_download_name**| Name of the nagios plugin download | yes | "nagios-plugins-release-{{nagios_plugin_version}}" |
|**nagios_plugins_extracted_dir**| Name of the extracted plugins directory | yes | "nagios-plugins-release-{{nagios_plugin_version}}" |
|**nagios_rhel7_optional_repo**| Name of the Red Hat Optionals repository | yes | rhel-7-server-optional-rpms |
|**rhel_packages**| List of packages that are required to be installed on a RHEL platform | yes | list in the defaults file |
|**rhel7_packages**| List of packages specific to RHEL 7 to be installed on a RHEL platform | yes | list in the defaults file |
|**epel_packages**| List of packages to be installed from EPEL repos | yes | list in defaults file |
|**nagios_services**| Used to determine how a Nagios target will be configured in Nagios. This should be configured per host. | yes | N/A |

Example Playbook
----------------

```
- name: 'Configure & Install Nagios server'
  hosts: nagios_hosts
  vars:
    install_nagios: "yes"
  roles:
    - config-nagios-server
  tags: 
    - configure_nagios_hosts
```

Example Inventory
-----------------

```
[nagios]
rhel7-nagios01 nagios_services=nothing

[nagios-targets]
rhel7-nagios01 nagios_services=nothing 
rhel7-dns01 nagios_services=dns
rhel7-dhcp01 nagios_services=dhcp

```

License
-------

Apache License 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.