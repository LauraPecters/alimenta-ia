# Plan de medición

| Ámbito | Fórmula | Fuente | Meta | Responsable |
|---|---|---|---|---|
| Producto / pruebas | aprobadas / ejecutadas × 100 | resultado_pytest.txt | 100 % | QA |
| Producto / cobertura RF por pruebas | RF con prueba automatizada directa / 5 × 100 | código y pruebas | ≥90 % | QA |
| Proceso / PR revisados | PR aprobados / PR integrados × 100 | GitHub | 100 % | Configuración |
| Proyecto / cumplimiento | tareas terminadas / comprometidas × 100 | tablero de tareas | ≥80 % | Líder |
| Producción / tasa defectos | unidades defectuosas / producidas × 100 | CSV sintético | observar tendencia | Desarrollo |
| IA / recall | TP / (TP + FN) | etiquetas sintéticas y predicciones | reportar límites | IA / QA |

**Resultados verificados:** 12/12 pruebas = 100 %. Cobertura estricta de RF con prueba automatizada directa: 3/5 = 60 % (RF-01, RF-02, RF-03; RF-04/RF-05 tienen verificación funcional/manual o prueba técnica parcial, no aceptación integral automatizada). PR revisados: N/D (sin PR). Proyecto cumplimiento: N/D (sin tablero). Producción tasa global = 2.931 % en 36 lotes ficticios. IA evaluación: TP=4, FN=0, FP=5, TN=3, recall=100 %; precisión=44.44 %, resultados no extrapolables a datos reales.

**Acciones:** agregar pruebas de aceptación para tablero y advertencias de IA; crear y revisar PR reales; definir tablero de tareas; revisar umbral/variables de IA para disminuir falsos positivos.
