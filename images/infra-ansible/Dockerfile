FROM quay.io/openshift/origin-ansible:v3.11

USER root

ENV WORK_DIR /infra-ansible

# Update System and install clients
RUN \
    yum-config-manager --disable azure-cli; \
    yum install -y --setopt=tsflags=nodocs \
      https://repos.fedorapeople.org/repos/openstack/openstack-queens/rdo-release-queens-2.noarch.rpm \
      http://resources.ovirt.org/pub/yum-repo/ovirt-release42.rpm; \
    yum -y update ansible python-jinja2; \
    yum -y install python2-pip; \
    pip install --upgrade pip; \
    yum -y install \
      jq \
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
    rm -rf /var/cache/yum

RUN \
    rpm -e --nodeps python-ipaddress PyYAML; \
    pip install --upgrade --force-reinstall requests; \
    pip install --upgrade \
      "cryptography==2.8" \
      "openstacksdk==0.37.0"

COPY . ${WORK_DIR}
COPY images/infra-ansible/root /

RUN /usr/local/bin/user_setup

USER ${USER_UID}

WORKDIR ${WORK_DIR}

ENTRYPOINT [ "/usr/local/bin/ep" ]
CMD [ "/usr/local/bin/run" ]
