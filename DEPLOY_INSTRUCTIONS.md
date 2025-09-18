# Instrucciones para Deploy en Streamlit Cloud

## Pasos para conectar el repositorio con Streamlit Cloud:

### 1. Crear el repositorio en GitHub
- Ve a https://github.com/IAtecnoaccion
- Haz clic en "New repository"
- Nombre del repositorio: `dashboard-proyecto-xtract`
- Descripción: "Dashboard interactivo para monitoreo del proyecto Xtract"
- Mantén el repositorio como público para usar Streamlit Cloud gratis
- **NO** inicialices con README, .gitignore o licencia (ya los tenemos)
- Haz clic en "Create repository"

### 2. Subir el código a GitHub
Ejecuta estos comandos en la terminal:
```bash
git push -u origin main
```

### 3. Conectar con Streamlit Cloud
- Ve a https://share.streamlit.io/
- Inicia sesión con tu cuenta de GitHub
- Haz clic en "New app"
- Selecciona tu repositorio: `IAtecnoaccion/dashboard-proyecto-xtract`
- Rama: `main`
- Archivo principal: `dashboard_xtract.py`
- Haz clic en "Deploy!"

### 4. URL final del dashboard
Una vez desplegado, tu dashboard estará disponible en:
`https://share.streamlit.io/iatecnoaccion/dashboard-proyecto-xtract/main/dashboard_xtract.py`

### 5. Actualizaciones futuras
Para actualizar el dashboard:
1. Modifica los archivos localmente
2. Haz commit: `git add . && git commit -m "Descripción de cambios"`
3. Sube a GitHub: `git push`
4. Streamlit Cloud se actualizará automáticamente

## Notas importantes:
- El archivo Excel se incluye en el repositorio para que funcione en Streamlit Cloud
- Si el Excel es muy grande o contiene datos sensibles, considera usar Google Sheets o una base de datos
- Streamlit Cloud tiene límites de recursos para apps gratuitas
