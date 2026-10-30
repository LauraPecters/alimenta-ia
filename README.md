\# ALIMENTA-IA — Taller educativo



Prototipo académico desarrollado con \*\*datos sintéticos\*\* para el registro de lotes alimentarios, cálculo de tasas de defectos, consulta por producto, tablero de indicadores e identificación de anomalías mediante inteligencia artificial.



Proyecto de Administración de Proyectos de Software.



\## Ejecución



Requisitos: Python 3.12 y las dependencias declaradas en `requirements.txt`.



Instalar dependencias:



```bash

python -m pip install -r requirements.txt

```



Ejecutar las pruebas:



```bash

python -m pytest -q

```



Ejecutar el prototipo:



```bash

python -m src.app

```



Para registrar un lote desde Python se puede utilizar `guardar\_lote()` junto con la clase `Lote`, importadas desde los módulos correspondientes.



El sistema valida identificadores únicos, fechas, cantidades y temperaturas. El tablero presenta indicadores y permite consultar resúmenes filtrados por producto.



\## Resultados verificados



\- 36 lotes sintéticos.

\- 13.888 unidades producidas.

\- 407 unidades defectuosas.

\- Tasa global de defectos: 2,931 %.

\- 17 pruebas automatizadas aprobadas de 17 ejecutadas.

\- Cinco requisitos funcionales con pruebas automatizadas asociadas.



\### Inteligencia artificial



Detector implementado mediante IsolationForest.



\- Entrenamiento: 24 lotes sintéticos.

\- Evaluación: 12 lotes sintéticos.

\- Semilla aleatoria: 42.

\- Recall: 100 %.

\- Precisión: 44,44 %.

\- Falsos positivos: 5.



Las alertas son exclusivamente orientativas y no sustituyen controles de inocuidad alimentaria, evaluaciones de laboratorio ni decisiones de profesionales responsables.



\## Gestión de configuración en GitHub



Repositorio: https://github.com/LauraPecters/alimenta-ia



Se gestionaron los cambios mediante Issues, ramas, commits y Pull Requests.



Pull Requests revisados y fusionados:



\- PR #2: Registro y validación de lotes.

\- PR #4: Indicadores de producción y calidad.

\- PR #6: Detector de anomalías con IA.

\- PR #7: Aplicación integrada.

\- PR #8: Pruebas y evidencias.

\- PR #9: Integración final en `main`.



Las revisiones fueron realizadas por el colaborador JcepedaM.



\*\*Estado:\*\* código y evidencias integrados en `main`, con 17 pruebas aprobadas. Liberación académica `v1.0.0` pendiente de verificación final y etiquetado.



\## Estructura del proyecto



\- `src/`: código fuente.

\- `tests/`: pruebas automatizadas.

\- `data/`: datos sintéticos.

\- `docs/`: documentación de requisitos, calidad, medición y configuración.

\- `evidencias/`: resultados de pruebas, indicadores y evaluación de IA.



\## Limitaciones



ALIMENTA-IA es un prototipo académico. Sus datos, etiquetas y resultados son ficticios; no debe utilizarse como sistema industrial de control sanitario.

