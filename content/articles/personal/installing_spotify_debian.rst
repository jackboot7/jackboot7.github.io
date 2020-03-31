A Quick Guide to Install Spotify in Debian 9.0
==============================================

:date: 2017-07-05 09:30
:slug: installing-spotify-debian
:tags: personal, spotify, debian, music, install, apt
:lang: en

A quick guide of the steps I took to install *Spotify version 1.0* in Debian 9.0. First of all, the Spotify team doesn't (officially) support the Linux version, so even if they claim to be compatible with de lastest version of Ubuntu's LTS, it tends to fall behind with the dependencies.


With a fresh install of Debian, you'll need *dirmngr* installed before adding the Spotify repository to your *apt* list:

.. code-block:: bash

    $ sudo apt install dirmngr

After *dirmngr* installation, you'll need to add the Spotify keys and repositories (just check the instructions in the `Spotify for Linux`_ website):

.. code-block:: bash

    $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886
    $ echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list

If you follow the instructions at Spotify's website, the installation should be ready with the update and install commands from apt:

.. code-block:: bash

    $ sudo apt update && sudo apt install spotify-client


But is a common case that not all the dependencies are up to date between Spotify and Debian, so you'll need to add them "by hand".

.. code-block:: bash

	The following packages have unmet dependencies:
	 spotify-client : Depends: libssl1.0.0 but it is not installable
					  Recommends: libavcodec54 but it is not installable or
								  libavcodec-extra-54 but it is not installable
					  Recommends: libavformat54 but it is not installable
	E: Unable to correct problems, you have held broken packages.

	
First you'll have to download the exact same version of the package that Spotify needs, in my case it was *libssl1.0.0*, I downloaded it from: `https://packages.debian.org/jessie/libssl1.0.0`_.

Then just install it with apt and try re-installing Spotify:

.. code-block:: bash

    $ wget http://security.debian.org/debian-security/pool/updates/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb
    $ sudo apt install ./libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb  # This can be replaced with sudo dpkg -i ./libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb
    $ sudo apt install spotify-client


You should be able to use Spotify in your Debian 9.0 following these steps!

**(If you have a premium account, you can use Spotify inside of third party clients such as Clementine in KDE)**

Sources:
---------

* `Spotify's community forum`_ 
* `Debian Wiki for Spotify`_

.. _`Spotify for Linux`: https://www.spotify.com/mx/download/linux/
.. _`https://packages.debian.org/jessie/libssl1.0.0`: `https://packages.debian.org/jessie/libssl1.0.0`
.. _`Spotify's community forum`: https://community.spotify.com/t5/Desktop-Linux-Windows-Web-Player/Debian-9-higher-versions-dependencies/m-p/1721521#M190484
.. _`Debian Wiki for Spotify`: https://wiki.debian.org/spotify
