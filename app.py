"""
🤎 Bitácora de Mari Reinoso
Portafolio con las aplicaciones de Streamlit hechas en clase.
"""

import os
import io
import base64
import streamlit as st
from PIL import Image, ImageOps


# ─────────────────────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Bitácora · Mari Reinoso",
    page_icon="🎀",
    layout="wide",
)


def html(codigo):
    """Muestra HTML/CSS. Usa st.html (Streamlit nuevo) y si no existe, st.markdown."""
    if hasattr(st, "html"):
        st.html(codigo)
    else:
        st.markdown(codigo, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# MI FOTO 📷 (debe estar en el repo con este mismo nombre)
# La app la endereza, la recorta en cuadrado y la pone en un círculo.
# ─────────────────────────────────────────────
FOTO = "WhatsApp Image 2026-09-30 at 19.04.57.jpeg"


@st.cache_data
def foto_base64(ruta):
    """Devuelve la foto lista para mostrar en HTML, o None si no se puede."""
    if not os.path.exists(ruta):
        return None
    try:
        try:
            from pillow_heif import register_heif_opener
            register_heif_opener()
        except ImportError:
            pass
        img = Image.open(ruta)
        img = ImageOps.exif_transpose(img).convert("RGB")   # endereza la foto
        img = ImageOps.fit(img, (600, 600), Image.Resampling.LANCZOS)  # cuadrada
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=88)
        return base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return None


foto = foto_base64(FOTO)


def foto_html(tam, borde=4):
    """Círculo con mi foto (o un moñito si la foto no carga)."""
    if foto:
        return (f'<img src="data:image/jpeg;base64,{foto}" '
                f'style="width:{tam}px; height:{tam}px; border-radius:50%; object-fit:cover; '
                f'border:{borde}px solid #fffaf5; box-shadow:0 0 0 2px #e8b4b8, '
                f'0 12px 30px rgba(111,78,55,0.25); display:block; margin:0 auto;">')
    return (f'<div style="width:{tam}px; height:{tam}px; margin:0 auto; border-radius:50%; '
            f'background:linear-gradient(135deg,#f9e4e4,#ead8c4); border:2px solid #e8b4b8; '
            f'display:flex; align-items:center; justify-content:center; font-size:{tam // 2.5}px;">🎀</div>')


# ─────────────────────────────────────────────
# MIS PROYECTOS  ✏️ (edita aquí nombres, textos o links)
# ─────────────────────────────────────────────
proyectos = [
    {
        "nombre": "Intro",
        "emoji": "🌷",
        "categoria": "Inicio",
        "descripcion": "Mi primera app en Streamlit: el punto de partida de todo este camino.",
        "link": "https://gx3hwpphjq46bu8fbuilp6.streamlit.app",
    },
    {
        "nombre": "Word Cloud",
        "emoji": "☁️",
        "categoria": "Texto",
        "descripcion": "Convierte cualquier texto en una nube donde las palabras más repetidas brillan más.",
        "link": "https://wordcloud-oah4vs4f39xymrw43qwfii.streamlit.app",
    },
    {
        "nombre": "OCR",
        "emoji": "📸",
        "categoria": "Visión",
        "descripcion": "Lee el texto que aparece en una foto y lo vuelve texto que puedes copiar.",
        "link": "https://kzwfzvzq2fsmj7lli8gxef.streamlit.app",
    },
    {
        "nombre": "OCR Audio",
        "emoji": "🎧",
        "categoria": "Voz",
        "descripcion": "Lee el texto de una imagen y además te lo dice en voz alta.",
        "link": "https://ocr-audio-cybx2bz8eug8vckezpgn9s.streamlit.app",
    },
    {
        "nombre": "Análisis de Sentimientos",
        "emoji": "💌",
        "categoria": "Texto",
        "descripcion": "Descubre si un texto se siente positivo, negativo o neutral.",
        "link": "https://sentimenta-9gdnuyqcwnqze9nppleexu.streamlit.app",
    },
    {
        "nombre": "Traductor",
        "emoji": "🌍",
        "categoria": "Voz",
        "descripcion": "Traduce tu voz o tus palabras a otro idioma en segundos.",
        "link": "https://traductor-fouskndrzrujvhecixkb67.streamlit.app",
    },
    {
        "nombre": "Teachable Machine",
        "emoji": "🤍",
        "categoria": "Visión",
        "descripcion": "Reconoce imágenes con un modelo que entrené en Teachable Machine.",
        "link": "https://zd3xxq4fqczr2k39vwwqcw.streamlit.app",
    },
    {
        "nombre": "YOLO",
        "emoji": "🔍",
        "categoria": "Visión",
        "descripcion": "Detecta y señala los objetos que aparecen en una foto.",
        "link": "https://yolov5-f8y7myw4rcqdvqtrtypnyn.streamlit.app",
    },
    {
        "nombre": "Texto a Audio",
        "emoji": "🔊",
        "categoria": "Voz",
        "descripcion": "Escribe lo que quieras y escúchalo convertido en voz.",
        "link": "https://ml42qcmqdtepzlpyhuzcej.streamlit.app",
    },
    {
        "nombre": "TF-IDF",
        "emoji": "📚",
        "categoria": "Texto",
        "descripcion": "Encuentra las palabras más importantes dentro de un grupo de textos.",
        "link": "https://jbqjzc6nivejaomlgmrhwk.streamlit.app",
    },
]

