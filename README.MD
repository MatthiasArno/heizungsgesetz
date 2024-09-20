
# Inhalt <!-- omit in toc -->
- [Motivation](#motivation)
	- [Heizenergiebedarf](#heizenergiebedarf)
	- [Heizstab](#heizstab)
	- [Heizlast](#heizlast)
	- [Wärmepumpe](#wärmepumpe)
	- [Wahl der Vorlauftemperatur](#wahl-der-vorlauftemperatur)
	- [Heizkörpergleichung](#heizkörpergleichung)
	- [Verstärkende Effekte](#verstärkende-effekte)
- [Simulation](#simulation)


# Motivation
Als Bewohner eines Altbaus mit Zentralheizung stelle ich mir schon länger die Frage, wie der Umstieg auf eine Wärmepumpe gelingen kann. Im ersten Schritt wird daher eine kleine Überschlagsrechnung durchgeführt, um die relevanten Grössen und Grössenordnungen zu erfassen. Im zweiten Schritt wird eine genauere Berechnung programmatisch mit Zeitreihen durchgeführt.

Ich bin kein Heizungsfachmann! Korrekturen und Verbesserungsvorschläge sind herzlich willkommen.

## Heizenergiebedarf
Die eingesetzte nutzbare Heizenergie $E_h$ entspricht der eingesetzten Primärenergie $E_p$ durch Öl 0der Gas, multipliziert mit der Effizienz $e_h$ der Heizung.

$[1]$ $E_h=E_p*e_h$

Bei einer Ölheizung mit 1000 Liter Jahresverbrauch und einer Effizienz von 0.85 ergibt sich:

$[2]$ $E_h=10.000kWh*0.85=8500kWh$

 Als gute Näherung kann man mit 10kWh pro Liter [Erdöl](https://de.wikipedia.org/wiki/Heiz%C3%B6l) oder [Erdgas](https://de.wikipedia.org/wiki/Erdgas#Physikalisch-technische_Eigenschaften) oder pro Kubikmeter [Erdgas](https://de.wikipedia.org/wiki/Erdgas#Physikalisch-technische_Eigenschaften) rechnen. Unterschiede im Heiz- und Brennwert werden einfach der Effizienz $e_h$ der Heizungsanlage zugeschrieben. In diesem Beispiel mit $e_h=0.85$ gehen 15% der Energie zum Schornstein hinaus. Das ist erstmal eine Annahme.

## Heizstab
Würde man den Öl- oder Gasbrenner durch einen Heizstab ersetzen, der praktisch eine Effizienz von $e_h=1$ hat, würden dafür 8500kWh Strombezug im Jahr fällig. Rechnet man mit 0,28 Cent für die Kilwattstunde Strom und 1,00 Euro für den Liter Heizöl, so stünden Kosten in Euro von 8500kWh*0,28&euro;/kWh=2380 &euro; Strom oder 1000l *1,00 &euro;/l=1000&euro; Heizöl zu buche. Ein reiner Heizstabbetrieb in einer vorhandenen Zentralheizung ist daher keine gute Lösung.


## Heizlast
Die Heizlast hängt von der Temperatur der Innen- und Aussentemperatur ab und kann über Wärmeleitung (Bodenkontakt), Konvektion (Luftumströmung) oder Wärmeabstrahlung geschehen. Das hängt stark vom Standort und der Beschaffenheit des Hauses ab. Es wird hier nur eine ganz einfache lineare Beziehung verwendet und die Heizenergie pro Monat berechnet. Anstelle von Grad Celsius wird für Temperaturdifferenzen die Einheit Kelvin [K] benutzt.

$[3]$ $E_m=(T_i,m-T_a,m)*F$,  mit $E_m$ in [kWh/Monat] und $F$ in [kWh/Monat/K]

Dabei ist $E_m$ der über den Monat m gemittelte Energiebedarf, $T_{i,m}$ bzw. $T_{a,m}$ die Innen- und Aussentemperatur im Mittel für den Monat m und $F$ ein Faktor, der noch zu bestimmen und nicht vom Monat abhängig ist.

Wikipedia liefert die monatlichen [Durchschnittstemperaturen von 2001-2020](https://de.wikipedia.org/wiki/Zeitreihe_der_Lufttemperatur_in_Deutschland) in den 8 Heizmonaten Oktober bis Mai.

Somit ist: $E_h=\sum(Em)$, die eingesetzte Heizenergie pro Jahr ist die Summe der gemittelten monatlichen Heizlasten. 

Vereinfacht wird für $T_i=20$ Grad angenommen:

| $Monat$	| $T_i$[°C]	| $T_a$[°C]	| $T_i-T_a$[K] | 
|----		|----------	|----------	|----------	|
| Oktober 	| 20,0      |  9,7     	| 10,3     	| 
| November  | 20,0    	|  5,3    	| 14,7     	|
| Dezember  | 20,0    	|  2,1     	| 17,9     	|
| Januar  	| 20,0    	|  0,9     	| 19,1     	|
| Februar  	| 20,0    	|  1,5     	| 18,5     	|
| März  	| 20,0   	|  4,6     	| 15,4     	|
| April  	| 20,0    	|  9,2     	| 10,8     	|
| Mai	  	| 20,0    	| 13,2     	| 6,8     	|
| $\sum$    |           |           | **113,5** |

 [Tabelle 1]


$[4]$ $E_h=\sum_{Oktober-Mai}(Em)_{}=(10,3+...+6,8)K*F=113,5K*F$

$[5]$ $F=E_h/113,5K=8500Kwh/113,5K=74,9kWh/K$

Mit F lässt sich dann wieder monatsweise die Heizlast berechnen, bspw. für den kältesten Monat Januar:

$[6]$ $E_{Januar}=(20-0,9)K*74,9kWh/K=1430kWh$

Für den Heizsstab würde das einer mittleren Leistung von $1430kWh/(30*24h)=1,99kW$ entsprechen. Das entspricht der Leistung von zwei Staubsaugern, die rund um die Uhr laufen.

## Wärmepumpe

Eine Wärmepumpe entzieht einem Medium Energie (Luft, Wasser, Boden). Das Verhältnis von bereitgestellter Energie in Form von Wärme zu eingesetzer Energie in Form von Strom hängt dabei von der Temperatur des Mediums zur Vorlauftemperatur im Heizwasserkreis ab. Der Faktor wird COP (Coefficient of Performance) genannt. Die Temperatur des Mediums, insbesondere bei Luftwärmepumpen, ist aber nicht konstant, weshalb der COP über eine Heizsaison gemittelt und dann als SCOP (Seasonal Coefficient of Performance) bezeichnet wird.

Der Heizenergiebedarf $E_h$ reduziert sich um den Faktor des SCOP. Der SCOP ist leider nicht konstant (hoch), sondern hängt sehr deutlich vom Betriebspunkt der Wärmepumpe ab. 

Der COP wird zur Vergleichbarkeit von Luftwärmepumpen üblicherweise bei -7, 2, 7 und 10 oder 12 Grad Mediumtemperatur und Vorlauftemperaturen von 35 und 55 Grad bestimmt. Je geringer die Temperaturdifferenz, desto höher ist der COP. Ab bestimmten hohen Vorlauftemperaturen wird bei manchen Gerätetypen mittels Heizstab geboostert, was den COP dann zusätzlich einknicken lässt. Grundsätzlich ist der COP aber immer grösser als eins. Mit diesen Angaben des Herstellers und Temperaturdurchschnittswerten für die Heizmonate, lässt sich ein SCOP berechnen.

Beispiel für den $COP_{T_a,T_v}$ einer modernen Luftwärmepumpe in Abhängigeit der Luftaussentemperatur $T_a$ und verschiedenen Vorlauftemperaturen $T_v$. In der letzten Spalte sind die Monate eingetragen, für die die Luftaussentemperatur $T_a$ [aus Tabelle 1] im Monatsmittel in etwa gilt.

| $T_a$	| $T_v=35°C$  | $T_v=55°C$  | $T_v=75°C$  | Monat(e), die nahe bei $T_a$ liegen
|----	|----------	|----------	|----------	|---------
| -7 	| 3,04     	| 2,03     	| 1,50     	| -
| +2  	| 4,38     	| 2,50     	| 1,90     	| Dezember, Januar, Februar
| +7  	| 5,04     	| 3,03     	| 2,00     	| November, März
| +10  	| 5,63     	| 3,50     	| 2,10     	| Oktober, April, Mai

[Tabelle 2]

Bei einer Vorlauftemperatur von 35 Grad und 10 Grad Lufttemperatur hat diese Wärmepumpe also einen $COP_{+10,35}=5,63$ und erzeugt aus einer Kilowattstunde Strom 5,63 Kilowattstunden Heizenergie. Bei -7 Grad Lufttemperatur und 75 Grad Vorlauftemperatur stehen nur 1,5 Kilowattstunden zur Verfügung, also $COP_{-7,75}=1,5$.

Analog zu $[1]$ gilt, dass die Heizenergie der eingesetzten Primärenergie (Strom) multipliziert mit dem SCOP für die Wärmepumpe ist, der laut Tabelle irgendwo zwischen 1,5 und 5,63 liegt. 

$[7]$ $E_h=E_p*SCOP$

Zur Berechnung der Primärenergie (Strom) über die Heizmonate bemüht man Gleichung $[3]$, teilt aber den Beitrag durch den COP, im Beispiel für 35 Grad Vorlauftemperatur.

$[8]$ $E_{p,m}=(T_i,m-T_a,m)*F/COP_{T_a,35}$

Weil Tabelle 2 nicht für jeden Wert von $T_a$ eine Angabe enthälte, wird die Zeile gewählt, die möglichst nahe an der Monatsdurchschnittstemperatur liegt. Das ist in der letzten Spalte von Tabelle 2 vermerkt.

$[9]$ $E_{p,Oktober-Mai}=((10,3+10,8+6,8)/5,63+(14,7+15,4)/5,04+(17,9+19,1+18,5)/4,38)*F=23,57K*F$

$[10]$ $SCOP=E_h/E_p=113,5K*F/(23,57K*F)=4,81$

Damit ergäbe sich ein Strompreis von Euro $2380/4,81=494,80$, was deutlich günstiger im Vergleich zum Heizen mit Heizöl ist.


## Wahl der Vorlauftemperatur

Die Wahl der Vorlauftemperatur bestimmt den Wirkungsgrad bzw. Stromverbrauch der Wärmepumpe direkt. Leider kann die Vorlauftemperatur nicht beliebig niedrig gewählt werden. Idealerweise ist sie so hoch, dass die von den Heizkörpern abgestrahle Wärme $E_w$ gerade den Bedarf deckt, den das Haus an die Umwelt verliert $E_h$.

$[8]$ $E_h=(T_i,m-T_a,m)*F$

$[9]$ $E_w=(T_v,m-T_i,m)*G$

$[10]$ $(T_i,m-T_a,m)*F=(T_v,m-T_i,m)*G$



$G$ ist ein Faktor, der von der installierten Fläche der Heizkörper abhängt. Je mehr Fläche zur Verfügung steht, desto grösser ist G, desto geringer kann die Vorlauftemperatur gewählt werden.
F und G bestimmen im Wesentlichen, wie effektiv die Wärmepumpe unter gegebenen Bedingungen arbeiten kann, also ob sich der Einbau einer Wärmepumpe wirtschaftlich rechnet. Für die Vorlauftemperatur $T_v$ ergibt sich dann:

$[11]$ $T_v,m=(T_i,m-T_a,m)*F/G+Ti,m$

Um mit den bisherigen Ergebnissen weiterrechnen zu können, wird ein Verbrauch von 1000 Liter Heizöl angenommen.

Somit bleibt $F=74,9kWh/K$ [aus 5].

Zur Ermittlung des Wertes G muss man nun wissen, welche Heizkörper verbaut sind und welche Daten diese haben. Diese Daten kann man als erste Näherung dieser [Tabelle zur Heizleistung](https://www.heizung.de/ratgeber/diverses/heizleistung-berechnen-gruende-und-ablauf.html) entnehmen. Die Quadratmeterzahl, die man üblicherweise mit 1000l Heizöl beheizen kann findet sich im [Heizölverbrauch]( https://www.heizung.de/oelheizung/wissen/den-heizoelverbrauch-bestimmen-und-senken.html).

Aus diesen Information kann man entnehmen, dass bei einem Altbau von 1970 etwa 20 Liter Heizöl pro Quadratmeter benötigt werden, so dass mit 1000 Liter Heizöl etwa 50 Quadratmetern Wohnfläche beheizt werden können. Weiterhin sind üblicherweise 125W Heizkörperleisung pro Quadratmeter installiert, die bei einer üblichen Vorlauftemperatur von 75 Grad und einer Raumtemperatur von 20 Grad abgegeben werden können. 75Grad Vorlauftemperatur und 20 Grad Raumtemperatur sind die Punkte, bei denen Flächenheizköper üblicherweise bemessen werden.
Das entspricht einer Heizleistung von $50qm*125W/qm=6.25kW$. Um nun die Energie pro Monat zu berechen, wir dieser Wert mit 24h und 30 Tagen multipliziert und angenommen, dass die Wärmepumpe rund um die Uhr durchläuft. 

Das ergibt $6.25kW*24h*30=4500 kWh$

$[12]$ $G=4500kWh/(75-20)Grad=81.8KWh/Grad$

Das ist ein sehr interessantes Ergebnis, denn $F/G=74.9kWh/81.8kWh=0,91 und nahe bei 1! Die Vorlauftemperatur liegt in diesem Beispiel etwa um x Grad über der Innenraumtemperatur, wenn die Ausstentemperatur um x Grad unter der Innenraumtemperatur liegt. Also -10°C Ausstemperatur ergibt +50°C Vorlauftemperatur.

Setzt man zur Vereinfachung F/G~1, schreibt sich Gleichung 9:

$[13]$ $T_{v,m}=(T_{i,m}-T_{a,m})+T_{i,m}=2*T_{i-m}-T_{a,m}$

Real wird die Vorlauftemperaturhöher sein, denn die Temperatur im Heizkreis sinkt ja durch die Abgabe der Energie und erreicht am Ende des Heizkreises die Rücklauftemperatur. Nimmt man eine Differenz (Spreizung) von 10K an, erhöht sich die mittlere Vorlauftemperatur um etwa 5 Grad und die Spalte $T_v$ lässt sich ausfüllen:

| $Monat$	| $T_v$  	| $T_a$  	| $2*T_i-T_a$ | 
|----		|----------	|----------	|----------	|
| Oktober 	| 35,3      |  9,7     	| 30,3     	| 
| November  | 39,7    	|  5,3    	| 34,7    	|
| Dezember  | 42,9    	|  2,1     	| 37,9     	|
| Januar  	| 44,1    	|  0,9     	| 39,1     	|
| Februar  	| 43,5    	|  1,5     	| 38,5     	|
| März  	| 40,4   	|  4,6     	| 35,4     	|
| April  	| 35,8    	|  9,2     	| 30,8     	|
| Mai	  	| 31,8    	| 13,2     	| 26,8    	|

[Tabelle 3]

Diese Tabelle stimmt erstmal optimistisch, befinden sich die Vorlauftemperaturen doch näher an 35 als and 55 Grad.


## Heizkörpergleichung

Eine weitere Ungenauigkeit ist die Annahme, dass Heizkörper ihre Energie proportional zur Temperaturdifferenz $E=G*(T_v-T_i)$ abgeben. Das gilt aber nicht für reale Heizkörper, die eine Energie durch Strahlung und Konvektion an den Raum abgeben. In den Datenblättern der Heizkörper ist zusätzlich ein Exponent n angegeben und die abgegebene Leistung bestimmt bei $T_v=75°C$ $T_i=20°C$ bestimmt sich zu:

$P=P_0*(T/(75-20)K)^n$, wobei n etwa zwischen 1 und 1,5 liegt.

Ein Heizkörper mit der Nennleistung von $P_0=1kW$ gibt daher, bei halber Vorlauftemperaturdifferenz von 55°C/2=27.5°C und einem n=1,3 nur $P=1kW*(27.5/55)^1,3=0,41kW Leistung ab, also weniger als die Hälfte. Entgegen dem linearen Modell aus $[9]$ muss die Vorlauftemperatur also überproportional steigen, wenn es kälter wird.


## Verstärkende Effekte

Wenn die Aussentmperatur sinkt, sinkt nicht nur die Mediumtemperatur (Luft), sondern es muss auch die Vorlauftemperatur entsprechend steigen. Und zwar, wie oben überschlagen, um etwa den gleichen Wert. Das bedeutet, dass ein Abfall von $T_a$ um 1 Grad Celsius einer Temperaturdifferenz von 2 Grad in der Wärmepumpe enstspricht, und somit der COP entsprechend schneller abnimmt. Die Heizkörpergleichung verschlechtert diesen Effekt zusätzlich, und zwar um so stärker, je grösser der Konvektionsanteil bzw. der Exponent n ist.

Plant man darüber hinaus den Einsatz von Photovoltaik, wird die Lage noch schwieriger, denn der Winter zeichnet sich ja eben durch die Abwesenheit von viel Sonne aus. Und in den kalten Nächten ist der PV-Anteil am Strom leider null.

Damit wird die Sache schnell unübersichtlich, weshalb im Folgenden ein eine kleines Programm erstellt wird.

# Simulation

Genauere Berechnungen finden sich hier:

[Simulation](src/heizung.ipynb)


