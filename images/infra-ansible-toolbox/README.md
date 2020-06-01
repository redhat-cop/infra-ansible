<<<<<<< HEAD
# infra-ansible-toolbox

## Overview

The infra-ansible-toolbox container is a built on the [Toolbox](https://github.com/containers/toolbox) project. Toolbox runs Podman under the hood and puts the new cgroup-v2 features to good use.

[Why use toolbox?](https://docs.fedoraproject.org/en-US/fedora-silverblue/toolbox/#toolbox-why-use)

- It keeps the host OS clean and stable, and helps to avoid the clutter that can happen after installing lots of development tools and packages.
- Containers are a safe space to experiment: if things go wrong, it’s easy to throw a toolbox away and start again.
- Containers are a good way to isolate and organise the dependencies needed for different projects.

On that note, there are some pitfalls to avoid. Ensure your user is a local user and not a network user as you will likely run into issues with user namespace mapping. When a user authenticates through a network-based identity management system, they will not automatically have the required entries in /etc/subuid and /etc/subgid for user namespace mapping.
=======
### infra-ansible-toolbox

The infra-ansible-toolbox container is a built on the [Toolbox](https://github.com/containers/toolbox) project.
>>>>>>> 1ac5c3f... updated readme for toolbox

The goal is to create a development environment with all of the dependencies required to run infra-ansible playbooks. Starting with the latest release,there should be a corresponding toolbox image with all of the correct dependencies to run any playbook in this repository. For example [https://github.com/redhat-cop/infra-ansible/tree/v1.0.15](https://github.com/redhat-cop/infra-ansible/tree/v1.0.15) should work with `infra-ansible-toolbox:v1.0.15` and so on.

RPM-based packages (such as httpd-tools and pandoc) are defined and installed from [extra-packages](./extra-packages) and Python dependencies are found in [requirements.txt](./requirements.txt)

## Usage

### Build base image

To create the image with buildah on your local machine, first lets set some variables:

```bash
export IMAGE_NAME=infra-ansible-toolbox
export IMAGE_TAGS=$(git rev-list --tags --max-count=1)
export IMAGE_TAG=$(git describe --tags ${IMAGE_TAGS})
```

Build the container:

```bash
buildah bud -t ${IMAGE_NAME}:${IMAGE_TAG} -f Containerfile .
=======
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

<<<<<<< HEAD
### Create and enter toolbox

The `toolbox create` command will run the container with a specific set of flags:

```bash
toolbox create --image ${IMAGE_NAME}:${IMAGE_TAG} --container ${IMAGE_NAME}
```

You can verify your container is running with `toolbox list` which shows a filtered output of `podman ps -a` and `podman image list -a`

```bash
toolbox list
IMAGE ID      IMAGE NAME                               CREATED
209371689f30  localhost/infra-ansible-toolbox:v1.0.15  2 hours ago

CONTAINER ID  CONTAINER NAME         CREATED      STATUS             IMAGE NAME
04527b5bc536  infra-ansible-toolbox  2 hours ago  Up 18 minutes ago  localhost/infra-ansible-toolbox:v1.0.15

```

Running `toolbox enter` is similar to running `podman exec -it ${CONTAINER_ID} bash` to shell into a container.

```bash
toolbox enter --container ${IMAGE_NAME}
```

### Using the infra-ansible-toolbox

Your $HOME directory will be mounted in the container and your user will be you! You will appear to have elevated *sudo* permissions in the toolbox, however the root user in the container will have the same permissions as the user you used to enter. This will allow you to install a one-off package if needed without needing actual root priveleges on your system!


### Cleanup

In order to uninstall or reset the image, you will need to first stop the container, then you can remove the toolbox image. **Be careful when using the `toolbox reset` command as it will perform a `podman system reset` which will affect your other non-toolbox containers, images and volumes.**

```bash
toolbox create --image ${IMAGE_NAME}:${IMAGE_TAG} --container ${IMAGE_NAME}
toolbox enter --container ${IMAGE_NAME}
```

In order to uninstall or reset the image, you will need to kill the container before removing the image
>>>>>>> 1ac5c3f... updated readme for toolbox

```bash
podman kill ${IMAGE_NAME}
toolbox rm ${IMAGE_NAME}
```

