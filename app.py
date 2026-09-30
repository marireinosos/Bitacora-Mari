import streamlit as st

# ---------------- CONFIGURACIÓN DE LA PÁGINA ----------------
st.set_page_config(
    page_title="Bitácora de Mari",
    page_icon="📒",
    layout="wide",
)

# ---------------- DATOS: EDITA AQUÍ TUS PROYECTOS ----------------
# Cambia el nombre, la descripción y el link de cada proyecto.
# Si tienes más o menos de 10, solo agrega o borra bloques { ... },
proyectos = [
    {
        "nombre": "Proyecto 1",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-1.streamlit.app",
        "emoji": "🎨",
    },
    {
        "nombre": "Proyecto 2",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-2.streamlit.app",
        "emoji": "📊",
    },
    {
        "nombre": "Proyecto 3",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-3.streamlit.app",
        "emoji": "🤖",
    },
    {
        "nombre": "Proyecto 4",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-4.streamlit.app",
        "emoji": "📷",
    },
    {
        "nombre": "Proyecto 5",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-5.streamlit.app",
        "emoji": "🗣️",
    },
    {
        "nombre": "Proyecto 6",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-6.streamlit.app",
        "emoji": "📄",
    },
    {
        "nombre": "Proyecto 7",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-7.streamlit.app",
        "emoji": "✏️",
    },
    {
        "nombre": "Proyecto 8",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-8.streamlit.app",
        "emoji": "🌐",
    },
    {
        "nombre": "Proyecto 9",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-9.streamlit.app",
        "emoji": "💡",
    },
    {
        "nombre": "Proyecto 10",
        "descripcion": "Breve descripción de lo que hace esta app.",
        "link": "https://tu-app-10.streamlit.app",
        "emoji": "✨",
    },
]

# ---------------- ENCABEZADO ----------------
st.title("📒 Bitácora de Mari")
st.subheader("Portafolio de aplicaciones creadas en clase")
st.write(
    "Aquí están todas las apps que hemos desarrollado con Streamlit. "
    "Haz clic en **Abrir app** para ver cada una."
)

# ---------------- BARRA LATERAL ----------------
with st.sidebar:
    st.header("👩‍💻 Sobre mí")
    st.write("**Mariana Reinoso Sánchez**")
    st.write("Bitácora de proyectos del curso.")
    st.divider()
    st.metric("Proyectos", len(proyectos))

# ---------------- BUSCADOR ----------------
busqueda = st.text_input("🔎 Buscar proyecto", placeholder="Escribe un nombre...")
filtrados = [
    p for p in proyectos
    if busqueda.lower() in p["nombre"].lower()
    or busqueda.lower() in p["descripcion"].lower()
]

st.divider()

# ---------------- TARJETAS (3 por fila) ----------------
columnas_por_fila = 3
for i in range(0, len(filtrados), columnas_por_fila):
    cols = st.columns(columnas_por_fila)
    for col, (n, proyecto) in zip(cols, enumerate(filtrados[i:i + columnas_por_fila], start=i + 1)):
        with col:
            with st.container(border=True):
                st.markdown(f"### {proyecto['emoji']} {proyecto['nombre']}")
                st.caption(f"Entrada #{n}")
                st.write(proyecto["descripcion"])
                st.link_button("Abrir app ↗", proyecto["link"], use_container_width=True)

if not filtrados:
    st.info("No se encontró ningún proyecto con ese nombre.")

st.divider()
st.caption("Hecho con ❤️ y Streamlit")
