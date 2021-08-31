Infra Ansible Docker Client
===========================

Produces a container capable of acting as a client for interacting with hosting infrastructure, such as OpenStack and AWS.

## Setup

The following steps are required to run the docker client.

1. Install docker
  1. on RHEL/Fedora: ```{yum/dnf} install docker```
  2. on Windows: [Install Docker for Windows](https://docs.docker.com/windows/step_one/)
  3. on OSX: [Max OS X](https://docs.docker.com/installation/mac/)
  4. on all other Operating Systems: [Supported Platforms](https://docs.docker.com/installation/)
2. Give your user access to run Docker containers (this is only required in Linux/Unix distros)
```
groupadd docker
usermod -a -G docker ${USER}
systemctl enable docker
systemctl restart docker
```

## Running

For OpenStack and AWS specific see the example runs below. For all others use the following generic run example.

**podman**:
```
podman run -u `id -u` \
      -v $HOME/.ssh/id_rsa:/tmp/.ssh/id_rsa \
      -v $HOME/src/:/tmp/src \
      -e INVENTORY_DIR=/tmp/src/<path-to-your-inventory> \
      -e PLAYBOOK_FILE=/tmp/src/<path-to-your-playbook> \
      -t quay.io/redhat-cop/infra-ansible
```

**docker**:
```
docker run -u `id -u` \
      -v $HOME/.ssh/id_rsa:/tmp/.ssh/id_rsa \
      -v $HOME/src/:/tmp/src \
      -e INVENTORY_DIR=/tmp/src/<path-to-your-inventory> \
      -e PLAYBOOK_FILE=/tmp/src/<path-to-your-playbook> \
      -t quay.io/redhat-cop/infra-ansible
```

... or, to run in interactive mode:

```
docker run -u `id -u` \
      -v $HOME/.ssh/id_rsa:/tmp/.ssh/id_rsa \
      -v $HOME/src/:/tmp/src \
      -it quay.io/redhat-cop/infra-ansible /bin/bash
```

### For OpenStack

The following setup setps are required to be done *once* in any new environments:

* Obtain the [OpenStack RC File](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/11/html/command-line_interface_reference/ch_cli#cli_openrc)
  * For the purpose of this write-up, copy the file to `~/.config/openstack/openrc.sh`
* A [Key-pair in OpenStack](https://github.com/naturalis/openstack-docs/wiki/Howto:-Creating-and-using-OpenStack-SSH-keypairs-on-Linux-and-OSX)
* Copy ```clouds.yaml``` file from [here](../../files/clouds.yaml) to `~/.config/openstack/clouds.yaml`

**NOTE** The default ```clouds.yaml``` available for download from OpenStack UI should not be used with the playbooks available in this repository. 

A typical run of the image would look like:

```
docker run -u `id -u` \
      -v $HOME/.ssh/id_rsa:/tmp/.ssh/id_rsa \
      -v $HOME/src/:/tmp/src \
      -v $HOME/.config/openstack/:/tmp/.config/openstack/ \
      -v /etc/pki:/etc/pki \
      -e INVENTORY_DIR=/tmp/src/<path-to-your-inventory> \
      -e PLAYBOOK_FILE=/tmp/src/<path-to-your-playbook> \
      -e OPTS="-e some-extra-var=my-value" \
      -t quay.io/redhat-cop/infra-ansible
```

**NOTE:** The above commands expects the following inputs:
* Your ssh key to be mounted in the container at `/tmp/.ssh/id_rsa`
* An link:https://docs.openstack.org/user-guide/common/cli-set-environment-variables-using-openstack-rc.html[OpenStack RC file] to be mounted at `/tmp/.config/openstack/opensh.rc`.
* Your ansible inventories and playbooks repos to live within the same directory, mounted at `/tmp/src`
* The `/etc/pki` repo has some custom certs needed by the container 

### For AWS
A typical run of the image would look like:

```
docker run -u `id -u` \
      -v $HOME/.ssh:/tmp/.ssh \
      -v $HOME/aws-credentials.csv:/tmp/aws-credentials.csv \
      -v $HOME/src/:/tmp/src \
      -e INVENTORY_DIR=/tmp/src/<path-to-your-inventory> \
      -e PLAYBOOK_FILE=/tmp/src/<path-to-your-playbook> \
      -e OPTS="-e some-extra-var=my-value" \
      -t quay.io/redhat-cop/infra-ansible
```

The above commands expects the following inputs:
* Your ssh key (~/.ssh/id_rsa) to be mounted in the container at `/tmp/.ssh/id_rsa`
* Your AWS credentials (in CSV format) is available in your home directory
* Your ansible inventories and playbooks repos to live within the same directory, mounted at `/tmp/src`

> **NOTE:** The AWS credentials file can be using the .csv as downloaded from AWS, or a .sh file can be used and will be sourced as-is (make sure the **AWS_SECRET_ACCESS_KEY** and **AWS_ACCESS_KEY_ID** environment variables are exported correctly).

### Supplying a TSIG key for DNS management with nsupdate

When doing DNS management with nsupdate, the TSIG key information can be sourced from a TSIG file. These parameters will then be available as environment variables, as shown below:

```
docker run -u `id -u` \
         :
      -v $HOME/my-tsig-file.key:/tmp/tsig.key \
         :
      -t quay.io/redhat-cop/infra-ansible
```

The parameters are then available as environment variables:

```
>  env | grep TSIG
TSIG_KEY_SECRET= ...
TSIG_KEY_NAME= ...
TSIG_KEY_ALGORITHM= ...
```

## Building the Image

This image is built and published to docker.io, so there's no reason to build it if you're just wanting to use the latest stable version. However, if you need to build it for development reasons, here's how:

**buildah**
```
cd ./infra-ansible
buildah bud -f images/infra-ansible/Dockerfile -t quay.io/redhat-cop/infra-ansible .
```

**docker**
```
cd ./infra-ansible
docker build -f images/infra-ansible/Dockerfile -t quay.io/redhat-cop/infra-ansible .
```

## Troubleshooting

Below are some of helpful hints for resolving issues experiencing while configuring and running the container

**Issue**

Getting "permission denied" when attempting to run the docker image, e.g. something similar to:

```
 :
time="2015-09-01T11:32:36-04:00" level=fatal msg="Get http:///var/run/docker.sock/v1.18/images/json: dial unix /var/run/docker.sock: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS?"
 :
FATA[0000] Post http:///var/run/docker.sock/v1.18/containers/create: dial unix /var/run/docker.sock: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS?
 :
```

**Resolution**

This error indicates the currently logged in user is unable to access the docker socket.

To resolve this issue, create a new *docker* group and add the user to the *docker* group

```
groupadd docker
usermod -a -G docker ${USER}
systemctl enable docker
systemctl restart docker
```

Reboot the machine or log out/log in to reload your environment and complete the configurations.

**Issue**

Getting "permission denied" when attempting to access external files mounted to the container:

```
$ docker run \
 -u `id -u` \
 -v $HOME/.ssh/id_rsa:/tmp/.ssh/id_rsa \
 -v $HOME/Workspace:/tmp/src \
 -it quay.io/redhat-cop/infra-ansible \
 /bin/bash
 :
bash-5.1$ cat $HOME/.ssh/id_rsa 
cat: /tmp/.ssh/id_rsa: Permission denied
 :
```
This error generated because SELinux context was not properly configured  for attached volume. 

**NOTE** the resolution may vary based on your runtime environment, for example using a shared filesystem for your home directory may have a different resolution and outcome than those described here. 

**Resolution #1**

As described at docker-run manual [page](https://docs.docker.com/storage/bind-mounts/#configure-the-selinux-label):

>if you use selinux you can add the ```z``` or ```Z``` options to modify the selinux label of the host file or directory being mounted into the container. This affects the file or directory on the host machine itself and can have consequences outside of the scope of Docker.
> * The z option indicates that the bind mount content is shared among multiple containers.
> * The Z option indicates that the bind mount content is private and unshared.
>
>Use **extreme caution** with these options. Bind-mounting a system directory such as /home or /usr with the Z option renders your host machine inoperable and you may need to relabel the host machine files by hand.
```
$ docker run \
 -u `id -u` \
 -v $HOME/.ssh/id_rsa:/tmp/.ssh/id_rsa:z \
 -v $HOME/Workspace:/tmp/src:z \
 -it quay.io/redhat-cop/infra-ansible \
 /bin/bash
```

**Resolution #2**

The host directory needs to be configured with the appropriate SELinux context, which is ```container_file_t```. Docker uses the ```container_file_t``` SELinux context to restrict which files of the host system the container is allowed to access (```$HOME/Workspace``` used as example).

1. Apply the ```container_file_t``` context to the directory (and all sub-directories) to allow containers access to all its contents:
```
$ sudo semanage fcontext -a -t container_file_t '$HOME/Workspace(/.*)?'
```

2. Apply the SELinux container policy that was created in the first step to the directory:
```
$ sudo restorecon -Rv $HOME/Workspace
```

3. Verify that the SELinux context type for the $HOME/Workspace directory is ```container_file_t```:
``` 
$ ls -ldZ /var/local/mysql
drwxr-xr-x. root root unconfined_u:object_r:container_file_t:s0 $HOME/Workspace
```
