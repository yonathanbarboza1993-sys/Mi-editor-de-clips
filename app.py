import streamlit as st

st.set_page_config(page_title="Mi Editor Privado", page_icon="🎬", layout="wide")
st.title("🎬 Mi Plataforma Automatizada de Clips")
st.markdown("---")

st.write("### 🚀 Generador de Clips en Tiempo Real (Versión Cloud Gratuita)")
st.write("Copia tu enlace de YouTube y procesa tus fragmentos virales utilizando las herramientas integradas abajo:")

# Entrada del link de YouTube
url = st.text_input("1. Pega aquí el enlace del video o directo de YouTube:", placeholder="https://youtube.com...")

if url:
    st.success("✨ ¡Enlace detectado con éxito! Elige tu método de extracción abajo:")
    
    # Crear pestañas organizadas para trabajar
    tab1, tab2 = st.tabs(["✂️ Extractor de Clips Limpios", "🤖 Automatización con IA"])
    
    with tab1:
        st.markdown("#### Herramienta de Descarga y Recorte Directo")
        st.write("Usa este panel integrado para extraer el fragmento exacto de tu video en alta definición y sin marcas de agua de forma gratuita:")
        
        # Inserta una herramienta web de descarga limpia dentro de tu propia página
        st.components.v1.iframe("https://snapsave.io", height=600, scroller=True)
        
    with tab2:
        st.markdown("#### Procesamiento automático de Momentos Virales")
        st.write("Si prefieres que una Inteligencia Artificial escuche la conversación, busque los momentos más virales y les ponga subtítulos automáticos en formato vertical (9:16), utiliza estos motores gratuitos:")
        
        st.info("💡 **Opus Clip:** Te regala créditos gratuitos al registrarte. Analiza el video completo y te entrega 10 clips listos en un par de minutos.")
        st.markdown("- **[Ir a Opus Clip (Herramienta de IA)](https://opus.pro)**")
        st.markdown("- **[Ir a Vizard AI (Alternativa Gratuita)](https://vizard.ai)**")
else:
    st.info("💡 Introduce un enlace de YouTube arriba para desbloquear las herramientas de edición en tiempo real.")
