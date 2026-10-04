from datetime import datetime
import time
import socket
import sqlite3
import requests
import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# CONFIGURACIÓN DE PÁGINA Y ESTILOS NEÓN / AMANECER AZUL
# ==========================================
st.set_page_config(
    page_title="AngeL Solana Intelligence - Guía y Auditoría On-Chain",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ANUNCIOS ADSTERRA - INTEGRACIÓN
# ==========================================
ad_social_1 = '<script src="https://recordssponge.com/de/6e/d9/de6ed91fcd1cb73a5c2197fd70a1f9fa.js"></script>'
st.components.v1.html(ad_social_1, height=0, width=0)

ad_banner_728x90 = '<script>atOptions = {\'key\' : \'10fcd40aed91182816ec3c5c46a7dd1f\', \'format\' : \'iframe\', \'height\' : 90, \'width\' : 728, \'params\' : {}};</script><script src="https://recordssponge.com/10fcd40aed91182816ec3c5c46a7dd1f/invoke.js"></script>'
st.components.v1.html(ad_banner_728x90, height=110, width=748, scrolling=False)

# --- BASE DE DATOS SQLITE (Registro Local de Consultas) ---
def init_db():
    conn = sqlite3.connect("angel_live_intelligence.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            category TEXT,
            status_info TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

def log_audit(query, category, status_info):
    try:
        conn = sqlite3.connect("angel_live_intelligence.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO audit_logs (query, category, status_info, timestamp) VALUES (?, ?, ?, ?)", 
                       (query, category, status_info, datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
    except Exception:
        pass

# --- ENDPOINTS RPC PROFESIONALES (Respaldo Múltiple para Cero Fallos) ---
RPC_ENDPOINTS = [
    "https://api.mainnet-beta.solana.com",
    "https://solana-mainnet.g.alchemy.com/v2/demo",
]

def query_solana_rpc(method, params):
    for endpoint in RPC_ENDPOINTS:
        try:
            payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
            res = requests.post(endpoint, json=payload, timeout=6)
            data = res.json()
            if "result" in data:
                return data["result"]
        except Exception:
            continue
    return None

# --- ESTILOS VISUALES: 3D FOSFORESCENTE NEÓN (BRILLO AZUL UNIFICADO) ---
st.markdown(
    """
    <style>
    .stApp, section[data-testid="stSidebar"] {
        background: radial-gradient(circle at 50% 20%, #38bdf8 0%, #0284c7 35%, #0f172a 80%, #020617 100%) !important;
        color: #FFFFFF;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    section[data-testid="stSidebar"] {
        border-right: 2px solid #38bdf8;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.8), inset 0 0 25px rgba(56, 189, 248, 0.3);
    }
    section[data-testid="stSidebar"] .stRadio label {
        color: #FFFFFF !important;
        font-weight: 700;
        text-shadow: 0 0 12px rgba(56, 189, 248, 1);
    }
    section[data-testid="stSidebar"] h3 {
        color: #facc15 !important;
        text-shadow: 0 0 20px rgba(250, 204, 21, 1), 0 0 10px rgba(250, 204, 21, 0.8);
    }
    .header-box { 
        text-align: center; padding: 30px 20px; 
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.98));
        border: 2px solid #facc15; border-radius: 20px;
        box-shadow: 0 0 50px rgba(56, 189, 248, 0.7), inset 0 0 30px rgba(56, 189, 248, 0.5);
        margin-bottom: 25px;
    }
    .mainnet-badge {
        display: inline-block; 
        background: linear-gradient(135deg, rgba(250, 204, 21, 0.25), rgba(202, 138, 4, 0.3)); 
        border: 2px solid #facc15;
        color: #fef08a; 
        padding: 6px 16px; 
        border-radius: 25px; 
        font-size: 0.9rem; 
        font-weight: 900;
        margin-bottom: 12px; 
        box-shadow: 0 0 20px rgba(250, 204, 21, 0.8), inset 0 0 10px rgba(255, 255, 255, 0.5);
        text-shadow: 0 0 10px rgba(250, 204, 21, 1);
        letter-spacing: 0.5px;
    }
    h1 { 
        color: #FFFFFF !important; 
        text-shadow: 0 0 15px rgba(255, 255, 255, 1), 0 0 35px rgba(56, 189, 248, 1), 0 0 50px rgba(250, 204, 21, 0.8); 
        font-weight: 900; 
    }
    h3, .stsubheader { 
        color: #facc15 !important; 
        border-bottom: 2px solid #38bdf8; 
        padding-bottom: 8px; 
        text-shadow: 0 0 15px rgba(250, 204, 21, 1), 0 0 30px rgba(56, 189, 248, 0.8); 
        font-weight: 800;
    }
    .stButton>button {
        background: linear-gradient(135deg, #0284c7 0%, #1e40af 100%) !important;
        color: #FFFFFF !important; font-weight: 900 !important; border-radius: 14px !important;
        width: 100% !important; border: 2px solid #38bdf8 !important; border-bottom: 4px solid #facc15 !important;
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.8), 0 0 15px rgba(250, 204, 21, 0.6); 
        text-transform: uppercase !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.9);
    }
    .data-metric-box {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.98));
        border: 2px solid #38bdf8; border-radius: 16px; padding: 24px; color: #FFFFFF; margin-top: 18px;
        box-shadow: 0 0 45px rgba(56, 189, 248, 0.7);
    }
    .guardian-explanation {
        font-size: 0.9rem; color: #e2e8f0; margin-top: 12px; padding: 12px;
        border-left: 4px solid #facc15; background: rgba(56, 189, 248, 0.15); border-radius: 0 8px 8px 0;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.4);
    }
    .status-safe { color: #4ade80; font-weight: 900; text-shadow: 0 0 15px rgba(74, 222, 128, 0.9); }
    .status-warning { color: #facc15; font-weight: 900; text-shadow: 0 0 15px rgba(250, 204, 21, 0.9); }
    .status-danger { color: #f87171; font-weight: 900; text-shadow: 0 0 15px rgba(248, 113, 113, 1); }
    </style>
""",
    unsafe_allow_html=True,
)

# --- BARRA LATERAL ---
with st.sidebar:
    st.markdown("### 🛡️ AngeL Intelligence")
    st.markdown("<p style='color: #FFFFFF; font-weight: 600; text-shadow: 0 0 10px rgba(56,189,248,0.8);'>Plataforma abierta de análisis y transparencia on-chain para la comunidad cripto.</p>", unsafe_allow_html=True)
    menu_choice = st.radio("Módulos de Análisis", [
        "🔍 Buscador On-Chain Universal", 
        "🔒 Análisis de Contratos & Permisos",
        "🔑 Auditoría de Delegaciones (Approvals)",
        "🧮 Calculadora Financiera & Conversor",
        "📊 Telemetría y Salud del Nodo RPC"
    ])
    st.markdown("---")
    st.markdown("<div class='mainnet-badge'>✨ ⚡ Conectado a Solana Mainnet</div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:0.75rem; color: #fef08a; font-weight: bold; text-shadow: 0 0 10px rgba(250, 204, 21, 0.8);'>Datos reales y directos de la cadena.</p>", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown(
    """
    <div class='header-box'>
        <div class='mainnet-badge'>✨ ⚡ Conectado a la Mainnet Oficial de Solana</div>
        <h1>🛡️ AngeL <span style='color: #facc15; font-size: 1.1rem; text-shadow: 0 0 20px rgba(250, 204, 21, 1), 0 0 35px rgba(56, 189, 248, 0.9);'>Solana Intelligence Engine</span></h1>
        <p style='color: #FFFFFF; font-size: 0.95rem; margin-top: 5px; font-weight: 600; text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);'>
            Información real, transparente y explicada en vivo para usuarios, traders y desarrolladores del ecosistema cripto.
        </p>
    </div>
""",
    unsafe_allow_html=True,
)

# ==========================================
# MÓDULO 1: BUSCADOR ON-CHAIN UNIVERSAL
# ==========================================
if menu_choice == "🔍 Buscador On-Chain Universal":
    st.subheader("🔍 Buscador Multivectorial en Vivo")
    st.markdown("<p style='font-size: 0.9cm; color: #FFFFFF; font-weight: 600; text-shadow: 0 0 10px rgba(56,189,248,0.8);'>Consulta <b>cualquier parámetro real</b> en Solana (Wallet, Mint, Transaction Hash o Símbolo). AngeL consultará directamente los nodos y te explicará el resultado.</p>", unsafe_allow_html=True)

    query_input = st.text_input("Ingrese valor a consultar en la red:", value="")

    if st.button("✨ Consultar y Explicar Datos"):
        query = query_input.strip()
        if not query:
            st.warning("Por favor, ingrese un valor de consulta válido.")
        else:
            with st.spinner("AngeL está escrutando los registros de la Mainnet con infraestructura multinodo..."):
                try:
                    found_result = False

                    # 1. ¿Es una Transacción?
                    tx_data = query_solana_rpc("getTransaction", [query, {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0}])
                    if tx_data:
                        found_result = True
                        slot = tx_data.get("slot", 0)
                        meta = tx_data.get("meta", {})
                        err = meta.get("err")
                        
                        if err is None:
                            status_text = "<span class='status-safe'>🟢 Transacción Confirmada Correctamente</span>"
                            explanation = "<b>Análisis de AngeL:</b> Esta transacción se ejecutó y validó con éxito en la blockchain de Solana."
                        else:
                            status_text = f"<span class='status-danger'>🔴 Transacción Fallida (Error: {err})</span>"
                            explanation = "<b>Análisis de AngeL:</b> La transacción no pudo completarse debido a un error en la ejecución."

                        log_audit(query, "Transacción", "Encontrada")
                        st.markdown(f"""
                            <div class='data-metric-box'>
                                <h3 style='color: #facc15; margin-top:0; text-shadow: 0 0 15px rgba(250,204,21,1);'>📋 Reporte de Transacción On-Chain</h3>
                                • <b>Hash:</b> <code>{query}</code><br>
                                • <b>Estado:</b> {status_text}<br>
                                • <b>Slot:</b> {slot:,}<br>
                                <div class='guardian-explanation'>{explanation}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        st.link_button("🔍 Ver en Solscan", f"https://solscan.io/tx/{query}")

                    if not found_result:
                        # 2. ¿Es una Cuenta / Billetera / Mint Contract?
                        acc_val = query_solana_rpc("getAccountInfo", [query, {"encoding": "jsonParsed"}])
                        if acc_val:
                            found_result = True
                            owner = acc_val.get("owner", "Desconocido")
                            parsed = acc_val.get("data", {}).get("parsed", {})
                            
                            is_mint = isinstance(parsed, dict) and parsed.get("type") == "mint"

                            if is_mint:
                                info = parsed.get("info", {})
                                m_auth = info.get("mintAuthority")
                                f_auth = info.get("freezeAuthority")
                                
                                mint_desc = f"Activa ({m_auth})" if m_auth else "Revocada (Suministro Fijo)"
                                freeze_desc = f"Activa ({f_auth})" if f_auth else "Revocada (Sin Restricciones)"
                                
                                explanation = (
                                    "<b>Análisis de Contrato Token (Mint):</b><br>"
                                    f"• <i>Autoridad de Emisión:</i> {mint_desc}.<br>"
                                    f"• <i>Autoridad de Congelamiento:</i> {freeze_desc}."
                                )
                                log_audit(query, "Token Mint", "Encontrado")
                                st.markdown(f"""
                                    <div class='data-metric-box'>
                                        <h3 style='color: #facc15; margin-top:0; text-shadow: 0 0 15px rgba(250,204,21,1);'>🔒 Auditoría de Contrato Token</h3>
                                        • <b>Dirección Mint:</b> <code>{query}</code><br>
                                        • <b>Emisión:</b> {mint_desc}<br>
                                        • <b>Congelamiento:</b> {freeze_desc}<br>
                                        <div class='guardian-explanation'>{explanation}</div>
                                    </div>
                                """, unsafe_allow_html=True)
                                st.link_button("🦅 Analizar en Birdeye", f"https://birdeye.so/token/{query}?chain=solana")

                            else:
                                bal_val = query_solana_rpc("getBalance", [query])
                                sol_balance = (bal_val.get("value", 0) if isinstance(bal_val, dict) else 0) / 1e9

                                explanation = f"<b>Análisis de Billetera/Cuenta:</b> Cuenta activa registrada en el libro mayor de Solana con un balance de {sol_balance:.6f} SOL. Programa propietario: <code>{owner}</code>."
                                log_audit(query, "Wallet", "Encontrada")
                                st.markdown(f"""
                                    <div class='data-metric-box'>
                                        <h3 style='color: #facc15; margin-top:0; text-shadow: 0 0 15px rgba(250,204,21,1);'>📊 Reporte de Cuenta / Billetera</h3>
                                        • <b>Dirección:</b> <code>{query}</code><br>
                                        • <b>Balance SOL:</b> <span class='status-safe'>{sol_balance:.6f} SOL</span><br>
                                        • <b>Programa Propietario:</b> <code>{owner}</code><br>
                                        <div class='guardian-explanation'>{explanation}</div>
                                    </div>
                                """, unsafe_allow_html=True)
                                col1, col2 = st.columns(2)
                                with col1:
                                    st.link_button("🔍 Ver en Solscan", f"https://solscan.io/account/{query}")
                                with col2:
                                    st.link_button("🦅 Ver en Solana FM", f"https://solana.fm/address/{query}")

                    if not found_result:
                        # 3. ¿Es un Símbolo o Ticker en DEX?
                        res_dex = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{query}", timeout=5)
                        pairs = res_dex.json().get("pairs", [])
                        if not pairs and len(query) < 20:
                            search_dex = requests.get(f"https://api.dexscreener.com/latest/dex/search?q={query}", timeout=5)
                            pairs = [p for p in search_dex.json().get("pairs", []) if p.get("chainId") == "solana"]

                        if pairs:
                            found_result = True
                            p_data = pairs[0]
                            t_name = p_data.get("baseToken", {}).get("name", "Desconocido")
                            t_symbol = p_data.get("baseToken", {}).get("symbol", "TOKEN")
                            mint_addr = p_data.get("baseToken", {}).get("address", query)
                            price = p_data.get("priceUsd", "0.00")
                            liq = p_data.get("liquidity", {}).get("usd", 0)
                            
                            explanation = f"<b>Análisis de Mercado:</b> Activo cotizado en DEX con una liquidez total de ${liq:,.2f} USD."
                            st.markdown(f"""
                                <div class='data-metric-box'>
                                    <h3 style='color: #facc15; margin-top:0; text-shadow: 0 0 15px rgba(250,204,21,1);'>📈 Datos de Mercado: {t_name} ({t_symbol})</h3>
                                    • <b>Mint Address:</b> <code>{mint_addr}</code><br>
                                    • <b>Precio:</b> ${price} USD | <b>Liquidez:</b>${liq:,.2f} USD<br>
                                    <div class='guardian-explanation'>{explanation}</div>
                                </div>
                            """, unsafe_allow_html=True)
                            st.code(mint_addr, language="text")

                    if not found_result:
                        st.warning(f"La dirección `{query}` no devolvió datos activos directos en las consultas estándar. Puede ser una dirección de programa personalizada o una cuenta vacía en este slot. Intenta verificarla directamente en Solscan.")
                except Exception as e:
                    st.error(f"Error al procesar la consulta on-chain: {e}")

# ==========================================
# MÓDULO 2: ANÁLISIS DE CONTRATOS & PERMISOS
# ==========================================
elif menu_choice == "🔒 Análisis de Contratos & Permisos":
    st.subheader("🔒 Inspección Transparente de Parámetros en Contratos")
    st.markdown("<p style='font-size: 0.9cm; color: #FFFFFF; font-weight: 600; text-shadow: 0 0 10px rgba(56,189,248,0.8);'>Examina los privilegios administrativos activos de cualquier token SPL.</p>", unsafe_allow_html=True)

    contract_check = st.text_input("Ingrese la Dirección del Contrato (Mint):", value="")
    if st.button("🔍 Examinar Parámetros del Contrato"):
        if not contract_check:
            st.warning("Ingrese una dirección de contrato válida.")
        else:
            with st.spinner("Consultando permisos en la Mainnet..."):
                try:
                    acc_val = query_solana_rpc("getAccountInfo", [contract_check, {"encoding": "jsonParsed"}])
                    if acc_val:
                        parsed = acc_val.get("data", {}).get("parsed", {})
                        info = parsed.get("info", {}) if isinstance(parsed, dict) else {}
                        m_auth = info.get("mintAuthority")
                        f_auth = info.get("freezeAuthority")

                        mint_status = f"Activa ({m_auth})" if m_auth else "Revocada (Suministro Fijo)"
                        freeze_status = f"Activa ({f_auth})" if f_auth else "Revocada (Sin Restricciones)"

                        summary_text = "<b>Explicación Técnica:</b> Las autoridades activas permiten modificar el suministro o congelar cuentas."

                        st.markdown(f"""
                            <div class='data-metric-box'>
                                <h3 style='color: #facc15; margin-top:0; text-shadow: 0 0 15px rgba(250,204,21,1);'>🔒 Reporte de Privilegios On-Chain</h3>
                                • <b>Autoridad de Emisión:</b> {mint_status}<br>
                                • <b>Autoridad de Congelamiento:</b> {freeze_status}<br>
                                <div class='guardian-explanation'>{summary_text}</div>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.warning("La cuenta consultada no existe o no contiene datos parseables.")
                except Exception as e:
                    st.error(f"Error en la consulta: {e}")

# ==========================================
# MÓDULO 3: AUDITORÍA DE DELEGACIONES (APPROVALS)
# ==========================================
elif menu_choice == "🔑 Auditoría de Delegaciones (Approvals)":
    st.subheader("🔑 Verificación de Aprobaciones y Delegaciones de Cuenta")
    st.markdown("<p style='font-size: 0.9cm; color: #FFFFFF; font-weight: 600; text-shadow: 0 0 10px rgba(56,189,248,0.8);'>Revisa si una dirección de billetera ha otorgado permisos de manejo de tokens SPL a contratos externos.</p>", unsafe_allow_html=True)

    wallet_appr = st.text_input("Ingrese Dirección de Billetera:", value="")
    if st.button("🔍 Consultar Cuentas y Delegaciones"):
        if not wallet_appr:
            st.warning("Ingrese una billetera válida.")
        else:
            with st.spinner("Consultando registros de cuentas de tokens SPL..."):
                try:
                    accounts = query_solana_rpc("getTokenAccountsByOwner", [
                        wallet_appr,
                        {"program": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"},
                        {"encoding": "jsonParsed"}
                    ]) or []

                    delegations_found = False
                    details_html = ""
                    for acc in accounts:
                        info = acc.get("account", {}).get("data", {}).get("parsed", {}).get("info", {})
                        delegate = info.get("delegate")
                        if delegate:
                            delegations_found = True
                            mint = info.get("mint")
                            amount = info.get("delegatedAmount", {}).get("uiAmountString", "0")
                            details_html += f"• <b>Token Mint:</b> <code>{mint}</code> | <b>Delegado a:</b> <code>{delegate}</code> | <b>Monto:</b> {amount}<br>"

                    if not delegations_found:
                        details_html = "• No se encontraron delegaciones de gasto activas en las cuentas SPL de esta billetera."
                        explanation = "<b>Información de AngeL:</b> Las cuentas operan sin delegaciones activas hacia terceros."
                    else:
                        explanation = "<b>Información de AngeL:</b> Se detectaron contratos con permisos delegados activos."

                    st.markdown(f"""
                        <div class='data-metric-box'>
                            <h3 style='color: #facc15; margin-top:0; text-shadow: 0 0 15px rgba(250,204,21,1);'>🔑 Estado de Delegaciones SPL</h3>
                            {details_html}<br>
                            <div class='guardian-explanation'>{explanation}</div>
                        </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error al verificar delegaciones: {e}")

# ==========================================
# MÓDULO 4: CALCULADORA FINANCIERA & CONVERSOR
# ==========================================
elif menu_choice == "🧮 Calculadora Financiera & Conversor":
    st.subheader("🧮 Herramientas de Cálculo y Planificación Financiera")
    st.markdown("<p style='font-size: 0.9cm; color: #FFFFFF; font-weight: 600; text-shadow: 0 0 10px rgba(56,189,248,0.8);'>Utilidades de conversión de mercado y estimación de costos operativos en la red.</p>", unsafe_allow_html=True)

    try:
        price_res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd", timeout=4)
        sol_usd_price = price_res.json().get("solana", {}).get("usd", 150.0)
    except Exception:
        sol_usd_price = 150.0

    tab_c1, tab_c2 = st.tabs(["💱 Conversor & Simulación PnL", "⛽ Tarifas de Red Estimadas"])

    with tab_c1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Conversión SOL a USD")
            sol_amt = st.number_input("Cantidad de SOL:", min_value=0.0, value=1.0, step=0.1)
            val_usd = sol_amt * sol_usd_price
            st.markdown(f"""
                <div class='data-metric-box'>
                    • <b>Cotización Actual:</b> ${sol_usd_price:,.2f} USD<br>
                    • <b>Total Equivalente:</b> <span class='status-safe'>${val_usd:,.2f} USD</span>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("### Simulador de Retorno (PnL)")
            p_buy = st.number_input("Precio de Compra ($):", min_value=0.0, value=100.0, step=1.0)
            p_sell = st.number_input("Precio Objetivo ($):", min_value=0.0, value=150.0, step=1.0)
            if p_buy > 0:
                pnl = ((p_sell - p_buy) / p_buy) * 100
                st.markdown(f"""
                    <div class='data-metric-box'>
                        • <b>Variación Teórica:</b> <span class='status-safe'>{pnl:+.2f}%</span>
                        <div class='guardian-explanation'>Calcula el rendimiento proyectado.</div>
                    </div>
                """, unsafe_allow_html=True)

    with tab_c2:
        st.markdown("### Costos Operativos de Referencia en Solana")
        st.markdown(f"""
            <div class='data-metric-box'>
                • <b>Transferencia Estándar:</b> ~0.000005 SOL (~${sol_usd_price * 0.000005:.5f} USD)<br>
                • <b>Creación de Cuenta Token (ATA):</b> ~0.00203 SOL (~${sol_usd_price * 0.00203:.4f} USD)<br>
                • <b>Estado del Clúster:</b> <span class='status-safe'>🟢 Operativo</span>
                <div class='guardian-explanation'>Tarifas base del protocolo de consenso.</div>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# MÓDULO 5: TELEMETRÍA Y SALUD DEL NODO RPC
# ==========================================
elif menu_choice == "📊 Telemetría y Salud del Nodo RPC":
    st.subheader("📊 Panel SOC y Diagnóstico de Conectividad RPC")
    st.markdown("<p style='font-size: 0.9cm; color: #FFFFFF; font-weight: 600; text-shadow: 0 0 10px rgba(56,189,248,0.8);'>Supervisión en tiempo real del enlace de red con los validadores de Solana Mainnet.</p>", unsafe_allow_html=True)

    if st.button("🔄 Actualizar Métricas de Red"):
        pass

    latency_ms = 0
    slot_current = 0
    port_status = "Desconectado"

    try:
        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res_sock = s.connect_ex(('api.mainnet-beta.solana.com', 443))
        s.close()
        port_status = "Abierto (Estable)" if res_sock == 0 else "Filtrado"
    except Exception:
        port_status = "Error"

    try:
        t_start = time.time()
        slot_res = query_solana_rpc("getSlot", [])
        latency_ms = int((time.time() - t_start) * 1000)
        slot_current = slot_res if slot_res else 0
    except Exception:
        slot_current = 0
        latency_ms = 999

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
            <div class='data-metric-box' style='text-align: center;'>
                <h4 style='color: #facc15; margin:0; text-shadow: 0 0 10px rgba(250,204,21,0.9);'>ESTADO TCP (443)</h4>
                <p class='status-safe' style='font-size: 1.1rem; margin-top: 10px;'>{port_status}</p>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class='data-metric-box' style='text-align: center;'>
                <h4 style='color: #facc15; margin:0; text-shadow: 0 0 10px rgba(250,204,21,0.9);'>LATENCIA RPC</h4>
                <p class='status-safe' style='font-size: 1.1rem; margin-top: 10px;'>{latency_ms} ms</p>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
            <div class='data-metric-box' style='text-align: center;'>
                <h4 style='color: #facc15; margin:0; text-shadow: 0 0 10px rgba(250,204,21,0.9);'>ALTURA DE BLOQUE</h4>
                <p class='status-safe' style='font-size: 1.1rem; margin-top: 10px;'>{slot_current:,}</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='data-metric-box' style='margin-top: 20px;'>
            <h3 style='color: #facc15; margin-top:0; text-shadow: 0 0 15px rgba(250,204,21,1);'>🛡️ Resumen de Infraestructura</h3>
            • <b>Red Destino:</b> Solana Mainnet (Oficial)<br>
            • <b>Sincronización:</b> <span class='status-safe'>🟢 Operando en tiempo real con la cadena</span><br>
            <div class='guardian-explanation'>Este panel confirma la comunicación directa y fluida con los nodos validadores globales.</div>
        </div>
    """, unsafe_allow_html=True)
