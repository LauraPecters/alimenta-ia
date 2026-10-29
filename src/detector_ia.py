"""Detector educativo no apto para decisiones de inocuidad alimentaria."""
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

SEMILLA = 42

def detectar(train, evaluacion, contaminacion=0.15):
    columnas = ['temperatura', 'tasa_defectos']
    escalador = StandardScaler()
    x_train = escalador.fit_transform(train[columnas].to_numpy(dtype=float))
    x_eval = escalador.transform(evaluacion[columnas].to_numpy(dtype=float))
    modelo = IsolationForest(n_estimators=100, contamination=contaminacion, random_state=SEMILLA)
    modelo.fit(x_train)
    etiquetas = modelo.predict(x_eval)
    return (etiquetas == -1).astype(int)
