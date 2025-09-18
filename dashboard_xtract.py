import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Proyecto Xtract",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("📊 Dashboard Proyecto Xtract")
st.markdown("### Automatización de Carga de Facturas: Xtract → NetSuite")
st.markdown("---")

# Función para cargar datos
@st.cache_data
def load_data():
    """Carga los datos del archivo Excel"""
    try:
        df = pd.read_excel('Status proyecto xtract.xlsx')
        return df
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

# Cargar datos
df = load_data()

if df is not None:
    # CSS personalizado para colores de métricas
    st.markdown("""
    <style>
    [data-testid="metric-container"] {
        background-color: #f0f2f6;
        border: 1px solid #e0e0e0;
        padding: 5% 5% 5% 10%;
        border-radius: 10px;
        border-left: 0.5rem solid #9e9e9e;
    }
    
    .metric-completadas {
        background-color: #d4edda !important;
        border-left-color: #28a745 !important;
    }
    
    .metric-pendientes {
        background-color: #fff3cd !important;
        border-left-color: #ffc107 !important;
    }
    
    .metric-errores {
        background-color: #f8d7da !important;
        border-left-color: #dc3545 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar con filtros
    st.sidebar.header("🔍 Filtros")
    
    # Filtro por estado
    status_options = ['Todos'] + list(df['Status'].unique())
    selected_status = st.sidebar.selectbox("Filtrar por Estado:", status_options)
    
    # Filtro por proveedor
    if 'Proveedor' in df.columns:
        proveedores = df['Proveedor'].dropna().unique()
        if len(proveedores) > 0:
            proveedor_options = ['Todos'] + list(proveedores)
            selected_proveedor = st.sidebar.selectbox("Filtrar por Proveedor:", proveedor_options)
        else:
            selected_proveedor = 'Todos'
    else:
        selected_proveedor = 'Todos'
    
    # Aplicar filtros
    filtered_df = df.copy()
    if selected_status != 'Todos':
        filtered_df = filtered_df[filtered_df['Status'] == selected_status]
    if selected_proveedor != 'Todos':
        filtered_df = filtered_df[filtered_df['Proveedor'] == selected_proveedor]
    
    # Métricas principales
    st.header("📈 Métricas Principales")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_facturas = len(filtered_df)
        st.metric("Total Facturas", total_facturas)
    
    with col2:
        done_count = len(filtered_df[(filtered_df['Status'] == 'Done') | (filtered_df['Status'] == 'Ok Xtract - No pasar a Sandbox')])
        done_percentage = (done_count / total_facturas * 100) if total_facturas > 0 else 0
        st.markdown('<div class="metric-completadas">', unsafe_allow_html=True)
        st.metric("Completadas", f"{done_count}", f"{done_percentage:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        pendiente_count = len(filtered_df[filtered_df['Status'].str.contains('Pendiente', na=False)])
        pendiente_percentage = (pendiente_count / total_facturas * 100) if total_facturas > 0 else 0
        st.markdown('<div class="metric-pendientes">', unsafe_allow_html=True)
        st.metric("Pendientes", f"{pendiente_count}", f"{pendiente_percentage:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        error_count = len(filtered_df[filtered_df['Status'].str.contains('Error', na=False)])
        error_percentage = (error_count / total_facturas * 100) if total_facturas > 0 else 0
        st.markdown('<div class="metric-errores">', unsafe_allow_html=True)
        st.metric("Con Errores", f"{error_count}", f"{error_percentage:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráficos principales
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Distribución por Estado")
        status_counts = filtered_df['Status'].value_counts()
        
        # Definir colores para cada estado
        colors = {
            'Done': '#28a745',
            'En Proceso': '#ffc107',
            'Error': '#dc3545',
            'Error NS': '#fd7e14',
            'Error Xtract': '#e83e8c',
            'Ok Xtract - No pasar a Sandbox': '#17a2b8',
            'Pendiente análisis Tekiio': '#6f42c1',
            'Pendiente Tekiio': '#6c757d'
        }
        
        fig_pie = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Distribución de Estados",
            color=status_counts.index,
            color_discrete_map=colors
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, width='stretch')
    
    with col2:
        st.subheader("📈 Estados por Categoría")
        
        # Categorizar estados
        def categorize_status(status):
            if status == 'Done' or status == 'Ok Xtract - No pasar a Sandbox':
                return 'Completado'
            elif 'Error' in status:
                return 'Error'
            elif 'Pendiente' in status:
                return 'Pendiente'
            elif 'En Proceso' in status:
                return 'En Proceso'
            else:
                return 'Otros'
        
        filtered_df['Categoria'] = filtered_df['Status'].apply(categorize_status)
        categoria_counts = filtered_df['Categoria'].value_counts()
        
        fig_bar = px.bar(
            x=categoria_counts.index,
            y=categoria_counts.values,
            title="Facturas por Categoría",
            color=categoria_counts.index,
            color_discrete_map={
                'Completado': '#28a745',
                'Error': '#dc3545',
                'Pendiente': '#6c757d',
                'En Proceso': '#ffc107',
                'Otros': '#17a2b8'
            }
        )
        fig_bar.update_layout(
            xaxis_title="Categoría",
            yaxis_title="Cantidad de Facturas",
            height=400
        )
        st.plotly_chart(fig_bar, width='stretch')
    
    # Tabla de detalles por estado
    st.header("📋 Detalle por Estado")
    
    # Crear tabs para cada estado
    status_list = filtered_df['Status'].unique()
    tabs = st.tabs([f"{status} ({len(filtered_df[filtered_df['Status'] == status])})" for status in status_list])
    
    for i, status in enumerate(status_list):
        with tabs[i]:
            status_df = filtered_df[filtered_df['Status'] == status]
            
            # Mostrar descripción del estado
            descriptions = {
                'Done': '✅ La factura ya se encuentra bien cargada tanto en Xtract como en NetSuite',
                'En Proceso': '🔄 Se debe analizar la factura y parametrizar en Xtract',
                'Error': '❌ Hay algún error en Xtract o en NetSuite',
                'Error NS': '🔴 La factura se cargó bien en Xtract, pero hay un error de parametrización en NetSuite',
                'Error Xtract': '🟠 Hay un error en la lectura de la factura en Xtract',
                'Ok Xtract - No pasar a Sandbox': '🟢 La factura se cargó bien en Xtract, no amerita probarla en NetSuite',
                'Pendiente análisis Tekiio': '🔍 La consultora de NetSuite debe analizar el caso',
                'Pendiente Tekiio': '⏳ Está pendiente de migrar a NetSuite'
            }
            
            if status in descriptions:
                st.info(descriptions[status])
            
            # Mostrar tabla con datos relevantes
            if len(status_df) > 0:
                display_columns = ['Nro factura', 'Proveedor', 'Link Xtract', 'Link Netsuite', 'Comentarios Tecno Accion']
                available_columns = [col for col in display_columns if col in status_df.columns]
                
                if available_columns:
                    st.dataframe(
                        status_df[available_columns],
                        width='stretch',
                        hide_index=True
                    )
                else:
                    st.dataframe(status_df, width='stretch', hide_index=True)
            else:
                st.info("No hay facturas con este estado en el filtro actual")
    
    # Análisis adicional
    st.header("📊 Análisis Adicional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚡ Progreso General")
        
        # Métrica grande del porcentaje
        total = len(df)
        done = len(df[(df['Status'] == 'Done') | (df['Status'] == 'Ok Xtract - No pasar a Sandbox')])
        progress = done / total if total > 0 else 0
        progress_percentage = progress * 100
        
        # Mostrar métrica destacada
        st.metric(
            label="Progreso Completado",
            value=f"{progress_percentage:.1f}%",
            delta=f"{done} de {total} facturas"
        )
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = progress_percentage,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "% Completado", 'font': {'size': 20}},
            delta = {'reference': 50, 'font': {'size': 16}},
            number = {'font': {'size': 48, 'color': "darkgreen"}},
            gauge = {
                'axis': {
                    'range': [None, 100],
                    'tickwidth': 1,
                    'tickcolor': "darkblue",
                    'tickfont': {'size': 14}
                },
                'bar': {'color': "darkgreen", 'thickness': 0.8},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 25], 'color': "#ffcccc"},
                    {'range': [25, 50], 'color': "#fff3cd"},
                    {'range': [50, 75], 'color': "#d1ecf1"},
                    {'range': [75, 100], 'color': "#d4edda"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        fig_gauge.update_layout(
            height=400,
            font={'color': "darkblue", 'family': "Arial"},
            margin=dict(l=20, r=20, t=60, b=20)
        )
        st.plotly_chart(fig_gauge, width='stretch')
    
    with col2:
        st.subheader("🔢 Resumen Numérico")
        summary_data = {
            'Categoría': ['Total Facturas', 'Completadas', 'En Proceso/Pendientes', 'Con Errores'],
            'Cantidad': [
                len(df),
                len(df[(df['Status'] == 'Done') | (df['Status'] == 'Ok Xtract - No pasar a Sandbox')]),
                len(df[df['Status'].str.contains('Proceso|Pendiente', na=False)]),
                len(df[df['Status'].str.contains('Error', na=False)])
            ]
        }
        summary_df = pd.DataFrame(summary_data)
        summary_df['Porcentaje'] = (summary_df['Cantidad'] / len(df) * 100).round(1)
        
        st.dataframe(summary_df, width='stretch', hide_index=True)
    
    # Información adicional en sidebar
    st.sidebar.markdown("---")
    st.sidebar.header("ℹ️ Información")
    st.sidebar.info(f"Última actualización: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    st.sidebar.info(f"Total de registros: {len(df)}")
    
    if selected_status != 'Todos' or selected_proveedor != 'Todos':
        st.sidebar.warning(f"Mostrando {len(filtered_df)} de {len(df)} registros (filtrado)")

else:
    st.error("❌ No se pudo cargar el archivo 'Status proyecto xtract.xlsx'")
    st.info("Asegúrate de que el archivo esté en el mismo directorio que este script.")