CATEGORIAS = {
    "Todas":  "✨",
    "Inicio": "🌷",
    "Texto":  "📝",
    "Voz":    "🎙️",
    "Visión": "👁️",
}


# ─────────────────────────────────────────────
# ESTILOS · beige, rosado y café 🤎🎀
# ─────────────────────────────────────────────
html("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Poppins:wght@300;400;500;600&display=swap');

    :root {
        --crema:   #fffaf5;
        --beige:   #f4e9dd;
        --beige2:  #ead8c4;
        --rosa:    #e8b4b8;
        --rosa2:   #d99aa0;
        --rosabg:  #f9e4e4;
        --cafe:    #6f4e37;
        --cafe2:   #9c7a60;
        --cafe3:   #b8977c;
    }

    .stApp, .stApp p, .stApp label, .stApp input, .stApp button, .stApp li {
        font-family: 'Poppins', sans-serif;
    }
    .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
        font-family: 'Cormorant Garamond', serif !important;
        color: var(--cafe) !important;
        font-weight: 600 !important;
    }
    .stApp {
        background:
            radial-gradient(circle at 0% 0%, #f9e4e4 0%, transparent 35%),
            radial-gradient(circle at 100% 20%, #f3e2d2 0%, transparent 40%),
            radial-gradient(circle at 50% 100%, #f9e4e4 0%, transparent 40%),
            #f8f0e7;
    }
    p, li, label { color: #7d5f4a; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: var(--crema) !important;
        border-right: 1px solid var(--beige2);
    }
    [data-testid="stSidebar"] h3 {
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.72rem !important;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        color: var(--cafe3) !important;
    }

    /* Tarjetas (st.container con borde) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid var(--beige2) !important;
        border-radius: 28px !important;
        background: var(--crema);
        box-shadow: 0 10px 28px rgba(111,78,55,0.07);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-6px);
        box-shadow: 0 18px 38px rgba(217,154,160,0.25);
    }

    /* Botones de link */
    [data-testid="stLinkButton"] a, .stLinkButton a {
        background: linear-gradient(135deg, #e8b4b8, #d99aa0) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 999px !important;
        font-weight: 500 !important;
        letter-spacing: 0.6px;
        transition: all 0.25s ease !important;
    }
    [data-testid="stLinkButton"] a:hover, .stLinkButton a:hover {
        background: linear-gradient(135deg, #b8977c, #6f4e37) !important;
        transform: scale(1.02);
    }

    /* Filtro de categorías */
    [data-testid="stRadio"] [role="radiogroup"] {
        gap: 10px;
        justify-content: center;
        flex-wrap: wrap;
    }
    [data-testid="stRadio"] [role="radiogroup"] label {
        background: var(--crema);
        border: 1px solid var(--beige2);
        border-radius: 999px;
        padding: 6px 16px;
        transition: all 0.2s;
    }
    [data-testid="stRadio"] [role="radiogroup"] label:hover {
        background: var(--rosabg);
        border-color: var(--rosa);
    }

    /* Portada */
    .portada {
        background: linear-gradient(135deg, #fffaf5 0%, #f7e3dc 45%, #efd9c7 100%);
        border: 1px solid var(--beige2);
        border-radius: 40px;
        padding: 56px 40px 48px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 18px 50px rgba(111,78,55,0.12);
        font-family: 'Poppins', sans-serif;
    }
    .portada::before, .portada::after {
        content: "";
        position: absolute;
        border-radius: 50%;
        filter: blur(2px);
    }
    .portada::before {
        width: 260px; height: 260px;
        background: rgba(232,180,184,0.35);
        top: -90px; left: -70px;
    }
    .portada::after {
        width: 220px; height: 220px;
        background: rgba(184,151,124,0.22);
        bottom: -90px; right: -50px;
    }
    .portada .marco {
        position: relative;
        z-index: 2;
        width: fit-content;
        margin: 0 auto 18px;
        animation: aparecer 0.8s ease;
    }
    @keyframes aparecer {
        from { opacity: 0; transform: scale(0.9); }
        to   { opacity: 1; transform: scale(1); }
    }
    .portada .sobre {
        position: relative;
        font-size: 0.72rem;
        letter-spacing: 5px;
        text-transform: uppercase;
        color: var(--cafe2);
    }
    .portada .firma {
        position: relative;
        font-family: 'Great Vibes', cursive;
        font-size: 5.2rem;
        line-height: 1.05;
        color: var(--cafe);
        margin: 10px 0 0;
    }
    .portada .firma span { color: var(--rosa2); }
    .portada .titulo {
        position: relative;
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 1.7rem;
        color: var(--cafe2);
        margin-top: 2px;
    }
    .portada .linea {
        position: relative;
        width: 90px;
        height: 2px;
        margin: 18px auto;
        background: linear-gradient(90deg, transparent, var(--rosa2), transparent);
    }
    .portada p {
        position: relative;
        color: #8a6a55;
        max-width: 560px;
        margin: 0 auto;
        font-size: 0.98rem;
        line-height: 1.7;
    }
    .deco {
        position: absolute;
        font-size: 1.4rem;
        opacity: 0.75;
        animation: flotar 5s ease-in-out infinite;
        z-index: 1;
    }
    @keyframes flotar {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50%      { transform: translateY(-10px) rotate(8deg); }
    }

    /* Mini stats */
    .stats {
        display: flex;
        gap: 14px;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 22px;
        font-family: 'Poppins', sans-serif;
    }
    .stat {
        background: var(--crema);
        border: 1px solid var(--beige2);
        border-radius: 22px;
        padding: 14px 26px;
        text-align: center;
        min-width: 130px;
    }
    .stat b {
        display: block;
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.1rem;
        color: var(--rosa2);
        line-height: 1;
    }
    .stat span {
        font-size: 0.75rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--cafe2);
    }

    /* Título de sección */
    .seccion {
        text-align: center;
        margin: 34px 0 6px;
        font-family: 'Poppins', sans-serif;
    }
    .seccion .mini {
        font-size: 0.7rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: var(--cafe3);
    }
    .seccion h2 {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-weight: 600;
        font-size: 2.4rem;
        color: var(--cafe);
        margin: 4px 0 0;
    }

    /* Contenido de cada tarjeta */
    .card {
        font-family: 'Poppins', sans-serif;
        padding: 4px 4px 0;
    }
    .card .arriba {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .card .num {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 1.1rem;
        color: var(--cafe3);
    }
    .card .chip {
        background: var(--rosabg);
        color: var(--rosa2);
        border-radius: 999px;
        padding: 3px 12px;
        font-size: 0.7rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-weight: 600;
    }
    .card .icono {
        width: 64px; height: 64px;
        margin: 16px 0 12px;
        border-radius: 50%;
        background: linear-gradient(135deg, #f9e4e4, #f4e9dd);
        border: 1px solid var(--beige2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.9rem;
    }
    .card .nombre {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.75rem;
        font-weight: 600;
        color: var(--cafe);
        line-height: 1.1;
    }
    .card .desc {
        color: #8a6a55;
        font-size: 0.9rem;
        line-height: 1.6;
        margin-top: 8px;
        min-height: 58px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        font-family: 'Poppins', sans-serif;
    }
    .footer .firma {
        font-family: 'Great Vibes', cursive;
        font-size: 2.4rem;
        color: var(--cafe);
    }
    .footer p {
        font-size: 0.78rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: var(--cafe3);
        margin: 0;
    }
</style>
""")


# ─────────────────────────────────────────────
# PANEL LATERAL
# ─────────────────────────────────────────────
with st.sidebar:
    html(f"""
    <div style="text-align:center; font-family:'Poppins',sans-serif; padding-top:10px;">
        {foto_html(110, 3)}
        <div style="font-family:'Great Vibes',cursive; font-size:2.4rem; color:#6f4e37; margin-top:10px;">
            Mari Reinoso
        </div>
        <div style="font-size:0.72rem; letter-spacing:3px; text-transform:uppercase; color:#b8977c;">
            Bitácora de clase
        </div>
    </div>
    """)
    st.divider()

    st.markdown("### Sobre esta bitácora")
    st.caption(
        "Aquí guardo todas las actividades que fui haciendo en clase "
        "con Python y Streamlit, una por una. 🤎"
    )

    st.divider()
    st.markdown("### Índice")
    for i, p in enumerate(proyectos, start=1):
        st.markdown(f"{p['emoji']} [{i:02d} · {p['nombre']}]({p['link']})")


# ─────────────────────────────────────────────
# PORTADA
# ─────────────────────────────────────────────
total = len(proyectos)
n_texto = sum(p["categoria"] == "Texto" for p in proyectos)
n_voz = sum(p["categoria"] == "Voz" for p in proyectos)
n_vision = sum(p["categoria"] == "Visión" for p in proyectos)

html(f"""
<div class="portada">
    <span class="deco" style="top:26px; left:40px;">🎀</span>
    <span class="deco" style="top:44px; right:56px; animation-delay:1.3s;">🤎</span>
    <span class="deco" style="bottom:30px; left:14%; animation-delay:2.1s;">🌷</span>
    <span class="deco" style="bottom:34px; right:16%; animation-delay:1.7s;">✨</span>
    <span class="deco" style="top:50%; left:6%; animation-delay:0.6s;">☕</span>

    <div class="marco">{foto_html(170, 5)}</div>
    <div class="sobre">Portafolio de clase</div>
    <div class="firma">Mari <span>Reinoso</span></div>
    <div class="titulo">Bitácora de actividades en clase</div>
    <div class="linea"></div>
    <p>Un pequeño diario con todas las actividades que hicimos en clase.
       Cada tarjeta es un proyecto: ábrela y pruébala 💌</p>
</div>

<div class="stats">
    <div class="stat"><b>{total}</b><span>Proyectos</span></div>
    <div class="stat"><b>{n_texto}</b><span>Texto</span></div>
    <div class="stat"><b>{n_voz}</b><span>Voz</span></div>
    <div class="stat"><b>{n_vision}</b><span>Visión</span></div>
</div>

<div class="seccion">
    <div class="mini">mis creaciones</div>
    <h2>Actividades del curso</h2>
</div>
""")


# ─────────────────────────────────────────────
# FILTRO
# ─────────────────────────────────────────────
filtro = st.radio(
    "Filtrar",
    list(CATEGORIAS.keys()),
    format_func=lambda c: f"{CATEGORIAS[c]} {c}",
    horizontal=True,
    label_visibility="collapsed",
)

visibles = [(i, p) for i, p in enumerate(proyectos, start=1)
            if filtro == "Todas" or p["categoria"] == filtro]

st.write("")


# ─────────────────────────────────────────────
# TARJETAS (3 por fila)
# ─────────────────────────────────────────────
POR_FILA = 3
for inicio in range(0, len(visibles), POR_FILA):
    cols = st.columns(POR_FILA, gap="medium")
    for col, (num, p) in zip(cols, visibles[inicio:inicio + POR_FILA]):
        with col:
            with st.container(border=True):
                html(f"""
                <div class="card">
                    <div class="arriba">
                        <span class="num">N.º {num:02d}</span>
                        <span class="chip">{p['categoria']}</span>
                    </div>
                    <div class="icono">{p['emoji']}</div>
                    <div class="nombre">{p['nombre']}</div>
                    <div class="desc">{p['descripcion']}</div>
                </div>
                """)
                st.link_button("Abrir proyecto ✨", p["link"], use_container_width=True)


# ─────────────────────────────────────────────
# PIE
# ─────────────────────────────────────────────
html("""
<div class="footer">
    <div class="firma">con cariño, Mari</div>
    <p>hecho con python, streamlit y mucho café ☕</p>
</div>
""")
