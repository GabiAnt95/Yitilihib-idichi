import streamlit as st

st.set_page_config(page_title='Yi ti li hibíi dichi', page_icon="mimimi.ico", layout="wide")

frase_repipi = st.text_area("Introducir frase repipi: ")

def repipi_plus_transformer(frase):
    
    frase = "\n" + "\n\n".join([e for e in frase.split('\n') if len(e) > 0 and e[0] != '[']) + "\n"

    return "".join([e.replace(e, 'i') if e in 'aeiou' else
                    e.replace(e, 'I') if e in 'AEIOU' else
                    e.replace(e, 'í') if e in 'áéíóú' else
                    e.replace(e, 'Í') if e in 'ÁÉÍÓÚ' else
                    e for e in frase])
    
output = repipi_plus_transformer(frase_repipi).replace('\n', ' ')[1:]
    
repipi_button = st.button("Convertir frase a repipi PLUS: ")

if repipi_button:
    st.success("Well done!", icon = "😫")
    frase_mimimi, img_mimimi = st.columns(2)
    with frase_mimimi:
        st.markdown(output)
    with img_mimimi:
        st.image('mimimi.gif')