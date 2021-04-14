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
      findutils \
      jq \
      ncurses \
      openssl \
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
      openssl \
      unzip && \
    dnf clean all && \
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && \
    ./get_helm.sh && \
    curl -fsSL -o kustomize.tar.gz https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv3.5.4/kustomize_v3.5.4_linux_amd64.tar.gz && \
    tar -xvf kustomize.tar.gz && \ 
    chmod 700 kustomize && \
    cp kustomize /usr/bin/ && \
    rm -rf /var/cache/yum

RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && \
    ./get_helm.sh; \
    rm -f ./get_helm.sh

COPY . ${WORK_DIR}
COPY images/infra-ansible/root /

RUN chmod 664 /etc/passwd
RUN /usr/local/bin/user_setup

USER ${USER_UID}

WORKDIR ${WORK_DIR}

ENTRYPOINT [ "/usr/local/bin/ep" ]
CMD [ "/usr/local/bin/run" ]
