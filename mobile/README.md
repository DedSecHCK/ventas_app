# Ventas App - Aplicación Móvil de Gestión

Aplicación móvil para gestión de ventas, créditos y cobranzas con almacenamiento local SQLite.

## Características

- ✅ **Gestión de Clientes**: Crear, listar y buscar clientes
- ✅ **Gestión de Créditos**: Administrar créditos asociados a clientes
- ✅ **Registro de Pagos**: Registrar pagos con ubicación GPS
- ✅ **Mapa**: Visualizar ubicación de clientes
- ✅ **Almacenamiento Local**: Base de datos SQLite en el dispositivo
- ✅ **Funciona Offline**: No requiere conexión a internet

## Requisitos

- Python 3.8+
- Kivy
- KivyMD
- Plyer (para GPS en Android)
- Buildozer (para compilar APK)

## Estructura del Proyecto

```
mobile/
├── database/              # Capa de base de datos SQLite
│   ├── db_manager.py     # Gestor de conexión y operaciones
│   └── models.py         # Definiciones de modelos
├── repositories/          # Capa de acceso a datos
│   ├── cliente_repository.py
│   ├── credito_repository.py
│   └── pago_repository.py
├── screens/              # Pantallas de la aplicación
│   ├── login.py
│   ├── dashboard.py
│   ├── clientes.py
│   ├── creditos.py
│   ├── pagos.py
│   └── mapa.py
├── kv/                   # Archivos de interfaz KV
├── widgets/              # Widgets personalizados
├── services/             # Servicios (GPS)
├── main.py              # Punto de entrada
└── buildozer.spec       # Configuración de compilación

```

## Instalación para Desarrollo

```bash
# Instalar dependencias
pip install kivy kivymd plyer

# Ejecutar en desktop
cd mobile
python main.py
```

## Compilar APK para Android

```bash
# Instalar buildozer
pip install buildozer

# Compilar APK
cd mobile
buildozer android debug

# Compilar y desplegar en dispositivo conectado
buildozer android debug deploy run
```

## Compatibilidad

- **Android**: 9.0 (API 28) - 10.0 (API 29)
- **Dispositivo de prueba**: Samsung Galaxy A20
- **Almacenamiento**: Memoria interna del dispositivo

## Base de Datos

La aplicación utiliza SQLite para almacenar datos localmente:

- **Ubicación**: `/data/data/com.ventasapp/databases/ventas.db`
- **Tablas**: clientes, creditos, pagos
- **Persistencia**: Los datos permanecen en el dispositivo

## Permisos de Android

La aplicación requiere los siguientes permisos:

- `ACCESS_FINE_LOCATION`: Para obtener ubicación GPS precisa
- `ACCESS_COARSE_LOCATION`: Para ubicación aproximada
- `WRITE_EXTERNAL_STORAGE`: Para escribir en almacenamiento
- `READ_EXTERNAL_STORAGE`: Para leer del almacenamiento

## Uso

1. **Login**: Ingresar credenciales (cualquier usuario/contraseña para desarrollo)
2. **Dashboard**: Navegar a diferentes secciones
3. **Clientes**: Agregar y listar clientes
4. **Créditos**: Crear créditos asociados a clientes
5. **Pagos**: Registrar pagos con ubicación GPS automática
6. **Mapa**: Ver ubicación actual

## Notas de Desarrollo

- La base de datos se inicializa automáticamente al abrir la app
- Los datos se guardan localmente y persisten entre sesiones
- No requiere backend ni conexión a internet
- GPS funciona en dispositivos Android reales (no en emulador)

## Autor

Proyecto de gestión de ventas y cobranzas
