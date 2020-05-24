IMAGE_NAME = infra-ansible
IMAGE_TAG = 1.0.15
cmd = bash
CONTAINER_HOME = /opt/app-root/src
GIT_HOME = ${HOME}/src
UID != id -u
GID != id -g

.PHONY: build
build:
		podman build --network host -t ${IMAGE_NAME}:${IMAGE_TAG} .

.PHONY: build-toolbox
build-toolbox:
		podman build --network host -t ${IMAGE_NAME}-toolbox:${IMAGE_TAG} -f Containerfile .

.PHONY: create-toolbox
create-toolbox:
		toolbox create -i ${IMAGE_NAME}-toolbox:${IMAGE_TAG} -c ${IMAGE_NAME}-toolbox

.PHONY: enter-toolbox
enter-toolbox:
		toolbox enter --container infra-ansible-toolbox

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
