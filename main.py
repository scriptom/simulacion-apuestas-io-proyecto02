import argparse
import numpy as np
import json
import pandas as pd
from random import random
from datetime import datetime

__timestamp = datetime.now().timestamp()
__default_filebase = f"simulacion-{__timestamp}"
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
                    help="Nombre de archivos personalizados. Si no se especifica, se tomará el timestamp actual",
                    default=__default_filebase)
parser.add_argument('-e', '--estadisticas', action='store_true',
                    help='Especifica si quiere mostrar las estadisticas de ejecución (default: False)', default=False)


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
        apuesta = apuesta if victoria else apuesta * 2 ** derrotas_consecutivas
        num_apuestas = num_apuestas + 1
    return {
        'meta_alcanzada': 'SI' if monto == 100 else 'QUIEBRA',
        'num_apuestas': num_apuestas,
        'jugadas': jugadas
    }


def exportar_excel(resultados: list[dict], filename: str) -> str:
    dataset = []
    for index, corrida in enumerate(resultados):
        for jugada in corrida['jugadas']:
            dataset.append((index + 1, jugada['monto_antes'], jugada['apuesta'], jugada['rand'],
                            'sí' if jugada['victoria'] else 'no', jugada['nuevo_monto'], corrida['meta_alcanzada']))
    cols = [
        'Número de corrida',
        'Cantidad antes de jugar',
        'Apuesta',
        'Número aleatorio',
        '¿Se ganó el juego?',
        'Cantidad luego de jugar',
        '¿Se llegó a la meta?'
    ]
    df = pd.DataFrame(dataset, columns=cols)
    df.to_excel(xlsx_file := f'{filename}.xlsx', index=False)
    return xlsx_file


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
    filename = args.filename
    with open(json_file := f"{filename}.json", 'w') as f:
        json.dump(corridas, f, indent=4)
    print(f'Resultados de simulación guardados en "{json_file}"')
    if args.estadisticas:
        victorias: int = np.count_nonzero([1 if corrida['meta_alcanzada'] == 'SI' else 0 for corrida in corridas])
        avg: float = victorias / c
        print(f"Probabilidad porcentual de llegar a la meta: {avg:.0%}")
        ganancia: float = 100 * avg - m
        print(f"Ganancia esperada: {ganancia:.2g}u.m.")
        xlsx_file = exportar_excel(corridas, filename)
        print(f'Cuadro de excel guardado en "{xlsx_file}"')
