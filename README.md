# Dashboard Proyecto Xtract

Dashboard interactivo para monitorear el estado del proyecto de migración de facturas desde Xtract hacia NetSuite.

## 📋 Descripción

Este dashboard proporciona una vista completa del progreso del proyecto Xtract, mostrando:

- **Métricas principales**: Total de facturas, completadas, pendientes y con errores
- **Visualizaciones interactivas**: Gráficos de distribución por estado y categoría
- **Análisis detallado**: Información específica por cada tipo de estado
- **Filtros dinámicos**: Por estado y proveedor
- **Indicador de progreso**: Medidor visual del avance general

## 🏷️ Estados del Proyecto

- **Done**: ✅ La factura ya se encuentra bien cargada tanto en Xtract como en NetSuite
- **En Proceso**: 🔄 Se debe analizar la factura y parametrizar en Xtract
- **Error**: ❌ Hay algún error en Xtract o en NetSuite
- **Error NS**: 🔴 La factura se cargó bien en Xtract, pero hay un error de parametrización en NetSuite
- **Error Xtract**: 🟠 Hay un error en la lectura de la factura en Xtract
- **Ok Xtract - No pasar a Sandbox**: 🟢 La factura se cargó bien en Xtract, no amerita probarla en NetSuite
- **Pendiente análisis Tekiio**: 🔍 La consultora de NetSuite debe analizar el caso
- **Pendiente Tekiio**: ⏳ Está pendiente de migrar a NetSuite

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.8 o superior
- Archivo Excel "Status proyecto xtract.xlsx" en el mismo directorio

### Pasos para ejecutar:

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar el dashboard**:
   ```bash
   streamlit run dashboard_xtract.py
   ```

3. **Abrir en el navegador**:
   El dashboard se abrirá automáticamente en tu navegador predeterminado (generalmente en http://localhost:8501)

## 📊 Características del Dashboard

### Métricas Principales
- Contador total de facturas
- Número y porcentaje de facturas completadas
- Número y porcentaje de facturas pendientes
- Número y porcentaje de facturas con errores

### Visualizaciones
- **Gráfico Circular**: Distribución detallada por cada estado
- **Gráfico de Barras**: Agrupación por categorías principales
- **Medidor de Progreso**: Indicador visual del porcentaje completado
- **Tablas Detalladas**: Información específica por estado con enlaces a Xtract y NetSuite

### Filtros Interactivos
- **Por Estado**: Permite filtrar por cualquier estado específico
- **Por Proveedor**: Filtra por proveedor cuando la información está disponible

### Funcionalidades Adicionales
- **Actualización automática**: Los datos se actualizan al recargar la página
- **Responsive**: El dashboard se adapta a diferentes tamaños de pantalla
- **Exportable**: Las visualizaciones pueden descargarse como imágenes

## 📁 Estructura de Archivos

```
Dashboard proyecto xtract/
├── dashboard_xtract.py      # Archivo principal del dashboard
├── requirements.txt         # Dependencias de Python
├── README.md               # Este archivo
└── Status proyecto xtract.xlsx  # Archivo de datos (requerido)
```

## 🔄 Actualización de Datos

Para actualizar los datos del dashboard:
1. Reemplaza el archivo "Status proyecto xtract.xlsx" con la nueva versión
2. Recarga la página del dashboard en tu navegador
3. Los nuevos datos se cargarán automáticamente

## 💡 Consejos de Uso

- Utiliza los filtros en la barra lateral para analizar segmentos específicos
- Haz clic en las pestañas de estados para ver detalles específicos
- El medidor de progreso te da una vista rápida del avance general
- Los enlaces a Xtract y NetSuite están disponibles en las tablas detalladas

## 🐛 Solución de Problemas

- **Error de archivo no encontrado**: Asegúrate de que "Status proyecto xtract.xlsx" esté en el mismo directorio
- **Error de dependencias**: Ejecuta `pip install -r requirements.txt` para instalar las librerías necesarias
- **El dashboard no se abre**: Verifica que el puerto 8501 no esté en uso por otra aplicación
