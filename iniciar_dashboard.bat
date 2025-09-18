@echo off
cd /d "c:\Users\Nicolas\Desktop\Dashboard proyecto xtract"
echo Iniciando Dashboard Proyecto Xtract...
echo.
echo El dashboard se abrirá en tu navegador web.
echo Para detener el dashboard, presiona Ctrl+C en esta ventana.
echo.
"C:/Users/Nicolas/AppData/Local/Programs/Python/Python313/python.exe" -m streamlit run dashboard_xtract.py
pause
