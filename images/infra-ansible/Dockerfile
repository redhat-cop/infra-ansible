FROM registry.fedoraproject.org/fedora

USER root
ENV WORK_DIR /infra-ansible
ENV HOME /tmp

# Update System and install clients
RUN \
    dnf install -y --setopt=tsflags=nodocs \
      https://repos.fedorapeople.org/repos/openstack/openstack-queens/rdo-release-queens-2.noarch.rpm
RUN dnf -y install \
      ansible \
      jq \
      ncurses \
      python3-cinderclient \
      python3-glanceclient \
      python3-heatclient \
      python3-neutronclient \
      python3-novaclient \
      python3-saharaclient \
      python3-swiftclient \
      python3-troveclient \
      python3-openstackclient \
      python3-dns \
      python3-pyOpenSSL \
      python3-shade \
      python3-boto3 \
      python3-openstacksdk \
      findutils \ 
      unzip && \
    dnf clean all && \
    rm -rf /var/cache/yum

COPY . ${WORK_DIR}
COPY images/infra-ansible/root /

RUN chmod 664 /etc/passwd
RUN /usr/local/bin/user_setup

USER ${USER_UID}

WORKDIR ${WORK_DIR}

ENTRYPOINT [ "/usr/local/bin/ep" ]
CMD [ "/usr/local/bin/run" ]
