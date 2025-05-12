import streamlit as st

st.set_page_config(page_title="Ecos del Olvido", layout="centered")
st.title("🌸 Ecos del Olvido - 20 K-Dramas")
st.markdown("Explora emociones a través de 20 historias que marcaron el alma...")

kdrama_opciones = {
    "Escalera al Cielo": ("kdrama_1.png", "El amor eterno no se detiene ante la muerte."),
    "Goblin": ("kdrama_2.png", "Incluso un ser inmortal anhela un final con sentido."),
    "Boys Over Flowers": ("kdrama_3.png", "A veces el amor florece en terrenos imposibles."),
    "My Love from the Star": ("kdrama_4.png", "La distancia entre planetas se acorta con el corazón."),
    "Crash Landing on You": ("kdrama_5.png", "El destino no necesita pasaporte."),
    "It's Okay to Not Be Okay": ("kdrama_6.png", "Sanar no es lineal, pero sí posible."),
    "True Beauty": ("kdrama_7.png", "La belleza verdadera se revela sin maquillaje."),
    "Start-Up": ("kdrama_8.png", "Los sueños no se programan, se viven."),
    "The Heirs": ("kdrama_9.png", "Herederos de riqueza, pero también de heridas."),
    "Hotel del Luna": ("kdrama_10.png", "Incluso los fantasmas tienen cuentas pendientes."),
    "Extraordinary Attorney Woo": ("kdrama_11.png", "La diferencia también es brillantez."),
    "Twenty-Five Twenty-One": ("kdrama_12.png", "Algunos amores solo existen en su tiempo perfecto."),
    "The Glory": ("kdrama_13.png", "A veces la venganza es la única justicia."),
    "Business Proposal": ("kdrama_14.png", "El amor no siempre sigue las reglas del contrato."),
    "Hometown Cha-Cha-Cha": ("kdrama_15.png", "La calma del mar guarda grandes revoluciones."),
    "Reborn Rich": ("kdrama_16.png", "La segunda oportunidad puede ser una herencia inesperada."),
    "Moon Lovers": ("kdrama_17.png", "En el pasado también se rompen corazones."),
    "Mr. Sunshine": ("kdrama_18.png", "Ser héroe es resistir, incluso sin capa."),
    "While You Were Sleeping": ("kdrama_19.png", "El futuro puede cambiar si lo sueñas distinto."),
    "Nevertheless": ("kdrama_20.png", "Aunque lo dudemos, el amor insiste.")
}

opcion = st.selectbox("Elige un K-Drama:", list(kdrama_opciones.keys()))

if opcion:
    imagen, frase = kdrama_opciones[opcion]
    st.image(imagen, use_column_width=True)
    st.markdown(f"**{frase}**")
