FROM registry.redhat.io/ubi8-minimal:8.2

LABEL MAINTAINTERS="Red Hat Services"

USER root

ENV OC_CLIENT_MIRROR=https://mirror.openshift.com/pub/openshift-v3/clients/3.11.115/linux/oc.tar.gz \
    USER_ID=1001 \
    APP_ROOT=/opt/app-root \
    HOME=/opt/app-root/src \
    INSTALL_PKGS=" \
      vim \
      git \
      tar \
      gzip \
      httpd-tools \
      python2-devel \
      python2-pip \
      python2-setuptools \
      python3-devel \
      python3-pip \
      python3-setuptools \
      gcc"

RUN microdnf install --nodocs ${INSTALL_PKGS} && \
    curl $OC_CLIENT_MIRROR | tar -C /usr/local/bin/ -xzf - && \
    ln -s /usr/bin/python2 /usr/bin/python && \
    ln -s /usr/bin/pip2 /usr/bin/pip

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY root /

RUN /usr/local/bin/user_setup

USER ${USER_ID}

WORKDIR ${HOME}
ENTRYPOINT ["/usr/local/bin/run"]
CMD ["sleep", "infinity"]
