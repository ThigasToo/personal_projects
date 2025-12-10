import streamlit as st
import pandas as pd
import psycopg2
from datetime import date

# --- CONFIGURAÇÃO DA CONEXÃO ---
# Coloque a URL do Neon.tech abaixo (entre as aspas)
DB_URL = "postgresql://neondb_owner:npg_7oPZcfaRsJL3@ep-long-snow-acc80dwv-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

def get_connection():
    return psycopg2.connect(DB_URL)

# --- TÍTULO E ESTILO ---
st.set_page_config(page_title="Gestão de Projetos", page_icon="📊")
st.title("🚀 Novo Reporte")

# --- CARREGAR DADOS DO BANCO (DROPDOWNS) ---
try:
    conn = get_connection()
    # Busca Clientes
    df_clientes = pd.read_sql("SELECT id, nome_cliente FROM clientes ORDER BY nome_cliente", conn)
    # Busca Indicadores
    df_indicadores = pd.read_sql("SELECT id, nome, unidade FROM indicadores ORDER BY nome", conn)
    conn.close()
except Exception as e:
    st.error(f"Erro ao conectar no banco: {e}")
    st.stop()

# --- FORMULÁRIO DE INPUT ---
with st.form("form_reporte"):
    col1, col2 = st.columns(2)
    
    with col1:
        # O usuário vê o Nome, mas o sistema pega o ID
        cliente_selecionado = st.selectbox("Cliente", df_clientes['nome_cliente'])
        # Acha o ID correspondente ao nome escolhido
        id_cliente = df_clientes[df_clientes['nome_cliente'] == cliente_selecionado]['id'].values[0]
        
        data_input = st.date_input("Data do Reporte", date.today())

    with col2:
        indicador_selecionado = st.selectbox("Indicador", df_indicadores['nome'])
        # Acha o ID e a Unidade correspondente
        linha_ind = df_indicadores[df_indicadores['nome'] == indicador_selecionado].iloc[0]
        id_indicador = int(linha_ind['id'])
        unidade_atual = linha_ind['unidade']

    st.divider()
    
    c1, c2 = st.columns(2)
    valor = c1.number_input(f"Valor Realizado ({unidade_atual})", step=0.01)
    meta = c2.number_input(f"Meta ({unidade_atual})", step=0.01)
    
    comentario = st.text_area("Comentário Executivo")
    
    submitted = st.form_submit_button("💾 Salvar Reporte no Banco de Dados")

    if submitted:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO reportes (cliente_id, indicador_id, data_report, valor, meta, comentario)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (int(id_cliente), id_indicador, data_input, valor, meta, comentario))
            conn.commit()
            cursor.close()
            conn.close()
            st.success(f"Sucesso! Dados de {cliente_selecionado} salvos na nuvem!")
        except Exception as e:
            st.error(f"Erro ao salvar: {e}")

# --- VISUALIZAÇÃO RÁPIDA ABAIXO (OPCIONAL) ---
st.divider()
st.subheader("Últimos Lançamentos Registrados")
conn = get_connection()
df_view = pd.read_sql("""
    SELECT c.nome_cliente, i.nome as indicador, r.valor, r.meta, r.data_report 
    FROM reportes r
    JOIN clientes c ON r.cliente_id = c.id
    JOIN indicadores i ON r.indicador_id = i.id
    ORDER BY r.id DESC LIMIT 5
""", conn)
st.dataframe(df_view)