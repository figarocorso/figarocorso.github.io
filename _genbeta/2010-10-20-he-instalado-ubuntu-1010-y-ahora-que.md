---
layout: post
title: "He instalado Ubuntu 10.10, y ¿ahora qué?"
category: genbeta
---



El primer paso después de instalar nuestro **sistema operativo favorito es
personalizarlo y dejarlo a nuestro gusto**. Después de años utilizando
nuestras aplicaciones _fetiche_ no podemos dejar pasar la oportunidad y
necesitamos tenerlas instaladas lo antes posible. De hecho, la mayoría de
nosotros hemos visto pasar la noche y la madrugada enfrascados en tales
_quehaceres_.

En este caso, después del lanzamiento de la nueva versión de Ubuntu,
**Maverick Meerkat** (10.10), aprovechamos para dar unas pinceladas sobre esos
**primeros pasos poniendo a tono nuestras aplicaciones favoritas**. Muchos de
estos pasos no serán nuevos para vosotros, pero siempre hay alguna sorpresa.  
  

## Primeros pasos

  
Sigue siendo un fastidio, pero el primer paso para hacer el recorrido un poco
más fácil será **abrir la terminal** (se encuentra bajo el menú _Aplicaciones
> Accesorios_). La verdad es que, cuando uno se familiariza con el comando
_apt-get install_, poner a tono nuestro sistema operativo es mucho más rápido
y sencillo de lo que parecía en un principio. Empezamos a poner a tono a
nuestro [Ubuntu Maverick Meerkat](http://www.genbeta.com/productos/sistemas-
operativos/ubuntu-maverick-meerkat).

Como siempre antes de instalar un paquete, es muy recomendable **actualizar la
información de los repositorios** y de los componentes que ya tenemos
instalados. Lo primero se consigue mediante la siguiente orden:

    
    
    sudo apt-get update

La actualización de los componentes la tendremos con:  

    
    
    sudo apt-get -y dist-upgrade

## Ubuntu Restricted Extras

  
Como diría el manual del comando _apt-get_, es aquí donde el artículo adquiere
los _Poderes de Súper Vaca_. Ya habíamos hablado acerca de las maravillas de
los **repositorios de Medibuntu**, de forma que podíamos añadir mediante apt-
get algunas de aquellas aplicaciones que no estaban incluidas en los
repositorios oficiales.

Si queremos **quitarnos muchos dolores de cabeza** y unas cuantas más
búsquedas en Google, no tenemos más que ejecutar el siguiente comando:

    
    
    sudo apt-get -y install ubuntu-restricted-extras

De esta forma **se instalarán de forma automática** (entre otros) los
siguientes componentes: **Adobe Flash Player**, Java Runtime Enviroment
**(JRE)**, una colección de fuentes de Microsoft (las famosas msttcorefonts),
diferentes codecs multimedia que acabaremos necesitando tarde o temprano
(incluido mp3), el compresor **unrar**, un paquete para decodificación de DVD
y más utilidades audiovisuales.

