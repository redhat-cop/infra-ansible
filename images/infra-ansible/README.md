### infra-ansible container image specs

potential base images:

ubi8/python-38
ubi8/python-36
ubi8/minimal
ubi7/python-36

pypi packages:

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
- python3-devel

