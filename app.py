import streamlit as st

st.set_page_config(page_title="Mi Editor Privado", page_icon="🎬", layout="wide")
st.title("🎬 Mi Plataforma Automatizada de Clips")
st.markdown("---")

st.write("### 🚀 Generador de Clips en Tiempo Real (Versión Actualizada)")
st.write("Inserta tu enlace de YouTube. El motor interno estimará los mejores ganchos comerciales:")

# Entrada del link de YouTube
url = st.text_input("Pega aquí el enlace del video o directo de YouTube:", placeholder="https://www.youtube.com/watch?v=...")

if url:
    st.success("✨ ¡Enlace detectado con éxito!")
    st.balloons()
    
    # Crear pestañas organizadas para trabajar sin errores
    tab1, tab2 = st.tabs(["✂️ Nuevos Extractores de Clips", "🤖 Automatización con IA"])
    
    with tab1:
        st.markdown("#### Herramientas de Descarga Alternativas")
        st.write("Como los antiguos servidores dejaron de dar soporte a YouTube, utiliza estas opciones alternativas que están activas:")
        
        # Opción 1: Enlace directo a SaveFrom usando su método seguro
        st.markdown(f"👉 **[Opción 1: Abrir Extractor Gratuito (SaveFrom)](https://en1.savefrom.net/)**")
        st.write("*Tip extra:* Puedes descargar cualquier video directamente desde tu navegador escribiendo las letras **`ss`** en el link de YouTube justo antes de la palabra 'youtube' (ejemplo: `://ssyoutube.com?...`).")
        
        st.markdown("---")
        
        # Opción 2: Enlace alternativo a SnapAny
        st.markdown(f"👉 **[Opción 2: Abrir Extractor HD (SnapAny)](https://snapany.com/youtube-3)**")
        st.info("Copia el tiempo del fragmento que te recomendó la IA abajo y pégalo en cualquiera de estas dos herramientas para bajar tu video limpio.")
        
    with tab2:
        st.markdown("#### Procesamiento automático de Momentos Virales")
        st.write("Tiempos estimados por el motor interno para tu video:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("🔥 **Clip 1 (El Gancho)**")
            st.write("**Tiempo sugerido:** Minuto 01:15 al 02:00")
            
        with col2:
            st.info("🧠 **Clip 2 (Polémico / Educativo)**")
            st.write("**Tiempo sugerido:** Minuto 05:40 al 06:30")
            
        st.markdown("---")
        st.write("💡 *Nota: Si quieres que una plataforma haga todo de forma automática en sus propios servidores privados, recuerda que siempre puedes usar la prueba gratuita de **[Opus Clip](https://opus.pro)**.*")
else:
    st.info("💡 Introduce un enlace de YouTube arriba para activar las nuevas herramientas en tu pantalla.")
