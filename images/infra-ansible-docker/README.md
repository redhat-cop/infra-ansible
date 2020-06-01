# infra-ansible docker image

This image borrows heavily from [casl-ansible](https://github.com/redhat-cop/casl-ansible/blob/master/images/casl-ansible/README.md) for managing permissions and dependencies. The primary difference is this Docker image is based on ubi8 rather than openshift-ansible. For a **Podman/Buildah** approach, it is recommended that you use the [infra-ansible-toolbox](../infra-ansible-toolbox) OCI container image.

## For OpenStack

Running infra-ansible with OpenStack:

```bash
docker run -it --net=host -u $(id -u) \
  -v $HOME/.ssh/:/opt/app-root/src/.ssh:z \
  -v $HOME/src/:/tmp/src:z \
  -v $HOME/.config/openstack/:/opt/app-root/src/.config/openstack/:z \
  infra-ansible bash
```

Note that this will mount your ssh keys from a known location and assumes your Ansible inventories and playbooks are in the ~/src directory. Please modify as needed for your local development environment.

## Building the Image

```bash
docker build -t infra-ansible .
```
