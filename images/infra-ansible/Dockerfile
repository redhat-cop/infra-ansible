FROM registry.redhat.io/ubi8:8.2

LABEL MAINTAINTERS="Red Hat Services"

USER root

ENV OC_CLIENT_MIRROR=https://mirror.openshift.com/pub/openshift-v3/clients/3.11.115/linux/oc.tar.gz \
    USER_ID=1001 \
    APP_ROOT=/opt/app-root \
    HOME=/opt/app-root/src \
    WORK_DIR=/opt/app-root/src \
    INSTALL_PKGS=" \
      gcc \
      git \
      java-1.8.0-openjdk-headless \
      httpd-tools \
      iproute \
      openssl \
      python2-devel \
      python2-pip \
      python2-setuptools \
      vim"

RUN yum install -y --nodocs ${INSTALL_PKGS} && \
    curl $OC_CLIENT_MIRROR | tar -C /usr/local/bin/ -xzf - && \
    ln -s /usr/bin/python2 /usr/bin/python && \
    ln -s /usr/bin/pip2 /usr/bin/pip

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY root /

WORKDIR ${HOME}

RUN /usr/local/bin/user_setup

USER ${USER_ID}

ENTRYPOINT ["/usr/local/bin/run"]
CMD ["sleep", "infinity"]
