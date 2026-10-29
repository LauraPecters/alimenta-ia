"""Indicadores de lotes."""
from .produccion import tasa_defectos


def resumen(lotes, producto=None):
    filtrados = [l for l in lotes if producto is None or l.producto == producto]
    if not filtrados:
        return {'lotes': 0, 'producidas': 0, 'defectuosas': 0, 'tasa_global': None}
    total = sum(l.producidas for l in filtrados)
    defectos = sum(l.defectuosas for l in filtrados)
    return {'lotes': len(filtrados), 'producidas': total, 'defectuosas': defectos,
            'tasa_global': tasa_defectos(total, defectos)}
