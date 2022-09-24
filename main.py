import pandas as pd #importer des bibliothèques nécessaires
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")
#@st.cache #les titres, les données du dashboard
def get_data_from_excel(file): #définition de la fonction qui permet de lire un fichier excel
    data = pd.read_excel(
        io=file,
        engine="openpyxl",
    )
    return data

uploaded_file = st.file_uploader("Choose a file",type=['xlsx','csv']) #permettre à l'utilisateur d'entrer
#base de donnée
if uploaded_file is not None:


     # Can be used wherever a "file-like" object is accepted:
     df =get_data_from_excel(uploaded_file)
     L = list(df.columns) #les colonnes (pour les rendre sous le format de liste
     del L[0:2] #supprimer l'élément d'indice 0 et 1 /ne laisser que les variables qu'on veut visualiser
     st.sidebar.header("Filtrage:") #étudier la base de donnée pour chaque secteur

     secteur = st.sidebar.multiselect(
        "Selectionner le Secteur:",
        options=df["secteur"].unique()
     )

     df_selection = df.query( #construire une base de donnée suivant le secteur choisi
        '''secteur == @secteur '''
     )
     st.dataframe(df_selection)
     st.title(":bar_chart: dashboard")
     st.markdown("---")
     columns = st.multiselect( #choisir la variable qu'on veut visualiser/
         label='Choose variable(s) you want to display', options=L #choisir depuis la liste L prédéfinie en haut
     )
     fig_1 = px.line(df_selection, x = 'num société', y = columns) #graphe en ligne
     st.plotly_chart(fig_1, use_container_width=True)
     fig_2 = px.bar(df_selection, x = 'num société', y = columns,barmode = 'group')
     st.plotly_chart(fig_2, use_container_width=True)