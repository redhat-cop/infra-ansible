FROM quay.io/openshift/origin-ansible:v3.11

USER root

# Update System and install clients
RUN \
    yum-config-manager --disable azure-cli; \
    yum install -y --setopt=tsflags=nodocs \
      https://repos.fedorapeople.org/repos/openstack/openstack-queens/rdo-release-queens-2.noarch.rpm \
      http://resources.ovirt.org/pub/yum-repo/ovirt-release42.rpm; \
    yum -y install python2-pip; \
    pip install --upgrade pip; \
    yum -y install \
      python-ovirt-engine-sdk4 \
      python-ceilometerclient \
      python-cinderclient python-glanceclient \
      python-heatclient python-neutronclient \
      python-novaclient python-saharaclient \
      python-swiftclient python-troveclient \
      python-openstackclient python-dns \
      python2-pyOpenSSL python-shade \
      python-boto3 \
      python-openstacksdk; \
    yum clean all; \
    rm -rf /var/cache/yum; \
    pip install --upgrade --force-reinstall requests

COPY images/infra-ansible/root /

RUN /usr/local/bin/user_setup

USER ${USER_UID}

ENTRYPOINT [ "/usr/local/bin/entrypoint" ]
CMD [ "/usr/local/bin/run" ]
