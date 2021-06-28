import argparse
import json
from random import random
from datetime import datetime

parser = argparse.ArgumentParser(
    description="Simula un juego de apuestas dado un monto inicial, una apuesta inicial y el numero de corridas a realizar")
parser.add_argument('-m', '--monto-inicial', help='Monto inicial para empezar cada corrida. Default: 60',
                    metavar='MONTO',
                    default=60)
parser.add_argument('-a', '--apuesta-inicial', help='Apuesta inicial para empezar cada corrida. Default: 10',
                    metavar='APUESTA', default=10)
parser.add_argument('-n', '--numero-corridas', help="Número de corridas a utilizar. Default: 50",
                    metavar='num_corridas', default=50)
parser.add_argument('-i', '--interactivo',
                    help="Ejecuta el programa en modo interactivo. NOTA: Esta opción ignorará los parámetros ingresados por CLI",
                    action='store_true', default=False)
parser.add_argument('-f', '--filename',
                    help="Nombre de archivo personalizado. Si no se especifica, se tomará el timestamp actual",
                    default=f'simulacion-{datetime.now().timestamp()}.json')


def jugar(monto_inicial: int, apuesta_inicial: int) -> dict:
    monto: int = monto_inicial
    apuesta: int = apuesta_inicial
    jugadas: list = []
    derrotas_consecutivas: int = 0
    num_apuestas: int = 0
    while 0 < monto < 100:
        jugadas.append({
            'monto_antes': monto,
            'apuesta': (apuesta := min(apuesta, monto)),
            'rand': (rand := random()),
            'victoria': (victoria := rand < 0.5),
            'nuevo_monto': (monto := min(100, monto + apuesta) if victoria else max(monto - apuesta, 0))
        })
        derrotas_consecutivas = 0 if victoria else derrotas_consecutivas + 1
        apuesta = apuesta * 2 if victoria else apuesta * 2 ** derrotas_consecutivas
        num_apuestas = num_apuestas + 1
    return {
        'meta_alcanzada': 'SI' if monto == 100 else 'QUIEBRA',
        'num_apuestas': num_apuestas,
        'jugadas': jugadas
    }


if __name__ == "__main__":
    args = parser.parse_args()
    if args.interactivo:
        m = int(input("Ingrese monto inicial: "))
        a = int(input("Ingrese apuesta inicial: "))
        c = int(input("Ingrese num corridas: "))
    else:
        m = int(args.monto_inicial)
        a = int(args.apuesta_inicial)
        c = int(args.numero_corridas)
    corridas = []
    for i in range(c):
        corridas.append(jugar(m, a))
    with open(filename := args.filename, 'w') as f:
        json.dump(corridas, f, indent=4)
    print(f'Resultados de simulación guardados en "{filename}"')
