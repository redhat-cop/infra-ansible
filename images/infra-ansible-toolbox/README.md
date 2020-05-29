### infra-ansible-toolbox

The infra-ansible-toolbox container is a built on the [Toolbox](https://github.com/containers/toolbox) project.

The goal is to create a development environment with all of the dependencies required to run infra-ansible playbooks. Starting with the latest release,there should be a corresponding toolbox image with all of the correct dependencies to run any playbook in this repository. For example [https://github.com/redhat-cop/infra-ansible/tree/v1.0.15](https://github.com/redhat-cop/infra-ansible/tree/v1.0.15) should work with `infra-ansible-toolbox:v1.0.15` and so on.

RPM-based packages (such as httpd-tools and pandoc) are defined and installed from [extra-packages](./extra-packages) and Python dependencies are found in [requirements.txt](./requirements.txt)

To build the image with podman in your local machine, first set some variables:

```bash
export IMAGE_NAME=infra-ansible-toolbox
export IMAGE_TAG=$(git describe --tags `git rev-list --tags --max-count=1)
```

Build the container image with Podman:

```bash
podman build -t ${IMAGE_NAME}:${IMAGE_TAG} -f Containerfile .
```

You will need the toolbox CLI tool as noted above to create and enter the infra-ansible-toolbox container

```bash
toolbox create --image ${IMAGE_NAME}:${IMAGE_TAG} --container ${IMAGE_NAME}
toolbox enter --container ${IMAGE_NAME}
```

In order to uninstall or reset the image, you will need to kill the container before removing the image

```bash
podman kill ${IMAGE_NAME}
toolbox rm ${IMAGE_NAME}
```

