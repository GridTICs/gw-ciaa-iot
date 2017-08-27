# Despliegue para Gatetway IoT con CIAA

## Entorno de desarrollo

El entorno de desarrollo ha sido la máquina virtual creada por Carlos
Taffernaberry y actualizada algunas veces. A continuación algunos datos
esenciales.

	developer@ciaa:~$ lsb_release -a
	No LSB modules are available.
	Distributor ID:	Ubuntu
	Description:	Ubuntu 14.04.5 LTS
	Release:	14.04
	Codename:	trusty
	developer@ciaa:~$ arm-none-eabi-gcc --version
	arm-none-eabi-gcc (GNU Tools for ARM Embedded Processors) 4.9.3 20150529 (release) [ARM/embedded-4_9-branch revision 227977]
	Copyright (C) 2014 Free Software Foundation, Inc.
	This is free software; see the source for copying conditions.  There is NO
	warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

	developer@ciaa:~$

## Despliegue

Se deben realizar las siguientes operaciones

### Clonar este repositorio con sus submódulos

	git clone --recursive https://git.wsn.gridtics.frm.utn.edu.ar/ciaa-lowpan/gw-ciaa-iot.git
	cd gw-ciaa-iot/

### Preparar Firmware para CIAA

	cd CIAAFirmware/
	# indicar compilar el programa del proyecto
	cat >Makefile.mine << EOF
	BOARD          ?= ciaa_nxp
	PROJECT_PATH ?= examples$(DS)blinking_lwip
	# parchar acceso a stack de OS
	bash parchar_memstatica.sh
	# compilar
	make -s all
	# conectar la CIAA a la computadora o VM y transferir
	make download

Los mensajes de depuración estarán accesibles en el segundo puerto serie del FTDI. Se puede leerlos usando gtkterm

	gtkterm --port /dev/ttuUSB1 -s 115200

### Preparar contiki para openmote-cc2538

FIXME

## Apéndice 1: Escenario sin IPv6 de alcance global

FIXME radvd

## TODOs / Posibilidades de Mejora

### En Motes

* acceso al servidor por nombre de host
* FIXME: Muchos otros

## En CIAA

* MAC address desde [Nro de serie](https://www.lpcware.com/content/forum/read-serial-number).
* Higiene de código para compartir código
* FIXME: Muchos otros
