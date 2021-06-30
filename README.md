# Simulador de apuestas

Sencillo proyecto de simulador de apuestas desarrollado para el Proyecto Práctico 02 de la materia Investigación de Operaciones de la UCAB.

## Enunciado

> Un juego consiste en duplicar la apuesta cada vez que se pierde. Si se apuesta X 
unidades monetarias (u.m.) y se pierde, entonces, se apuesta 2X u.m.; si se vuelve a 
perder, entonces se apuesta 4X u.m. y así sucesivamente. Sin embargo, si al seguir 
esta política la apuesta es mayor que la cantidad que se dispone, entonces, se apuesta 
lo que se tiene disponible. Por otro lado, cada vez que se gane, la apuesta será de X 
u.m. Si la cantidad inicial disponible es de 60 u.m., la apuesta es de 10 u.m., la 
ganancia es igual a la cantidad apostada, la probabilidad de ganar es de 0.5 y se 
quiere tener 100 u.m. Si se llega a obtener una cantidad mayor solo se reconocerán 
100 u.m., ¿cuál es la probabilidad porcentual de llegar a la meta?, ¿cuál es la ganancia 
esperada?. Realice 50 corridas.

## Instalacion

- Clonar el repositorio

`git clone https://github.com/scriptom/simulacion-apuestas-io-proyecto02`


- Uso del programa

```
usage: python main.py [-h] [-m MONTO] [-a APUESTA] [-n num_corridas] [-i] [-f FILENAME]
optional arguments:
  -h, --help            show this help message and exit
  -m MONTO, --monto-inicial MONTO
                        Monto inicial para empezar cada corrida. Default: 60
  -a APUESTA, --apuesta-inicial APUESTA
                        Apuesta inicial para empezar cada corrida. Default: 10
  -n num_corridas, --numero-corridas num_corridas
                        Número de corridas a utilizar. Default: 50
  -i, --interactivo     Ejecuta el programa en modo interactivo. NOTA: Esta opción ignorará los parámetros ingresados por CLI
  -f FILENAME, --filename FILENAME
                        Nombre de archivo personalizado. Si no se especifica, se tomará el timestamp actual
```

