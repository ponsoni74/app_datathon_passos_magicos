import streamlit as st
import warnings
from utils.sidebar import show_sidebar

home_page = st.Page("pages/presentation.py", title="Apresentação, Objetivo e Indicadores", icon="🎯")
dashboards_page = st.Page("pages/datathon_specs.py", title="Orientações para elaboração dos trabalhos", icon="📋")
create_page = st.Page("pages/data_analytics.py", title="Storytelling dos impactos alcançados", icon="🔭")
model_scholarship = st.Page("pages/bolsa_estudos_model.py", title="Modelo Preditivo - Obtenção Bolsa de Estudos", icon="💡")
model_next_grade = st.Page("pages/ponto_virada_model.py", title="Modelo Preditivo - Alcance Ponto de Virada", icon="💡")

pg = st.navigation([home_page, dashboards_page, create_page, model_scholarship, model_next_grade])
st.set_page_config(layout="wide", page_title="Tech Challenge 5 | FIAP", page_icon=":material/edit:")
pg.run()


warnings.filterwarnings("ignore")

show_sidebar()