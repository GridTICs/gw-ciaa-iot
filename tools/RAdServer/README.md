# Configuración para Router Advertisement Server (y router IPv6)

*Escenario*: El Gateway IoT no funcionará como tal si no recibe anucios
de rutas. En una red IPv4 only acontecerá esto.

Estos archivos de configuración son para un sistema ubuntu server 16.04
(podría ser uno distinto).
Está la configuración para `radvd`, `interfaces` para tener una IPv6 estática
propia y `sysctl.conf`.

Se entregan algnos archivos en formato diff para agregar solamente la informaciRónn que resulta necesaria para no generar interferencia con futuras versiones de los paquetes.

Notar que el tráfico de LAN a PAN pasará por este equipo que hace los anuncios.

## Instrucciones

Instalar ubunt 16.04 server. Podría ser en una máquina virtual. Una instalación
mínima es suficiente.

Si se tratara de una máquina virtual de virtualbox instalar los guest utils

	sudo apt-get install virtualbox-guest-utils virtualbox-guest-x11-

Para tener andando a radvd instalar además el server ssh y screen

	sudo apt-get install screen radvd ssh

Luego aplicar los archivos  contenidos en este directorio

* interfaces.diff: diff que aplica dirección fdb7:da99:8748:9289::1/64 al equipo
* radvd.conf: archivo de configruación de radvd que anuncia rutas para fd00::0/64
* sysctl.conf.diff: habilitación de reenvío de paquetes IPv6.
* README.md: este archivo
