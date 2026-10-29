"""Registro y validacion de lotes con datos sinteticos."""
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Lote:
    codigo: str
    fecha: str
    producto: str
    producidas: int
    defectuosas: int
    temperatura: float


def tasa_defectos(producidas: int, defectuosas: int) -> float:
    if type(producidas) is not int or type(defectuosas) is not int:
        raise ValueError('Las cantidades deben ser enteras')
    if producidas <= 0 or defectuosas < 0 or defectuosas > producidas:
        raise ValueError('Cantidades invalidas')
    return 100 * defectuosas / producidas


def validar_lote(lote: Lote, codigos_existentes=()) -> Lote:
    if not lote.codigo.strip() or lote.codigo in codigos_existentes:
        raise ValueError('Codigo vacio o duplicado')
    date.fromisoformat(lote.fecha)
    if not lote.producto.strip():
        raise ValueError('Producto vacio')
    if not isinstance(lote.temperatura, (int,float)) or not -30 <= lote.temperatura <= 200:
        raise ValueError('Temperatura no valida')
    tasa_defectos(lote.producidas, lote.defectuosas)
    return lote
