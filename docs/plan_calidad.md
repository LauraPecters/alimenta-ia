# Plan de calidad

**Objetivo:** prevenir registros erróneos, integrar cambios trazables y evaluar críticamente alertas IA.

| Objetivo de calidad | Control preventivo | Prueba o evidencia | Responsable | Criterio de aceptación |
|---|---|---|---|---|
| Evitar registros inválidos | Validación de tipo, rango, fecha y unicidad | pytest en `tests/test_produccion.py` | Desarrollo / QA | Todos los casos obligatorios aprobados |
| Asegurar cambios trazables | Convenciones, revisión de PR asociadas a issue | enlaces de issue/PR y commit | Configuración / QA | 100 % de PR integrados revisados; pendiente GitHub |
| Detectar fallas de IA | Entrenamiento/evaluación separados, semilla fija, etiquetas simuladas | CSV de predicciones, TP/FN/FP, recall | IA / QA | Reportar desempeño y límites sin declarar seguridad sanitaria |

**Criterio de salida:** cero defectos críticos abiertos, pruebas obligatorias aprobadas, revisión de PR comprobada. La entrega actual **no cumple** el último criterio (sin PR reales), por lo que no se autoriza release verificado v1.0.0.
