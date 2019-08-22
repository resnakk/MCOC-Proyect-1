# MCOC-Proyecto-1 

Introducción
==============
Este proyecto se trata del estudio sobre la difusion de calor al interio de una probeta de hormigón de 1 metro cúbico, para lo que se desarrollará un modelo tri-dimensional que busca predecir las temperaturas producidas por la hidratacion del hormigón.

Integrantes:
==============
```
	Tomás García
	Rodrigo Molina
	Javier Marín
	Mauricio Sánchez
```
Referencias:
==============
1.- Para el estudio de la comportación de la temperatura ambiente a traves del tiempo se utilizó la fórmula:
```
	T = A*sin(2*pi*(t - b1)/(2*b2) + B)

	A = (Tmax - Tmin)/2
	B = (Tmax + Tmin)/2
	b1 = (hmax + hmin)/2
	b2 = (hmax - hmin)

	Tmax: Temperatura maxima en el dia
	Tmin: Temperatura minima en el dia
	hmax: Hora en que se alcanza la temperatura
	hmin: Hora en la que se alcanza la temperatura minima 
```
La cual fue obtenida de Propuesta metodlógica par la optimización de cemento: 
https://tdx.cat/bitstream/handle/10803/6163/08Jaol08de15.pdf?sequence=8&isAllowed=y

2.- Para la obtención de las temeraturas extremas, se extrajo informacion de AccuWeather, especificamente del lunes 10 de diciembre del 2018. Sin embargo no esta la información sobre a que hora se alcanzas enstas temperaturas, por lo que se asumio un hmax = 15:00, hmin = 05:00.
(https://www.accuweather.com/es/cl/san-carlos/57580/december-weather/57580?monyr=12/1/2018&view=table)