## Alternativas a los programas pre-instalados

  
![VLC icon](http://img.genbeta.com/2010/10/ubuntu-10-10-vlc-icon.jpg)Lo
admito, siempre defendía Ubuntu como un sistema operativo que puedes usar en
cuanto se instala. Pero siempre escondo mis **manías**, que con el tiempo, me
he dado cuenta de que eran **compartidas por bastantes usuarios**.

Totem no está mal. No es una delicia de reproductor, pero funciona… (sudo apt-
get -y remove totem). Así que las **dos alternativas que suelen tener más
adeptos**. En este caso [VLC](http://www.genbeta.com/productos/reproductores-
video/vlc) y MPlayer son los candidatos perfectos. Fácil y sencillo:  

    
    
    sudo apt-get -y install vlc  
    
    
    sudo apt-get -y install mplayer

De igual manera cuando empezaba por estos lares Rhythmbox me parecía un gran
reproductor de música. Pero podemos deshacernos de él, fácilmente con el _sudo
apt-get -y remove rythmbox_.

En esta ocasión personalmente **siempre me decantaba por Exaile**:  

    
    
    sudo apt-get -y install exaile

  

![Banshee icon](http://img.genbeta.com/2010/10/ubuntu-10-10-banshee-
icon.jpg)Pero últimamente me estoy viendo arrastrado al lado oscuro de
**[Banshee](http://www.genbeta.com/productos/reproductores-audio/banshee) ya
que me resulta más intuitivo y con mejores plugins**:  

    
    
    sudo apt-get -y install banshee

  

## Imprescindibles: Gráficos y descargas

  
En el territorio de la edición y creación de gráficos no pueden faltar **dos
estandartes de los proyectos de código libre**. Hablamos de
[Gimp](http://www.genbeta.com/productos/editores-fotograficos/gimp) e
[Inkscape](http://www.genbeta.com/imagen-digital/ya-esta-disponible-un-nuevo-
inkscape-el-048):

    
    
    sudo apt-get -y install gimp

sudo add-apt-repository ppa:ricotz/ppa  
sudo apt-get update  
sudo apt-get install inkscape

Si con esto **creemos que hemos acabado**, la siguiente vez que vayas a
arrancar tu ordenador e intentes abrir tu programa de descargas favorito,
habrás detectado **un pequeño olvido**. Hay bastantes alternativas pero aquí
va mi selección personal para que no haya que buscar por ningún lado:

Descarga directa: [Tucan](http://www.genbeta.com/linux/tucan-gestor-de-
descargas-de-megaupload-y-rapidshare-en-gnulinux)  

    
    
    sudo apt-get -y install tucan

![Vuze icon](http://img.genbeta.com/2010/10/ubuntu-10-10-vuze-icon.jpg)Cliente
de BitTorrent: [Vuze](http://www.genbeta.com/multimedia/vuze-40-otra-vuelta-
de-tuerca-sobre-el-viejo-azureus) (AKA Azureus de otros tiempos)  

    
    
    sudo apt-get -y install vuze

Usando _la mula_ en Linux: [aMule](http://www.genbeta.com/a-fondo/de-burros-
mulas-y-elefantes)  

    
    
    sudo apt-get -y install amule

## Lo último, tu toque personal

  
Si la elección de los programas anteriores ya es personal, más o menos, la
mayoría de los usuarios están de acuerdo en elegir esas aplicaciones como las
mejores. Así que ahora es cuando ya **faltan los últimos retoques**, para
acabar de aliñar la ensalada al gusto, aquí dejo algunos de los que nunca se
me olvidan para cerrar el artículo.

Para **ejecutar aplicaciones Windows**,
[Wine](http://www.genbeta.com/productos/virtualizacion/wine):  

    
    
    sudo apt-get -y install wine1.2

Capturas de pantalla a medida, [Shutter](http://www.genbeta.com/productos
/redes-sociales/shutter):  

    
    
    sudo apt-get -y install shutter

![Avant Window Navigator icon](http://img.genbeta.com/2010/10/ubuntu-10-10
-awn-icon.jpg)Un lanzador de aplicaciones,** un _dock_**, [Avant Window
Navigator](http://www.genbeta.com/herramientas/avant-window-navigator-un-
poderoso-y-hermoso-dock-para-gnulinux-screencast):  

    
    
    sudo apt-get -y install avant-window-navigator

## Últimas reflexiones

  
Desde mi punto de vista la mayoría de las distribuciones GNU/Linux, y en este
caso en concreto Ubuntu, incorporan una multitud de aplicaciones que hacen que
**se pueda utilizar el sistema operativo desde el primer minuto**. En este
aspecto sólo se puede encontrar un paralelismo con los entornos OS X.

La existencia y proliferación de este tipo de manuales por internet es debida
principalmente al perfil de usuarios que instalan Ubuntu en sus ordenadores.
Normalmente **usuarios con un perfil de conocimientos informáticos altos**,
que exigen muchas aplicaciones y, cómo no, también tienen sus **manías**
adquiridas a lo largo de los años.

Es por ello que, si bien son actuaciones recomendables, creo que es
**reseñable el hecho de encontrar un sistema operativo tan completo** y
preparado para su uso desde el minuto cero, donde todo está basado entorno a
la filosofía del software libre. Espero que el lanzamiento del Ubuntu Software
Centre acabe de asentarse y se pueda ver como una especie de iTunes Store o
Android Market en cuanto a aplicaciones se refiere.

Es una pena que, como se ve con el paquete _Ubuntu Restricted Extras_, no se
de un impulso a nivel global a las iniciativas open source. De forma que no
haya **diferencias entre unos países y otros**, aspecto que, a día de hoy, es
una **cortapisa** importante en cuanto al desarrollo y proliferación de
entornos libres en las computadoras domésticas.

Vía | [Slice of Linux](http://sliceoflinux.com/2010/10/13/que-hacer-despues-
de-instalar-ubuntu-10-10-maverick-meerkat-paso-a-paso/)  
En Genbeta | [Medibuntu, porque la vida puede ser
maravillosa](http://www.genbeta.com/linux/medibuntu-porque-la-vida-puede-ser-
maravillosa)

Artículo extraído de [Genbeta](http://www.genbeta.com).