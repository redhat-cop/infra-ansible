IMAGE_NAME = localhost/infra-ansible
IMAGE_TAG = python27

.PHONY: build
build:
		podman build -t ${IMAGE_NAME}:${IMAGE_TAG} .

.PHONY: test
test:
		podman build -t ${IMAGE_NAME}-candidate:${IMAGE_TAG} .
		IMAGE_NAME=${IMAGE_NAME}-candidate:${IMAGE_TAG} test/run

.PHONY: push
push:
		podman push ${IMAGE_NAME}:${IMAGE_TAG}
