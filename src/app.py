"""Interfaz de consola: registro, historial, indicadores y alertas orientativas."""
import csv
from pathlib import Path
import pandas as pd
from .produccion import Lote, validar_lote, tasa_defectos
from .calidad import resumen
from .detector_ia import detectar

ROOT = Path(__file__).resolve().parents[1]

def cargar_lotes(ruta=ROOT / 'data/lotes_ejemplo.csv'):
    lotes=[]
    with open(ruta, encoding='utf-8', newline='') as f:
        for fila in csv.DictReader(f):
            lote=Lote(fila['codigo'],fila['fecha'],fila['producto'],int(fila['producidas']),
                      int(fila['defectuosas']),float(fila['temperatura']))
            validar_lote(lote,[l.codigo for l in lotes])
            lotes.append(lote)
    return lotes

def guardar_lote(lote, ruta=ROOT/'data/lotes_ejemplo.csv'):
    existentes=cargar_lotes(ruta)
    validar_lote(lote,[l.codigo for l in existentes])
    with open(ruta,'a',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow([lote.codigo,lote.fecha,lote.producto,lote.producidas,lote.defectuosas,lote.temperatura,0])

def mostrar_tablero(lotes):
    print('TABLERO ALIMENTA-IA (datos ficticios)')
    print('Resumen:',resumen(lotes))
    for p in sorted(set(l.producto for l in lotes)):
        print(p, resumen(lotes,p))
    print('Lotes:')
    for l in lotes:
        print(l.codigo,l.producto,f'{tasa_defectos(l.producidas,l.defectuosas):.2f}%',f'{l.temperatura} °C')


def mostrar_alertas(ruta=ROOT/'data/lotes_ejemplo.csv'):
    df=pd.read_csv(ruta)
    df['tasa_defectos']=100*df.defectuosas/df.producidas
    # Entrenamiento y evaluación separados, deterministas y sintéticos.
    train=df.iloc[:24]
    eval_df=df.iloc[24:]
    pred=detectar(train,eval_df)
    print('ALERTAS ORIENTATIVAS - NO sustituyen controles sanitarios')
    for codigo,p in zip(eval_df.codigo,pred):
        print(codigo,'ALERTA' if p else 'sin alerta')

if __name__ == '__main__':
    mostrar_tablero(cargar_lotes())
    mostrar_alertas()
