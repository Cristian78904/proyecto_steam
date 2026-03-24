🧠 Explicación de mi proyecto

En este proyecto desarrollé un análisis de datos aplicando técnicas de Data Science y Machine Learning sobre un dataset de juegos de Steam.

El objetivo principal fue predecir el precio de un videojuego en función de sus valoraciones positivas (ratings), buscando entender si existe una relación entre la popularidad de un juego y su valor en el mercado.

⚙️ ¿Cómo lo desarrollé?

Primero, trabajé con un archivo de datos en formato CSV que contenía información de distintos juegos, como precios y cantidad de valoraciones positivas.

Luego realicé una etapa de limpieza y preparación de datos, donde filtré únicamente los juegos que tenían un precio mayor a cero, para evitar inconsistencias en el análisis.

Después, definí las variables del modelo:

Como variable independiente utilicé la cantidad de ratings positivos
Como variable dependiente, el precio del juego
🤖 Aplicación de Machine Learning

Implementé un modelo de regresión lineal utilizando la librería Scikit-learn.

El modelo fue entrenado con los datos para que pudiera aprender la relación entre la popularidad (ratings) y el precio.

Una vez entrenado, lo utilicé para realizar predicciones, estimando cuánto podría costar un juego en base a diferentes cantidades de valoraciones positivas.

📈 Visualización y análisis

Para validar el comportamiento del modelo, generé gráficos donde:

Se muestran los datos reales
Se visualiza la recta de regresión generada por el modelo

Esto me permitió analizar qué tan bien el modelo se ajusta a los datos y entender la tendencia entre ambas variables.

🎯 Conclusión del proyecto

Este proyecto me permitió aplicar conceptos clave como:

Análisis y limpieza de datos
Modelado predictivo
Uso de librerías de Data Science
Interpretación de resultados

Además, me ayudó a entender cómo el Machine Learning puede utilizarse para resolver problemas reales a partir de datos.
