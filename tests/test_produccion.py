import pytest
from src.produccion import tasa_defectos, Lote, validar_lote

def test_tasa_normal(): assert tasa_defectos(200,6)==3.0

def test_cero_producidas():
    with pytest.raises(ValueError): tasa_defectos(0,0)

def test_negativos():
    with pytest.raises(ValueError): tasa_defectos(-10,-1)

def test_defectuosas_mayor():
    with pytest.raises(ValueError): tasa_defectos(10,11)

def test_lote_valido():
    l=Lote('L1','2026-10-01','Galletas',100,2,75)
    assert validar_lote(l)==l

def test_codigo_duplicado():
    with pytest.raises(ValueError): validar_lote(Lote('L1','2026-10-01','Galletas',100,2,75),['L1'])

def test_fecha_invalida():
    with pytest.raises(ValueError): validar_lote(Lote('L1','2026-50-01','Galletas',100,2,75))

def test_tipo_cantidad_invalido():
    with pytest.raises(ValueError): tasa_defectos(100.5,3)
