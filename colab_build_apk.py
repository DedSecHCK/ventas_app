# ========================================
# COMPILADOR APK PARA KIVY EN GOOGLE COLAB
# ========================================
# Instrucciones:
# 1. Ir a https://colab.research.google.com/
# 2. Crear nuevo notebook
# 3. Copiar todo este código en una celda
# 4. Ejecutar (botón play)
# 5. Subir mobile.zip cuando lo pida
# 6. Esperar 30-60 minutos
# 7. Descargar APK automáticamente

# PASO 1: Instalar Buildozer
print("📦 Instalando Buildozer...")
!pip install -q buildozer cython

# PASO 2: Instalar dependencias del sistema
print("🔧 Instalando dependencias del sistema...")
!sudo apt-get update -qq
!sudo apt-get install -qq -y openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev build-essential ccache

# PASO 3: Subir proyecto
print("\n📁 Sube tu archivo mobile.zip")
from google.colab import files
import zipfile
import os

uploaded = files.upload()

# Extraer ZIP
for filename in uploaded.keys():
    print(f"Extrayendo {filename}...")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('.')

# PASO 4: Navegar a carpeta mobile
%cd mobile

# PASO 5: Verificar archivos
print("\n📋 Archivos en el proyecto:")
!ls -la

# PASO 6: Limpiar compilaciones anteriores (si existen)
print("\n🧹 Limpiando compilaciones anteriores...")
!rm -rf .buildozer bin

# PASO 7: Compilar APK
print("\n🔨 Compilando APK...")
print("⏰ Esto puede tardar 30-60 minutos en la primera compilación")
print("☕ Ve por un café mientras tanto...")
!buildozer -v android debug

# PASO 8: Verificar y descargar APK
print("\n✅ Compilación completada!")
import glob

apk_files = glob.glob('bin/*.apk')
if apk_files:
    print(f"\n📱 APK generado exitosamente: {apk_files[0]}")
    
    # Mostrar tamaño del APK
    import os
    size_mb = os.path.getsize(apk_files[0]) / (1024 * 1024)
    print(f"📊 Tamaño del APK: {size_mb:.2f} MB")
    
    print("\n⬇️ Descargando APK...")
    files.download(apk_files[0])
    print("\n✅ ¡Listo! APK descargado a tu PC.")
    print("\n📲 Ahora puedes:")
    print("   1. Transferir el APK a tu Samsung A20")
    print("   2. Instalar (habilita 'Orígenes desconocidos' en Configuración)")
    print("   3. ¡Disfrutar tu app!")
else:
    print("\n❌ No se encontró APK.")
    print("Revisa los errores arriba para ver qué salió mal.")
    print("\n🔍 Contenido de la carpeta bin:")
    !ls -la bin/ 2>/dev/null || echo "La carpeta bin no existe"
