# Programa del curso — Analítica de Datos (Aprendizaje de máquina)

> Contenido tomado de la ficha oficial de la asignatura (código 4200729, Universidad Nacional de Colombia — Sede Manizales) y del material de introducción del curso. Los campos marcados como *(completar)* o "por confirmar" deben ajustarse con la información específica del periodo 2026-II.

## Información general

| Campo | Detalle |
|---|---|
| Código | 4200729 |
| Nombre de la asignatura | Analítica de datos (Aprendizaje de máquina) |
| Docente | Diego Fabián Collazos Huertas |
| Correo | dfcollazosh@unal.edu.co |
| Sede | Manizales |
| Facultad | Ingeniería y Arquitectura |
| Unidad académica | Departamento de Ingeniería Eléctrica, Electrónica y Computación — Manizales |
| Nivel | Pregrado |
| Créditos | 4 (HAP = 4 h/semana, HAI = 6 h/semana, 16 semanas) |
| Horario | Lunes 9:00 a.m.–11:00 a.m. y Miércoles 2:00 p.m.–4:00 p.m. *(confirmar para 2026-II)* |
| Modalidad | Presencial |
| Planes asociados | 4028 — Ingeniería Electrónica (también cursada por estudiantes de otros planes como libre elección) |
| Prerrequisitos | Técnicas de programación; Probabilidad y estadística |
| Tipología | Asignatura de libre elección — Componente disciplinar |
| Asistencia mínima | 85% (según ficha oficial; el material de inducción del curso menciona 80% — verificar el porcentaje vigente) |

## Descripción

El curso Analítica de datos pretende estudiar los métodos y herramientas básicas relacionadas con aprendizaje estadístico orientadas a la extracción de información relevante desde datos.

**Objetivo general:** introducir los conceptos básicos relacionados con aprendizaje estadístico orientados a la extracción de información relevante sobre bases de datos.

## Objetivos de aprendizaje

- Estimular el espíritu crítico y generar actitudes ético-científicas dentro de las cuales se orienta el plan de estudios.
- Comprender los conceptos principales relacionados con esquemas lineales y no lineales de aprendizaje supervisado y no supervisado.
- Desarrollar competencias de aprendizaje autónomo en aras de adaptarse a las necesidades del medio, en concordancia con el continuo cambio tecnológico y científico en el área de la ingeniería.
- Leer y comprender una segunda lengua de influencia científica, posibilitando la asimilación de literatura técnica en otro idioma relacionada con el área de conocimiento.
- Aplicar algoritmos de analítica de datos utilizando herramientas de software para la extracción y visualización de información relevante.

## Conceptos previos necesarios

Cálculo diferencial, cálculo integral, álgebra lineal, programación, y probabilidad y estadística.

## Metodología

Clases magistrales acompañadas de simulaciones en **Orange Data Mining** y **Python** sobre cada una de las temáticas del curso (60% contenido teórico / 40% contenido práctico). Se complementa con talleres y un proyecto integrador, promoviendo la participación de los estudiantes mediante discusiones académicas y consultas.

## Evaluación

| Componente | Peso | Entregas proyecto integrador |
|---|---|---|
| Laboratorios de simulación | 45% | Entrega 1: semana 6 · Entrega 2: semana 15 |
| Proyecto integrador | 45% | Idea del proyecto: semana 8 · Presentación final: semana 16 |
| Asistencia | 10% | Mínimo 85% de asistencia (ver [`asistencia/`](asistencia/)) |

**Proyecto integrador:** aplicación integral de las técnicas y conocimientos del curso en la solución de un problema real de analítica de datos. Puede desarrollarse en grupos de hasta 3 personas, con datos reales (propios de empresas, negocios o proyectos de los estudiantes, bajo acuerdo de confidencialidad si aplica) o artificiales.

## Contenidos básicos

1. **Introducción a la analítica de datos** — conceptos clave de ciencia de datos; introducción al manejo de Orange Data Mining; repaso de manejo de datos en Python.
2. **Transformación y visualización de datos** — transformación de variables; preproceso de datos; visualización de datos.
3. **Modelado y evaluación de enfoques no supervisados** — conceptos básicos de correlación; selección y extracción de características; algoritmos de reducción de dimensión; principios de agrupamiento de datos.
4. **Modelado y evaluación de enfoques supervisados** — modelos de predicción (clasificación y regresión); evaluación de modelos; clasificadores clásicos (KNN, árboles de decisión, random forest, SVMs, regresión logística); regresión lineal y ensemble learning.
5. **Redes neuronales artificiales y Deep Learning** — redes neuronales artificiales; introducción al deep learning (CNNs).
6. **Herramientas de análisis de datos** — herramientas para la implementación de EDA; herramientas web de visión por computador; manejo de GitHub y Streamlit.

## Cronograma

> Cronograma tentativo de 16 semanas construido a partir de los contenidos básicos oficiales. Completa la columna **Fecha** con el calendario académico real de 2026-II.

| Semana | Fecha | Tema | Entregable |
|---|---|---|---|
| 1 | | Introducción a la analítica de datos; bases de datos y tipos de variables | — |
| 2 | | Introducción a Orange Data Mining; repaso de manejo de datos en Python | — |
| 3 | | Transformación de variables; preproceso de datos | — |
| 4 | | Visualización de datos | — |
| 5 | | Correlación, selección y extracción de características | — |
| 6 | | Reducción de dimensión; agrupamiento de datos | Laboratorios de simulación — Entrega 1 |
| 7 | | Aprendizaje supervisado: modelos de predicción, métricas y validación, KNN | — |
| 8 | | Árboles de decisión y SVMs | Proyecto integrador — idea |
| 9 | | Regresión logística y redes neuronales | — |
| 10 | | Random Forest; ensemble learning (boosting y bagging) | — |
| 11 | | Regresión lineal; métricas de evaluación | — |
| 12 | | Redes neuronales artificiales | — |
| 13 | | Introducción al deep learning (CNNs) | — |
| 14 | | Herramientas para la implementación de EDA | — |
| 15 | | Herramientas web de visión por computador; manejo de GitHub y Streamlit | Laboratorios de simulación — Entrega 2 |
| 16 | | Presentación final del proyecto integrador | Proyecto integrador — Entrega 2 |

> Puedes editar esta tabla directamente desde GitHub (botón de lápiz ✏️ en la esquina superior derecha del archivo) sin necesidad de clonar el repositorio.

## Bibliografía básica

- Géron, A. *Hands-On Machine Learning with Scikit-Learn and TensorFlow*. O'Reilly Media, 2019.
- Goodfellow, I. *Deep Learning*. MIT Press, 2016.
- Bishop, C. *Pattern Recognition and Machine Learning*. Springer, 2006.
- Scholkopf, B. *Learning with Kernels*. MIT Press, 2001.
- Príncipe, J. *Information Theoretic Learning*. Springer, 2010.
- Kay, S. *Fundamentals of Statistical Signal Processing: Detection Theory*. Prentice Hall, 1993.

## Recursos y materiales

Los materiales de cada sesión se organizarán en carpetas por semana o módulo dentro de este repositorio (por ejemplo `semana-01/`, `semana-02/`, ...).

## Asistencia

El registro de asistencia se administra en la carpeta [`asistencia/`](asistencia/). 👉 [Abrir la página de asistencia](https://diegocollazos.github.io/CursoAnaliticaDatos_/asistencia/asistencia.html) — ver [`asistencia/README.md`](asistencia/README.md) para más detalles.
