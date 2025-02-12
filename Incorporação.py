import streamlit as st


st. title("Hacka Itaú Empresas")
st.subheader("Extrato")
col1 , col2 = st.columns(2 , gap = "medium")
col1.write("Jornada atual")
col2.embed_code = """<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="200" height="450" src="https://embed.figma.com/proto/OYgx6p20H1Y0dnoGkCmESh/Hacka-Empresas?node-id=1-15&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A16&embed-host=share" allowfullscreen></iframe>"""

st.components.v1.html(embed_code,height=500)



tab1 , tab2 = st.tabs(["Visão para o cliente " , "Visão para o operador"])
tab1.write("""
 # Visão do cliente
 - Esclarece muito bem os literais
 - Maior autonomia
           
           """)
tab2.write("""
 # Visão do operador
 - Visão limitada, precisa ir em várias rotas para localizar as informações
 - Em alguns casos precisa deduzir do que se refere os valores
""")
