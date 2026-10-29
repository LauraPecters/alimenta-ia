from src.produccion import Lote
from src.calidad import resumen

def test_resumen():
    ls=[Lote('A','2026-10-01','Pan',100,4,70),Lote('B','2026-10-02','Pan',300,8,72)]
    assert resumen(ls)['tasa_global']==3.0

def test_filtro():
    ls=[Lote('A','2026-10-01','Pan',100,4,70),Lote('B','2026-10-02','Galleta',100,1,72)]
    assert resumen(ls,'Pan')['lotes']==1

def test_vacio(): assert resumen([])['tasa_global'] is None
