### infra-ansible container image specs

base image:

ubi8/minimal

general list of python packages required to run infra-ansible:

```
ansible
boto
boto3
botocore
Paste
eventlet
openstacksdk
python-ceilometerclient
python-cinderclient
python-glanceclient
python-heatclient
python-keystoneclient
python-mistralclient
python-neutronclient
python-novaclient
python-openstackclient
python-swiftclient
python-troveclient
passlib
shade
selinux
```

Other packages:

- httpd-tools (htpasswd)
