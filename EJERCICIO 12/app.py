import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import pandas as pd

# Configuración estética basada en tu diseño (Verde Walmart/Moe)
st.set_page_config(page_title="Walmart Style POS", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f2f5; }
    .stButton>button {
        background-color: #28a745; 
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    .product-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border-bottom: 3px solid #28a745;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE ESCANEO ---
# Nota: Para QR/Barras sin app, usamos este componente que abre la cámara en el iPhone
st.title("🛒 POS Minisuper - Modo Cámara IP")

if 'carrito' not in st.session_state:
    st.session_state.carrito = []

col_escanner, col_carrito = st.columns([1, 1.5])

with col_escanner:
    st.subheader("📸 Escáner de Celular")
    st.info("Abre esta IP en tu iPhone para activar la cámara")
    
    # Este componente activa la cámara del dispositivo que abra la web
    webrtc_streamer(
        key="scanner",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        video_frame_callback=None, # Aquí irá la lógica de Zbar después
        media_stream_constraints={"video": True, "audio": False},
    )
    
    manual_code = st.text_input("O ingresa código manualmente:")
    if st.button("Registrar Producto"):
        # Simulación basada en productos de tu PDF (Duff, Snacks)
        st.session_state.carrito.append({"Producto": "Duff Especial", "Precio": 12.99})
        st.success("Añadido al carrito")

with col_carrito:
    st.subheader("🛍️ Tu Carrito (Tipo Walmart)")
    if st.session_state.carrito:
        for item in st.session_state.carrito:
            st.markdown(f"""
            <div class="product-card">
                <b>{item['Producto']}</b><br>
                <span style="color: #28a745; font-size: 20px;">${item['Precio']}</span>
            </div><br>
            """, unsafe_allow_html=True)
            
        total = sum(i['Precio'] for i in st.session_state.carrito)
        st.divider()
        st.write(f"## Total a Pagar: ${total:.2f}")
        if st.button("FINALIZAR COMPRA"):
            st.balloons()
            st.session_state.carrito = []
    else:
        st.write("Esperando escaneo...")