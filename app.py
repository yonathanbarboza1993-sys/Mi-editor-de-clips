import streamlit as st

st.set_page_config(page_title="Mi Editor Privado", page_icon="🎬", layout="wide")
st.title("🎬 Mi Plataforma Automatizada de Clips")
st.markdown("---")

st.write("### 🚀 Generador de Clips en Tiempo Real (Versión Cloud Gratuita)")
st.write("Copia tu enlace de YouTube y procesa tus fragmentos virales utilizando los accesos directos de abajo:")

# Entrada del link de YouTube
url = st.text_input("1. Pega aquí el enlace del video o directo de YouTube:", placeholder="https://youtube.com...")

if url:
    st.success("✨ ¡Enlace detectado con éxito! Elige tu método de extracción abajo:")
    
    # Crear pestañas organizadas para trabajar sin errores de iframe
    tab1, tab2 = st.tabs(["✂️ Extractor de Clips Limpios", "🤖 Automatización con IA"])
    
    with tab1:
        st.markdown("#### Herramienta de Descarga y Recorte Directo")
        st.write("Para evitar bloqueos del servidor y marcas de agua, usa esta herramienta externa recomendada de forma directa:")
        
        # Enlace directo limpio y seguro
        st.markdown(f"👉 **[Haga clic aquí para abrir el Extractor Gratuito (SnapSave)](https://snapsave.io)**")
        st.info("Pega tu enlace en esa página para descargar el fragmento de video en alta definición totalmente libre.")
        
    with tab2:
        st.markdown("#### Procesamiento automático de Momentos Virales")
        st.write("Si prefieres que una Inteligencia Artificial escuche la conversación, busque los momentos más virales y les ponga subtítulos automáticos en formato vertical (9:16), utiliza estos motores gratuitos:")
        
        st.markdown("- 👉 **[Abrir Opus Clip (Herramienta de IA)](https://opus.pro)** (Te regala créditos gratuitos al registrarte).")
        st.markdown("- 👉 **[Abrir Vizard AI (Alternativa Gratuita)](https://vizard.ai)**")
else:
    st.info("💡 Introduce un enlace de YouTube arriba para desbloquear las herramientas de edición en tiempo real.")
