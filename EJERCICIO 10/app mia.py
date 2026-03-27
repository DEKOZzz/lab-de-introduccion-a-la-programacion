import collections
import collections.abc
# Parche de compatibilidad para Python 3.12 (¡Indispensable!)
if not hasattr(collections, 'MutableMapping'):
    collections.MutableMapping = collections.abc.MutableMapping

import streamlit as st

# Configuración de página con tema oscuro por defecto
st.set_page_config(page_title="Agencia Chikitines Goth", layout="wide", initial_sidebar_state="collapsed")

# --- ESTILOS CSS GÓTICOS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Importar fuente gótica/medieval */
    @import url('https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap');

    /* Fondo de la página y texto global */
    .main {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Títulos Góticos */
    .stTitle, h1, h2, h3 {
        font-family: 'MedievalSharp', cursive !important;
        color: #ff4b4b !important; /* Rojo sangre para títulos */
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
    }

    /* Estilo Gótico de las Cards */
    .card-goth {
        background-color: #1a1a1a; /* Negro mate */
        padding: 25px;
        border-radius: 10px;
        border: 2px solid #440000; /* Borde de hierro oxidado */
        box-shadow: 0 5px 15px rgba(187, 134, 252, 0.2); /* Brillo púrpura sutil */
        text-align: center;
        margin-bottom: 15px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }

    /* Efecto Hover Gótico (Pasa el mouse) */
    .card-goth:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 10px 25px rgba(187, 134, 252, 0.5); /* Brillo púrpura intenso */
        border-color: #ff4b4b; /* El borde se vuelve rojo sangre */
        cursor: url('https://cur.cursors-4u.net/symbols/sym-1/sym1.ani'), fire !important; /* Puntero de fuego */
    }
    
    /* Texto dentro de la card */
    .card-goth h3 {
        font-size: 1.8em;
        margin-bottom: 10px;
    }
    
    .card-goth p {
        color: #a0a0a0;
        font-size: 1em;
        font-style: italic;
    }

    /* Decoración de esquinas góticas (opcional, usando pseudo-elementos) */
    .card-goth::before {
        content: '☠';
        position: absolute;
        top: 5px;
        right: 10px;
        font-size: 1.2em;
        color: #440000;
        opacity: 0.5;
    }

    /* Botones estilo Metal Oscuro */
    .stButton>button {
        border-radius: 5px;
        background-color: #2d2d2d; /* Metal oscuro */
        color: #ff4b4b; /* Texto rojo */
        border: 1px solid #440000;
        font-family: 'MedievalSharp', cursive;
        font-size: 1.1em;
        letter-spacing: 1px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #440000; /* Rojo oscuro al hover */
        border-color: #ff4b4b;
        color: #ffffff;
        box-shadow: 0 0 10px rgba(255, 75, 75, 0.5);
    }

    /* Estilo de los inputs oscuros */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1a1a1a !important;
        color: #e0e0e0 !important;
        border: 1px solid #440000 !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #bb86fc !important;
        box-shadow: 0 0 5px rgba(187, 134, 252, 0.5) !important;
    }

    /* Mensajes de éxito/error góticos */
    .stAlert {
        background-color: #1a1a1a !important;
        border: 1px solid #440000 !important;
        color: #e0e0e0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADO DE SESIÓN ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'seccion' not in st.session_state:
    st.session_state.seccion = "Menu"

# --- LOGICA DE LOGIN GÓTICO ---
if not st.session_state.autenticado:
    st.title("⚰️ Portal de las Sombras Chikitines")
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        st.markdown('<div class="card-goth"><h3>Identifícate, Mortal</h3><p>Solo los elegidos pueden pasar...</p>', unsafe_allow_html=True)
        with st.form("login_form"):
            user = st.text_input("Nombre del Alma:", placeholder="Ej. Admin")
            pw = st.text_input("Conjuro de Acceso:", type="password", placeholder="********")
            
            submit = st.form_submit_button("📜 Invocar Acceso")
            if submit:
                # Validaciones originales de tu código
                if user == "Admin" and pw == "Admin2026":
                    st.session_state.autenticado = True
                    st.success("🎉 El conjuro es correcto. Pasa, Admin.")
                    st.rerun()
                else:
                    st.error("❌ NO NO NO, conjuro incorrecto. Inténtalo de nuevo, tilín.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- PANEL PRINCIPAL (DASHBOARD GÓTICO) ---
else:
    # Mostrar el menú principal si no se ha seleccionado una sección
    if st.session_state.seccion == "Menu":
        st.title("🏰 Castillo Chikitines - Panel de Control")
        st.write("---")
        
        # Estructura de Cards Góticas
        c1, c2, c3 = st.columns(3)
        
        with c1:
            # Card 1: Números (Icono Calavera)
            st.markdown('<div class="card-goth"><h3>💀 El Juicio del Número</h3><p>Verifica si el número es par o impar, positivo o negativo.</p></div>', unsafe_allow_html=True)
            if st.button("⚖️ Iniciar Juicio", use_container_width=True, key="btn_num"):
                st.session_state.seccion = "Clasificador"
                st.rerun()

        with c2:
            # Card 2: Edad (Icono Gárgola/Castillo)
            st.markdown('<div class="card-goth"><h3>🏰 Edictos de Edad</h3><p>Consulta tus permisos reales según los años que has sobrevivido.</p></div>', unsafe_allow_html=True)
            if st.button("📜 Ver Edictos", use_container_width=True, key="btn_edad"):
                st.session_state.seccion = "Edad"
                st.rerun()

        with c3:
            # Card 3: Tarifas (Icono Cofre)
            st.markdown('<div class="card-goth"><h3>🪙 Cofre de Tributos</h3><p>Calcula el tributo final con los descuentos de la agencia.</p></div>', unsafe_allow_html=True)
            if st.button("💰 Calcular Tributo", use_container_width=True, key="btn_tarifas"):
                st.session_state.seccion = "Tarifas"
                st.rerun()
        
        st.write("---")
        col_out1, col_out2, col_out3 = st.columns([1,1,1])
        with col_out2:
            if st.button("👋 Desvanecerse (Salir)", use_container_width=True):
                st.session_state.autenticado = False
                st.rerun()

    # --- SECCIONES INDIVIDUALES (DESBLOQUEADAS AL PICAR LA CARD) ---
    
    # 1. CLASIFICADOR
    elif st.session_state.seccion == "Clasificador":
        st.button("⬅️ Regresar al Castillo", on_click=lambda: st.session_state.update({"seccion": "Menu"}))
        st.header("💀 El Juicio del Número")
        st.write("---")
        
        with st.container():
            num = st.number_input("Ingresa el número a juzgar:", step=1, value=0)
            if st.button("⚖️ Dictar Sentencia"):
                # Lógica original
                if num == 0: pos = "Es el Cero Absoluto."
                else: pos = "Es Positivo." if num > 0 else "Es Negativo."
                par = "Es Par." if num % 2 == 0 else "Es Impar."
                
                st.markdown(f"### SENTENCIA:\n* **Naturaleza:** {pos}\n* **Paridad:** {par}")

    # 2. EDAD
    elif st.session_state.seccion == "Edad":
        st.button("⬅️ Regresar al Castillo", on_click=lambda: st.session_state.update({"seccion": "Menu"}))
        st.header("🏰 Edictos de Edad y Permisos")
        st.write("---")
        
        edad = st.number_input("Ingresa los años que has sobrevivido:", min_value=0, max_value=120, value=25)
        if st.button("📜 Leer Edicto Real"):
            # Lógica original
            if edad < 0:
                st.error("Tu edad no puede ser negativa mi bro (cómo vas a tener -0 años).")
            elif edad <= 12:
                st.warning("Eres un escuincle, no puedes registrarte en el libro real.")
            elif 13 <= edad < 18:
                st.info("Eres un adolescente, puedes registrarte pero no puedes manejar carruajes ni hacer compras sin tutor chaval.")
            elif edad >= 21:
                st.success("🎉 Tienes el servicio VIP :D puedes hacer lo que quieras sin restricciones en el reino.")
            elif 18 <= edad :
                st.success("Mayor de edad: puedes conducir carruajes y hacer compras sin Tutor.")

    # 3. TARIFAS
    elif st.session_state.seccion == "Tarifas":
        st.button("⬅️ Regresar al Castillo", on_click=lambda: st.session_state.update({"seccion": "Menu"}))
        st.header("🪙 Cofre de Tributos (Calculadora)")
        st.write("---")
        
        tarifa_base = 200.0
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            edad_t = st.number_input("Edad para el diezmo:", 0, 120, 30)
            dia = st.slider("Día del ciclo lunar (1=Lun... 7= Dom):", 1, 7, 1)
        with col_t2:
            estudiante = st.checkbox("¿Eres aprendiz (estudiante)?")
            miembro = st.checkbox("¿Eres miembro del aquelarre (club)?")
            pago = st.radio("Método de ofrenda:", ["T= Tarjeta Arcanos", "E= Efectivo Oro"], index=1)
            metodo_pago = pago[0]
        
        if st.button("💰 Calcular Tributo Final"):
            recargo = 0.0
            descuento_total = 0.0
            
            # Recargos y descuentos originales
            if dia >= 6: recargo = tarifa_base * 0.10 # Recargo fin de ciclo
            if edad_t <= 12: descuento_total += tarifa_base * 0.50
            elif 13 <= edad_t < 17: descuento_total += tarifa_base * 0.20
            elif edad_t >= 65: descuento_total += tarifa_base * 0.30
            if estudiante and edad_t >= 13: descuento_total += tarifa_base * 0.15
            if miembro: descuento_total += tarifa_base * 0.10
            if metodo_pago == 'E': descuento_total += tarifa_base * 0.05
            
            # Límite de descuento original
            if descuento_total > tarifa_base * 0.60:
                st.warning("⚠️ El descuento total no puede exceder el 60% del diezmo base.")  
                descuento_total = tarifa_base * 0.60          
            
            tarifa_final = tarifa_base + recargo - descuento_total
            
            st.markdown("### OFRENDA CALCULADA:")
            col_res1, col_res2, col_res3 = st.columns(3)
            col_res1.metric("Diezmo Base", f"${tarifa_base:.2f}")
            col_res2.metric("Recargo Lunar", f"${recargo:.2f}")
            col_res3.metric("Tributo Final", f"${tarifa_final:.2f}", delta=f"-${descuento_total:.2f} desc", delta_color="normal")