# Simulador de apuestas

Sencillo proyecto de simulador de apuestas desarrollado para el Proyecto Práctico 02 de la materia Investigación de Operaciones de la UCAB.

## Enunciado

> Un juego consiste en duplicar la apuesta cada vez que se pierda o se gane. Si se apuesta X unidades 
monetarias (u.m.) y se pierde, entonces, se apuesta 2X u.m.; si se vuelve a perder, entonces se apuesta 4X 
u.m. y así sucesivamente. Sin embargo, si al seguir esta política la apuesta es mayor que la cantidad que se 
dispone, entonces, se apuesta lo que se tiene disponible. Por otro lado, cada vez que se gane, la apuesta será 
de 2X u.m y asi sucesivamente. Si la cantidad inicial disponible es de 60 u.m., la apuesta es de 10 u.m., la 
ganancia es igual a la cantidad apostada, la probabilidad de ganar es de 0.5 y se quiere tener 100 u.m. Si se 
llega a obtener una cantidad mayor solo se reconocerán 100 u.m. , ¿cuál es la probabilidad porcentual de 
llegar a la meta?, ¿cuál es la ganancia esperada?. Realice 50 corridas.

## Instalacion

- Clonar el repositorio

`git clone https://github.com/scriptom/simulacion-apuestas-io-proyecto02`

- Instalar dependencias

`pip install -r requirements.txt`

- Ejecutar

`python main.py`

El programa le pedirá datos como el monto inicial, la apuesta y el numero de corridas a ejecutar. Finalmente, guardará los resultados en un archivo JSON con el timestamp.