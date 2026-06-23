import streamlit as st

st.set_page_config(
    page_title="💖 Una pregunta muy importante 💖",
    page_icon="💘"
)

# Estado de la aplicación
if "intentos_no" not in st.session_state:
    st.session_state.intentos_no = 0

st.title("🌹 Una pregunta muy especial 🌹")

st.markdown("""
### Estimada Nicol:

Espero que te encuentres muy bien.

Después de una profunda reflexión y de incontables momentos de felicidad a tu lado,
quisiera hacerte una pregunta muy importante:

# 💖 ¿Quieres ser mi novia? 💖
""")

mensajes_no = [
    "🙈 No",
    "🤔 ¿Segura?",
    "😅 ¿Muy segura?",
    "🥺 Piénsalo otra vez",
    "💖 Tómate tu tiempo y vuelve a pensar",
]

indice = min(st.session_state.intentos_no, len(mensajes_no) - 1)

col1, col2 = st.columns(2)

with col1:
    if st.button("💖 Sí 💖", use_container_width=True):
        st.balloons()
        st.success("""
🥰❤️ ¡Muchas gracias por tu respuesta!

Me hace muy feliz que hayas aceptado. 💖

🌹💕😊✨💘🥰😍

Prometo esforzarme cada día para seguir sacándote una sonrisa.
""")

with col2:
    if st.button(mensajes_no[indice], use_container_width=True):

        if st.session_state.intentos_no < len(mensajes_no) - 1:
            st.session_state.intentos_no += 1
            st.warning("😄 Creo que esa opción merece una segunda reflexión...")
            st.rerun()
        else:
            st.balloons()
            st.success("""
🥰❤️ ¡Muchas gracias por tu respuesta!

Después de una exhaustiva revisión del sistema,
hemos concluido que la respuesta correcta era:

💖 ¡Sí! 💖

Me hace muy feliz que hayas aceptado. 🌹❤️

😊💕✨🥰💘😍❤️🌹
""")
