FROM registry.fedoraproject.org/fedora

ENV HELM_VERSION=latest \
    KUSTOMIZE_VERSION=v3.5.4

USER root
ENV WORK_DIR /infra-ansible
ENV HOME /tmp

# Update System and install clients
RUN \
    dnf install -y --setopt=tsflags=nodocs \
      https://repos.fedorapeople.org/repos/openstack/openstack-queens/rdo-release-queens-2.noarch.rpm
RUN dnf -y install \
      ansible \
      findutils \
      jq \
      ncurses \
      openssl \
      pandoc \
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
      unzip && \
    dnf clean all && \
    rm -rf /var/cache/yum

RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && \
    ./get_helm.sh; \
    rm -f ./get_helm.sh

RUN curl -fsSL -o kustomize.tar.gz https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2F${KUSTOMIZE_VERSION}/kustomize_${KUSTOMIZE_VERSION}_linux_amd64.tar.gz && \
    tar -xzf kustomize.tar.gz && \
    chmod 755 kustomize && \
    cp kustomize /usr/bin/; \
    rm -f kustomize.tar.gz

COPY . ${WORK_DIR}
COPY images/infra-ansible/root /

RUN chmod 664 /etc/passwd
RUN /usr/local/bin/user_setup

USER ${USER_UID}

WORKDIR ${WORK_DIR}

ENTRYPOINT [ "/usr/local/bin/ep" ]
CMD [ "/usr/local/bin/run" ]
