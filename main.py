import json
from random import random
from datetime import datetime


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
    m = int(input("Ingrese monto inicial: "))
    a = int(input("Ingrese apuesta inicial: "))
    c = int(input("Ingrese num corridas: "))
    corridas = []
    for i in range(c):
        corridas.append(jugar(m, a))
    with open(filename := f'simulacion-{datetime.now().timestamp()}.json', 'w') as f:
        json.dump(corridas, f, indent=4)
    print(f'Resultados de simulación guardados en "{filename}"')
