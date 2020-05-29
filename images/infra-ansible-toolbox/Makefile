IMAGE_NAME = infra-ansible-toolbox
IMAGE_TAG != git describe --tags `git rev-list --tags --max-count=1`

.PHONY: build
build:
		podman build --network host -t ${IMAGE_NAME}:${IMAGE_TAG} -f Containerfile .

.PHONY: create
create:
		toolbox create --image ${IMAGE_NAME}:${IMAGE_TAG} --container ${IMAGE_NAME}

.PHONY: enter
enter:
		toolbox enter --container ${IMAGE_NAME}

.PHONY: push
push:
		podman push ${IMAGE_NAME}:${IMAGE_TAG}

.PHONY: reset
reset:
		podman kill ${IMAGE_NAME};
		toolbox rm ${IMAGE_NAME}

