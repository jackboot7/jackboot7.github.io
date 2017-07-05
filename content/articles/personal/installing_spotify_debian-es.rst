Guía rápida de instalación de Spotify en Debian 9.0
====================================================

:date: 2017-07-05 09:30
:slug: installing-spotify-debian
:tags: personal, spotify, debian, music, install, apt
:lang: es


Una guía rápida de los pasos que tomé para instalar la *versión 1.0 de Spotify* en Debian 9.0. Primero que nada, la versión para Linus de Spotify no está soportada oficialmente, entonces, a pesar de que Spotifiy la anuncia como compatible con la última versión LTS de Ubuntu, tiende a quedar atrasada en cuanto a sus dependencias.


En una instalación limpia de Debian, será necesario tener instalado *dirmngr* antes de poder agregar los repositorios de Soptify a tus repositorios *apt*:

.. code:: bash

    $ sudo apt install dirmngr

Luego de la instalación de *dirmngr*, es necesario agregar las claves y repositorios de Spotify (siguiendo los pasos de la página de instalación de `Spotify para Linux`):

.. code:: bash

    $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886
    $ echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list


Si sigues las instrucciones en el website de Spotify, la instalación debería terminar con los comandos de *update* e *install* de apt:

.. code:: bash

    $ sudo apt update && sudo apt install spotify-client


Pero es común que no todas las dependencias estén al día entre Spotify y Debian, entonces habrá que agregarlas "a mano".

.. code:: bash

	The following packages have unmet dependencies:
	 spotify-client : Depends: libssl1.0.0 but it is not installable
					  Recommends: libavcodec54 but it is not installable or
								  libavcodec-extra-54 but it is not installable
					  Recommends: libavformat54 but it is not installable
	E: Unable to correct problems, you have held broken packages.

	
En primer lugar, deberás descargar la versión exacta del paquete que Spotify necesita, en mi caso era necesario *libssl1.0.0*, el cual descargué desde: `https://packages.debian.org/jessie/libssl1.0.0`_.

Luego, sólo tendrás que instalarlo con apt e intentar instalar Spotity:

.. code:: bash

    $ wget http://security.debian.org/debian-security/pool/updates/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb
    $ sudo apt install ./libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb  # This can be replaced with sudo dpkg -i ./libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb
    $ sudo apt install spotify-client


Deberías poder usar Spotify en tu Debian 9.0 siguiendo estos pasos!

(Si tienes una cuenta *Premium*, puedes usar Spotify en aplicaciones de terceros como Clementine en KDE)

Fuentes:
--------

* `Foro de la comunidad de Spotify`_ 
* `Debian Wiki para Spotify`_

.. _`Spotify para Linux`: https://www.spotify.com/mx/download/linux/
.. _`https://packages.debian.org/jessie/libssl1.0.0`: `https://packages.debian.org/jessie/libssl1.0.0`
.. _`Foro de la comunidad de Spotify`: https://community.spotify.com/t5/Desktop-Linux-Windows-Web-Player/Debian-9-higher-versions-dependencies/m-p/1721521#M190484
.. _`Debian Wiki para Spotify`: https://wiki.debian.org/spotify
