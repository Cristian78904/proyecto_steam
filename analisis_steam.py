# VERSIÓN SIMPLIFICADA - PRUEBA RÁPIDA
import pandas as pd
import matplotlib.pyplot as plt
import os

print(" EJECUTANDO PRUEBA RÁPIDA...")
print("===============================")

# Verificar archivos en la carpeta
print("📁 Archivos en tu carpeta:")
archivos = os.listdir('.')
for archivo in archivos:
    print(f"   - {archivo}")

# Si no hay steam.csv, crear datos de ejemplo
if 'steam.csv' not in archivos:
    print("\n📊 CREANDO DATOS DE EJEMPLO...")
    
    # Crear un dataset pequeño de ejemplo
    datos_ejemplo = {
        'name': ['Game A', 'Game B', 'Game C', 'Game D', 'Game E'],
        'price': [0, 9.99, 19.99, 59.99, 4.99],
        'genre': ['Action', 'RPG', 'Strategy', 'Action', 'Indie']
    }
    
    df = pd.DataFrame(datos_ejemplo)
    print("✅ Datos de ejemplo creados!")
    
else:
    # Cargar el archivo real
    df = pd.read_csv('steam.csv')
    print("✅ steam.csv cargado correctamente!")

# Análisis básico
print(f"\n📈 TOTAL DE JUEGOS: {len(df)}")
print(f"💰 PRECIO PROMEDIO: ${df['price'].mean():.2f}")
print(f"🎁 JUEGOS GRATIS: {len(df[df['price'] == 0])}")

# Gráfico simple
plt.figure(figsize=(10, 5))
df['price'].hist(bins=20, color='lightblue', edgecolor='black')
plt.title('ANÁLISIS DE PRECIOS - PROYECTO ')
plt.xlabel('Precio ($)')
plt.ylabel('Cantidad de Juegos')
plt.grid(True, alpha=0.3)

# Guardar y mostrar
plt.savefig('mi_primero_analisis.png', dpi=150)
plt.show()

print("\n🎉 ¡PRIMER ANÁLISIS COMPLETADO!")
print("📸 Gráfico guardado como: 'mi_primero_analisis.png'")