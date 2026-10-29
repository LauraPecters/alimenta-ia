import csv

import pytest

from src.app import cargar_lotes, guardar_lote, mostrar_tablero
from src.produccion import Lote


def test_cargar_lotes(tmp_path):
    ruta = tmp_path / "lotes.csv"
    ruta.write_text(
        "codigo,fecha,producto,producidas,defectuosas,temperatura,anomalia\n"
        "L-001,2026-10-01,Pan,100,5,72.0,0\n",
        encoding="utf-8"
    )

    lotes = cargar_lotes(ruta)

    assert len(lotes) == 1
    assert lotes[0].codigo == "L-001"
    assert lotes[0].producto == "Pan"


def test_guardar_lote(tmp_path):
    ruta = tmp_path / "lotes.csv"
    ruta.write_text(
        "codigo,fecha,producto,producidas,defectuosas,temperatura,anomalia\n",
        encoding="utf-8"
    )

    lote = Lote("L-002", "2026-10-02", "Pan", 200, 6, 73.0)

    guardar_lote(lote, ruta)

    lotes = cargar_lotes(ruta)

    assert len(lotes) == 1
    assert lotes[0].codigo == "L-002"
    assert lotes[0].defectuosas == 6


def test_rechazar_lote_duplicado(tmp_path):
    ruta = tmp_path / "lotes.csv"
    ruta.write_text(
        "codigo,fecha,producto,producidas,defectuosas,temperatura,anomalia\n"
        "L-001,2026-10-01,Pan,100,5,72.0,0\n",
        encoding="utf-8"
    )

    lote = Lote("L-001", "2026-10-02", "Pan", 200, 6, 73.0)

    with pytest.raises(ValueError):
        guardar_lote(lote, ruta)


def test_mostrar_tablero(capsys):
    lotes = [
        Lote("L-001", "2026-10-01", "Pan", 100, 4, 72.0),
        Lote("L-002", "2026-10-02", "Galletas", 100, 2, 73.0)
    ]

    mostrar_tablero(lotes)

    salida = capsys.readouterr().out

    assert "TABLERO ALIMENTA-IA" in salida
    assert "Pan" in salida
    assert "Galletas" in salida
    assert "L-001" in salida
    assert "L-002" in salida