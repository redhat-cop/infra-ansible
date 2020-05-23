IMAGE_NAME = infra-ansible
IMAGE_TAG = python27
cmd = bash
CONTAINER_HOME = /opt/app-root/src
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
			--interactive \
			--tty \
			--rm \
			--volume ${HOME}/.ssh:${CONTAINER_HOME}/.ssh:z \
			--volume ${GIT_HOME}:/tmp/src:z \
			--volume ${HOME}/.config/openstack/:${CONTAINER_HOME}/.config/openstack/:z \
			--volume /etc/pki/ca-trust/source/anchors/:/etc/pki/ca-trust/source/anchors/ \
			${IMAGE_NAME}:${IMAGE_TAG} ${cmd}

.PHONY: push
push:
		docker push ${IMAGE_NAME}:${IMAGE_TAG}
