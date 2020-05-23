IMAGE_NAME = infra-ansible
IMAGE_TAG = python27
cmd = bash
CONTAINTER_HOME = /opt/app-root/src
GIT_HOME = ${HOME}/src
UID != id -u
GID != id -g

.PHONY: build
build:
		podman build --network host -t ${IMAGE_NAME}:${IMAGE_TAG} .

.PHONY: run
run:
		podman run \
			--userns=keep-id \
			--network host \
			--volume ${HOME}/.ssh:${CONTAINTER_HOME}/.ssh:z \
			--volume ${GIT_HOME}:/tmp/src:z \
			--volume ${HOME}/.config/openstack/:${CONTAINER_HOME}/.config/openstack/:z \
			--volume /etc/pki/ca-trust/source/anchors/:/etc/pki/ca-trust/source/anchors/ \
			--interactive \
			--tty \
			${IMAGE_NAME}:${IMAGE_TAG} ${cmd}

.PHONY: push
push:
		docker push ${IMAGE_NAME}:${IMAGE_TAG}
