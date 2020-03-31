[Debian] Changing Docker's default /var/lib/docker directory
============================================================

:date: 2019-09-10 18:40
:slug: moving-docker-default-directory-debian
:tags: debian, docker, directory, systemd
:lang: en


By default, Docker storage its files in the `/var/lib/docker` directory in the file system. If, like me, you're running out of disk space in the default file system, you can quickly change the default directory. This are the steps I followed in Debian 10, it should work with any distro that uses `systemd`

As superuser, modify the systemd docker startup script. Edit the file `/lib/systemd/system/docker.service` replacing the `ExecStart` command:

.. code-block:: bash

   $ sudo vim /var/systemd/system/docker.service

Change the line:

.. code-block:: bash

   ExecStart=/usr/bin/docker daemon -H fd://

to

.. code-block:: bash

   ExecStart=/usr/bin/docker daemon -g /new/path -H fd://

then stop the service, and be sure that the daemon is completely stopped:

.. code-block:: bash

   $ sudo systemctl stop docker
   $ ps -aux | grep -i docker

The only output should be the one from `grep`. Then you can reload the system and -optionally- synchronize your current docker data to the new directory

.. code-block:: bash

   $ sudo systemctl daemon-reload
   $ sudo mkdir /new/path
   $ sudo rsync -aqxP /var/lib/docker /new/path

Your docker installation should be running in the new data directory:

.. code-block:: bash

   $ ps -aux | grep -i docker


That's it.
