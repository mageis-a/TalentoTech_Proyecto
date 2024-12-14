# LiftCare: Predicción de mantenimientos de montacargas en la empresa XYZ.SA

Proyecto - TalentoTech 2024
El proyecto fue realizado en el Bootcamp de Talento Tech en la U de A.


## Descripción

En la empresa se llevan registros de mantenimiento de montacargas, sin embargo, se desea predecir los mantenimientos, para realizar planes de acción y tomar decisiones que permitan impactar lo menos posile la operación y evitar que las montacargas lleguen al taller por averías.


## Etapas del Proyecto

**Recolección de Datos:** Se recopilaron los datos de reportes de mantenimientos de montacargas y se cargan desde un archivo de excel

**Análisis Exploratorio:** Se analizó la información para entender el reporte y entender cada uno de los terminos de los campos, por ejemplo el tipo de máquina, los tipos de intervención, que es una avería, un defecto, plan de acción etc, se hace limpieza de datos, se estandariza la información y se impugnan datos faltantes, para el modelado.

**Desarrollo del Modelo:** Se utilizaron algoritmos de aprendizaje automático, para la creación del modelo que predice el mantenimiento.

**Validación y Evaluación:** Se evaluó el modelo con métricas, para garantizar la precisión y confiabilidad.

**Implementación:** Se realizó una interfaz que permite utilizando el modelo predecir el tipo de mantenimiento.


## Estructura del proyecto

Proyecto_Mantenimiento.ipynb: Notebook con el análisis de datos y el modelo predictivo.
REPORTE MANTENIMIENTO.xlsx: Archivo de datos en Excel con información de los mantenimientos de las montacargas (no incluido en el repositorio por confidencialidad).
README.md: Este archivo README.


## Requisitos

El proyecto requiere las siguientes bibliotecas de Python:

* numpy
* pandas
* matplotlib
* seaborn
* scikit-learn
* pickle

**Pandas:** Biblioteca de Python diseñada que trabaja con datos tabulares, es decir, datos organizados en filas y columnas, Proporciona estructuras de datos como DataFrames, facilita la manipulación y análisis de datos.

**NumPy:** Biblioteca que proporciona soporte para arreglos multidimensionales y funciones matemáticas de alto rendimiento. Utilizada en la ciencia de datos, análisis numérico y computación científica.

**Matplotlib:** Biblioteca de Python que crea visualizaciones estáticas, animadas e interactivas en Python. Es utilizada en la ciencia de datos, análisis de datos y visualización. Se usa para representar datos numéricos en forma gráfica.

**Seaborn:** Biblioteca de visualización de datos con interfaz de alto nivel para crear gráficos estadísticos, simplifica la creación de gráficos complejos, incluyendo temas y paletas de colores que mejoran la estética de las visualizaciones.

**Sklearn:** Las librerías de Scikit-learn en Google Colab ofrecen herramientas clave para el aprendizaje automático: train_test_split divide los datos en conjuntos de entrenamiento y prueba; KFold y cross_val_score facilitan la validación cruzada; los clasificadores MultinomialNB, GaussianNB y BernoulliNB implementan Naive Bayes; funciones como classification_report y accuracy_score evalúan el rendimiento del modelo; KNNImputer imputa valores faltantes usando K-Nearest Neighbors, y RobustScaler normaliza características de manera robusta frente a outliers.

**SodaPy:** La biblioteca permite interactuar con la API de datos abiertos de Socrata. Facilita la consulta y obtención de conjuntos de datos públicos en formatos como JSON o CSV, lo que es útil en Google Colab para analizar datos de interés público sin necesidad de descargarlos manualmente.

**Pickle:** Se utiliza en Google Colab, permite serializar y deserializar objetos de Python. Esto es para guardar modelos de aprendizaje automático y estructuras de datos en archivos, facilitando su almacenamiento y carga posterior sin necesidad de regenerarlos, optimizando así el tiempo y los recursos en proyectos de análisis y machine learning.


## Instalación

1. Clona el repositorio:
2. Git clone https://github.com/tu_usuario/tu_repositorio.git
3. Navega al directorio del proyecto:
cd tu_repositorio
4. Instala las dependencias:
5. pip install -r requirements.txt


## Utilización

1. Abre el notebook Proyecto_Mantenimiento.ipynb
2. Ejecuta las celdas secuencialmente para:
    - Cargar y explorar el conjunto de datos.
    - Entrenar el modelo.
    - Evaluar el modelo


# Instrucciones para Despliegue y Utilización

Se indica como desplegar y utilizar la aplicación paso a paso

1. Crear el entorno virtual
Haz clic derecho en la carpeta del proyecto y selecciona Abrir terminal.
Instalar las librerias
Flask
pandas
sklearn

2. Activar el Entorno Virtual
Ejecuta el siguiente comando para activar el entorno virtual:

.\source\Scripts\Activate
 python app.py

3. Activar Python
Una vez que el entorno esté activo, validar que Python esté funcionando.

 python --version

4. Abrir el Navegador
Copiar la direccion ip y pegarla en el navegador de preferencia.

 http://127.0.0.1:5000

5. Interacción con la Aplicación
icon24.png

En la aplicación siga los siguientes pasos:

1️⃣ Agregar la máquina

Ingresa la fecha 
2️⃣ Seleccionar Fecha

Elige técnico desplegable.
3️⃣ Seleccionar Técnico

Selecciona el xxx
4️⃣ Enviar

Clic en el botón de Enviar para procesar la información.


## Autores

* Milena Arboleda
* Juan David Montoya
* Maryory López
* Ferney Pinzón

"# TalentoTech_Proyecto" 
