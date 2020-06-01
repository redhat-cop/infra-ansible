FROM registry.redhat.io/ubi8:8.2

LABEL maintainers="Red Hat Communities of Practice" \
      usage="This image is meant to be used with the 'docker run'"

USER root

ENV OC_CLIENT_MIRROR=https://mirror.openshift.com/pub/openshift-v3/clients/3.11.115/linux/oc.tar.gz \
    USER_ID=1001 \
    APP_ROOT=/opt/app-root \
    HOME=/opt/app-root/src \
    WORK_DIR=/opt/app-root/src \
    PIP_NO_PYTHON_VERSION_WARNING=true

COPY requirements.txt install-packages .

RUN echo "enabled=0" >> /etc/yum/pluginconf.d/subscription-manager.conf && \
    yum install -y --nodocs $(<install-packages) && \
    rm /install-packages && \
    curl $OC_CLIENT_MIRROR | tar -C /usr/local/bin/ -xzf - && \
    ln -s /usr/bin/python2 /usr/bin/python && \
    ln -s /usr/bin/pip2 /usr/bin/pip && \
    pip install -r requirements.txt && \
    rm requirements.txt

COPY root /

WORKDIR ${HOME}

RUN /usr/local/bin/user_setup

USER ${USER_ID}

ENTRYPOINT ["/usr/local/bin/run"]
CMD ["sleep", "infinity"]
