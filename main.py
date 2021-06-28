import json
from random import random
from datetime import datetime
import win32com.client as win32

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

def generarExcel(nombre_archivo: str):
    json_data = json.loads(open(nombre_archivo).read())
    rows = []
    numero_corrida = 1
    for record in json_data:
        jugadas = record['jugadas']
        for jugada in jugadas:
            cant_antes_jugar = jugada['monto_antes']
            apuesta = jugada['apuesta']
            numero_aleatorio = jugada['rand']
            victoria = 'si' if (jugada['victoria'] == True) else 'no'
            cant_luego_jugar = jugada['nuevo_monto']
            meta = record['meta_alcanzada']
            rows.append([numero_corrida, cant_antes_jugar, apuesta, numero_aleatorio, victoria, cant_luego_jugar, meta])
        numero_corrida +=1

    excel_app = win32.Dispatch('Excel.Application')
    excel_app.visible = True

    workbook = excel_app.Workbooks.Add()
    worksheet = workbook.Worksheets(1)

    etiquetas_columnas = ('Número de corrida', 'Cantidad antes de jugar', 'Apuesta', 'Número aleatorio', '¿Se ganó el juego?', 'Cantidad luego de jugar', '¿Se llegó a la meta?')

    for indice, value in enumerate(etiquetas_columnas):
        worksheet.Cells(1, indice + 1).Value = value

    row_tracker = 2
    tamaño_columna = len(etiquetas_columnas)

    for row in rows:
        worksheet.Range(
            worksheet.Cells(row_tracker, 1),
            worksheet.Cells(row_tracker, tamaño_columna)
        ).Value = row
        row_tracker += 1


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
    generarExcel(filename)
