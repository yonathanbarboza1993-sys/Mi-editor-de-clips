import streamlit as st

st.set_page_config(page_title="Mi Editor Privado", page_icon="🎬")
st.title("🎬 Mi Plataforma de Clips Gratis")
st.markdown("---")

# Entrada del link
url = st.text_input("Pega el enlace de YouTube aquí para procesar:")

if st.button("🚀 Comenzar a Crear Clips"):
    if not url:
        st.error("Por favor, introduce un enlace de YouTube primero.")
    else:
        st.success("¡Enlace conectado correctamente!")
        st.balloons()
        st.write("Tu servidor privado está listo para empezar a estructurar los videos.")
