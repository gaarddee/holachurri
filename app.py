import streamlit as st

# Título de la página
st.title("hola guapa")

# Mensaje divertido
st.markdown("""
Hola nena, tan novia y sin guapo? anda ven paqui que te voy a enseñar un truco de magia
""")

# Almacenar el estado de los botones en session_state
if "show_truco" not in st.session_state:
    st.session_state.show_truco = False
if "show_gif" not in st.session_state:
    st.session_state.show_gif = False
if "show_balloons" not in st.session_state:
    st.session_state.show_balloons = False
if "show_message" not in st.session_state:
    st.session_state.show_message = False

# Botón "Ver truco de magia"
if st.button("Ver truco de magia"):
    st.session_state.show_truco = True

# Mostrar el truco de magia y el gif si el estado es verdadero
if st.session_state.show_truco:
    st.image("https://media.giphy.com/media/ZLoMb5AJ1SMZQgvMxo/giphy.gif?cid=790b7611j9v988dqow45iuuzc0jerdb922spx9a63t41a7pi&ep=v1_gifs_search&rid=giphy.gif&ct=g", caption="¿me harias el churro mas feliz del mundo?")

    # Botón "Si quiero, eres el mejor del mundo"
    if st.button("Si quiero, eres el mejor del mundo"):
        st.session_state.show_balloons = True
        st.session_state.show_gif = True
        st.session_state.show_message = True

# Mostrar globos, gif y mensaje de éxito si el estado es verdadero
if st.session_state.show_balloons:
    st.balloons()  # Mostrar globos
if st.session_state.show_gif:
    st.image("https://media.giphy.com/media/t6f2bNAjx7Bio/giphy.gif?cid=790b76110f7easqaznecin7eirh2u5rxmzz02epibkzx3cgb&ep=v1_gifs_search&rid=giphy.gif&ct=g", caption="celebración power reinger")  # Gif adicional
if st.session_state.show_message:
    st.success("no te arrepentiras nena, cuando quieras comemos y nos quedamos")  # Mensaje de éxito

# Botón "Mandar a la mierda"
if st.button("Mandar a la mierda"):  # Corregido: se cerraron las comillas
    st.title("Es el peor día de mi vida")
    st.markdown("""
    Levo media hora haciendo esta mierda y no me ha funcionado
    """)