IMAGE_NAME = infra-ansible
IMAGE_TAG = python27

.PHONY: build
build:
		docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .

.PHONE: run
run:
		docker run -u `id -u` \
			-v ${HOME}/.ssh/:/opt/app-root/src/.ssh:z \
			-v ${HOME}/src/:/tmp/src:z \
			-v ${HOME}/.config/openstack/:/opt/app-root/src/.config/openstack/:z \
			-v /etc/pki:/etc/pki:ro \
			-it ${IMAGE_NAME}:${IMAGE_TAG} bash


.PHONY: push
push:
		docker push ${IMAGE_NAME}:${IMAGE_TAG}
