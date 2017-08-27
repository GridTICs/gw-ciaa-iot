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

Indicar compilar el programa del proyecto

```
cat >Makefile.mine << EOF
BOARD          ?= ciaa_nxp
PROJECT_PATH ?= examples$(DS)blinking_lwip
```

Parchar acceso a stack de OS

	bash parchar_memstatica.sh

Pcompilar

	make -s all

Conectar la CIAA a la computadora o VM
Transferir

	make download

Los mensajes de depuración estarán accesibles en el segundo puerto serie del
FTDI. Se puede leerlos usando gtkterm

	gtkterm --port /dev/ttuUSB1 -s 115200

### Ajustes en el código (configuraciones)

Una buena parte de los ajustes se hicieron en `lwipopts.h`, archivo ubicado
en `CIAAFirmware/examples/blinking_lwip/inc/lwipopts.h`.

La Red IPv6 de la WSN es fd00::0/64, eso se ajusta en CIAAFirmware/modules/drivers/cortexM4/lpc43xx/lpc4337/src/ciaaDriverEth.c:204`. Si se quisiera indicar otra red alcanzaría con editar ese archivo.

### Preparar contiki para openmote-cc2538

#### Del lado del border router

Se programa solo un mote

* ir al directorio de contiki

	cd ../contiki/gw-iot/

* compilar mote router border

	cd rpl-border-router/
	make -s

* conectar el mote a un OpenUSB y puentear los pines `ON/SLEEP` y `GND`
* conectar el OpenUSB a la computadora o VM
* transferir el firmware

	make border-router.upload

* desconectar el puente de programación
* instalar el mote en la placa adaptadora a RS232

#### Mote entregando datos

Se programa tantos motes como se desee, el origen de los datos son los sensores
de OpenUSB.

* ir al directorio de contiki

	cd ../../../contiki/gw-iot/

* compilar mote router border

	cd udp-ipv6-client/
	make -s

* conectar el mote a un OpenUSB y puentear los pines `ON/SLEEP` y `GND`
* conectar el OpenUSB a una computadora o VM
* transferir el firmware

	make udp-client.upload

Se puede transferir el mismo binario a todos los motes

#### Ajustes en el código

Las intervenciones al código para openmote han sido comentadas con el string
`GW-IoT`, para cada una se explica y justifica el uso.
Se puede ajustar el Número de IP(v6) del servidor al cual enviar datos entre otras cosas.

## Servidor de recolección de datos

Los motes envían la información en texto plano como CSV por UDP al puerto 3000
del host indicado en project-conf.h del udp-client.

La primera fila es número de secuencia de 16 bits sin signo, para el ñumero de secuencia 0 se indica qué parámetro ambiental es cada valor.

TODO: servidor de carlos, instructivo de depsliegue.

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
