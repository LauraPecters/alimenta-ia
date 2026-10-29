# Plan de medición

| Ámbito | Fórmula | Fuente | Meta | Responsable |
|---|---|---|---|---|
| Producto / pruebas | Pruebas aprobadas / ejecutadas × 100 | resultado_pytest.txt | 100 % | QA |
| Producto / cobertura RF por pruebas | RF con pruebas automatizadas asociadas / 5 × 100 | Código y pruebas | ≥90 % | QA |
| Proceso / PR revisados | PR aprobados / PR integrados × 100 | GitHub | 100 % | Configuración |
| Proyecto / cumplimiento | Tareas terminadas / comprometidas × 100 | Tablero de tareas | ≥80 % | Líder |
| Producción / tasa defectos | Unidades defectuosas / producidas × 100 | CSV sintético | Observar tendencia | Desarrollo |
| IA / recall | TP / (TP + FN) | Etiquetas sintéticas y predicciones | Reportar límites | IA / QA |

## Resultados verificados

- **Pruebas automatizadas:** 17/17 aprobadas = 100 %.
- **Cobertura de requisitos funcionales:** 5/5 = 100 % con pruebas automatizadas asociadas.
- **Pull Requests creados:** 5, pendientes de revisión y aprobación.
- **PR revisados:** N/D, debido a que todavía no existen integraciones aprobadas.
- **Cumplimiento del proyecto:** N/D, porque aún no se ha establecido un tablero de tareas con compromisos medibles.
- **Lotes sintéticos analizados:** 36.
- **Unidades producidas:** 13.888.
- **Unidades defectuosas:** 407.
- **Tasa global de defectos:** 2,931 %.
- **Recall del detector de IA:** 100 %.
- **Precisión del detector de IA:** 44,44 %.
- **Evaluación de IA:** 4 verdaderos positivos, 0 falsos negativos, 5 falsos positivos y 3 verdaderos negativos.

La cobertura de requisitos representa la existencia de pruebas asociadas a los cinco requisitos funcionales. No equivale a una cobertura del 100 % del código ni garantiza que se hayan evaluado todos los escenarios posibles.

## Análisis de resultados

Los resultados de las pruebas automatizadas muestran una tasa de aprobación del 100 %, lo que indica que los casos evaluados cumplen con los comportamientos esperados.

El prototipo procesó 36 lotes sintéticos y obtuvo una tasa global de defectos del 2,931 %. Este indicador corresponde a la producción alimentaria simulada y no debe confundirse con defectos del software.

El detector de inteligencia artificial obtuvo un recall del 100 %, identificando los cuatro casos atípicos etiquetados. Sin embargo, su precisión del 44,44 % evidencia la presencia de falsas alertas. Por lo tanto, sus resultados deben utilizarse únicamente como apoyo orientativo.

En gestión de configuración, se han creado cinco Pull Requests, pero continúan pendientes las revisiones formales y su integración.

## Acciones pendientes

- Obtener la revisión y aprobación formal de los Pull Requests.
- Integrar los cambios siguiendo el orden de dependencias establecido.
- Definir y medir el cumplimiento de las tareas del proyecto.
- Analizar las falsas alertas del detector de IA.
- Actualizar las evidencias después de integrar los cambios.
- Ejecutar nuevamente las pruebas de regresión.
- Completar la auditoría y decidir sobre la liberación de la versión v1.0.0.