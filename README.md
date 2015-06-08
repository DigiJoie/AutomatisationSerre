# AutomatisationSerre
Projet d'automatisation de serre réalisé au iMuFab

Le projet d'automatisation de Serre a été réalisé par le iMuFab en collaboration avec Antoine Malouin dans le cadre d'un projet avec le pavillon d'agriculture de McGill.

Matériels utilisés:

-Micro-contrôleur Arduino uno

-4 Valve solenoid série 2400:
Caractéristiques techniques électriques
.Solénoïde : 24 V c.a.
.Courant d'appel volt-ampère : 24 V c.a.-9,6 VA
.Courant d'appel : 4 ampères
.Courant de maintien volt-ampère : 24 V c.a.-4,8 VA
.Courant de maintien : 2 ampères

-Modules 4 relais de keyes funduino 2x

-4 capteurs d'humidités au sol Vegetronix VH400

-2 Photorésistance de 10k

-Micro ordinateur Rapsberry Pi

-écrand touchscreen adafruit 1024x600 7" avec port hdmi

-4 Modules de lumière Led commercial LS1011 LidLum

-2 Modules de lumière contrôlable par relais

-Hub USB avec alimentation externe et fils USB

-Power Supply 24V 15A

-Power supply pour arduino, et raspberry pi

-Des fils pour souder les composantes enssembles

Assemblage:

PhotoRésistances:
http://fr.wikipedia.org/wiki/Diviseur_de_tension

CapteurLumièreA - Résistance 10k----|----PhotoRésistance-----Ground Arduino
                                    |
                            Pin Analogique 4 Arduino
                            

CapteurLumièreB - Résistance 10k----|----PhotoRésistance----Ground Arduino
                                    |
                            Pin Analogique 5 Arduino

Module 4 relais Funduino Keyes:
VCC-Int1-Int2-Int3-Int4-GND

Arduino:
Pin Digital:
0:RX ne pas utiliser
1:TX ne pas utiliser
2:CapteurHumiditéA - fils rouge VH400 
3:CapteurHumiditéB - fils rouge VH400
4:CapteurHumiditéC - fils rouge VH400
5:CapteurHumiditéD - fils rouge VH400
6:CapteurLumièreA -Avant résistance 10k
7:CapateurLumièreB- Avant résistance 10k
8:Relay pour Valve SolenoidA --- Relai funduino keyesA int1
9:Relay pour Valve SolenoidB --- Relai funduino keyesA int2 
10:Relay pour Valve SolenoidC--- Relai funduino keyesA int3
11:Relay pour Valve SolenoidD--- Relai funduino keyesA int4
12:Relay pour Module LumièreA--- Relai funduino keyesB int1 
13:Relay pour Module LumièreB--- Relai funduino keyesB int2

Analog Pin
0:CapteurHumiditéA - fil noir VH400
1:CapteurHumiditéB - fil noir VH400
2:CapteurHumiditéC - fil noir VH400
3:CapteurHumiditéD - fil Noir VH400
4:PhotoRésistanceA - après résistance 10k avant PhotoRésistanceA 
5:PhotoRésistanceB - après résistance 10k avant PhotoRésistanceB 

Ground Arduino
CapteurHumiditéA - fil dénudé VH400
CapteurHumiditéB - fil dénudé VH400
CapteurHumiditéC - fil dénudé VH400
CapteurHumiditéD - fil dénudé VH400
PhotoRésistanceA - Après PhotoRésistanceA
PhotoRésistanceB - Après PhotoRésistanceB
Relai Funduino keyesA - GND
Relai Funduino keyesB - GND

5V Arduino
Relai Funduino keyesA - VCC
Relai Funduino keyesB - VCC
