import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from pyzbar.pyzbar import decode
import cv2
import sqlite3
import av

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="POS Minisuper",
    layout="wide"
)

# =========================
# BASE DE DATOS SQLITE
# =========================

conn = sqlite3.connect(
    "productos.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
codigo TEXT UNIQUE,
nombre TEXT,
precio REAL
)
""")

conn.commit()


def insertar_producto(codigo,nombre,precio):
    try:
        cursor.execute("""
        INSERT INTO productos
        (codigo,nombre,precio)
        VALUES(?,?,?)
        """,(codigo,nombre,precio))

        conn.commit()

    except:
        pass


# PRODUCTOS DE EJEMPLO

insertar_producto("750100000001","Duff Especial",12.99)
insertar_producto("750100000002","Doritos",19.50)
insertar_producto("750100000003","Coca Cola",22)
insertar_producto("750100000004","Pan",35)


def buscar_producto(codigo):

    cursor.execute("""
    SELECT nombre,precio
    FROM productos
    WHERE codigo=?
    """,(codigo,))

    return cursor.fetchone()


# =========================
# SESSION
# =========================

if "carrito" not in st.session_state:
    st.session_state.carrito=[]

if "ultimo" not in st.session_state:
    st.session_state.ultimo=""


# =========================
# ESTILO
# =========================

st.markdown("""
<style>

.stButton button{
background:#28a745;
color:white;
border-radius:10px;
}

.card{
background:white;
padding:15px;
margin:10px;
border-radius:10px;
border-left:8px solid green;
}

</style>
""",unsafe_allow_html=True)


# =========================
# ESCANER
# =========================

def procesar(frame):

    img=frame.to_ndarray(format="bgr24")

    codigos=decode(img)

    for c in codigos:

        codigo=c.data.decode()

        if codigo!=st.session_state.ultimo:

            producto=buscar_producto(codigo)

            if producto:

                nombre,precio=producto

                st.session_state.carrito.append(
                    {
                        "Producto":nombre,
                        "Precio":precio
                    }
                )

                st.session_state.ultimo=codigo

    return av.VideoFrame.from_ndarray(
        img,
        format="bgr24"
    )


# =========================
# INTERFAZ
# =========================

st.title("🛒 POS Minisuper")

c1,c2=st.columns([1,1.5])

with c1:

    st.subheader("📸 Escáner")

    webrtc_streamer(
        key="cam",
        mode=WebRtcMode.SENDRECV,
        video_frame_callback=procesar,
        media_stream_constraints={
            "video":True,
            "audio":False
        }
    )

    st.divider()

    codigo=st.text_input("Código Manual")

    if st.button("Agregar"):

        p=buscar_producto(codigo)

        if p:

            st.session_state.carrito.append({
                "Producto":p[0],
                "Precio":p[1]
            })

            st.success("Producto agregado")

        else:

            st.error("No existe")


with c2:

    st.subheader("🛍️ Carrito")

    total=0

    for p in st.session_state.carrito:

        total+=p["Precio"]

        st.markdown(f"""
        <div class='card'>
        <h4>{p["Producto"]}</h4>
        <h3>${p["Precio"]}</h3>
        </div>
        """,unsafe_allow_html=True)

    st.write(f"## Total: ${total:.2f}")

    if st.button("FINALIZAR"):

        st.balloons()

        st.session_state.carrito=[]


# =========================
# PANEL ADMIN
# =========================

st.divider()

st.subheader("➕ Registrar Producto")

nuevo_codigo=st.text_input("Código")
nuevo_nombre=st.text_input("Nombre")
nuevo_precio=st.number_input("Precio")

if st.button("Guardar Producto"):

    insertar_producto(
        nuevo_codigo,
        nuevo_nombre,
        nuevo_precio
    )

    st.success("Guardado")
    