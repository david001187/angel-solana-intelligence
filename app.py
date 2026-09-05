import requests
import pandas as pd
import streamlit as st

st.subheader("🪽 Escáner Global del Ecosistema Solana")
st.write("Explora memecoins, tokens y activos de toda la red Solana en tiempo real:")

@st.cache_data(ttl=30)
def fetch_live_solana_tokens():
    try:
        # Consulta a la API pública de DexScreener para tokens/pairs recientes en Solana
        url = "https://api.dexscreener.com/latest/dex/tokens/solana"
        # O la API de pares en tendencia de Solana:
        response = requests.get("https://api.dexscreener.com/token-profiles/latest/v1", timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Filtrar solo activos en la red de Solana
            sol_tokens = [item for item in data if item.get("chainId") == "solana"]
            return sol_tokens
    except Exception as e:
        st.error(f"Error al sincronizar datos en vivo: {e}")
        return []

tokens = fetch_live_solana_tokens()

if tokens:
    data_list = []
    for t in tokens[:10]: # Muestra los 10 principales tokens en vivo
        data_list.append({
            "Token": t.get("tokenAddress", "N/A"),
            "Símbolo / URL": t.get("url", "N/A"),
            "Descripción": t.get("description", "Sin descripción")[:50] + "..."
        })
    df = pd.DataFrame(data_list)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Sincronizando flujo global de tokens en Solana (Reintentando conexión con la red)...")
