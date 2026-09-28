from datetime import datetime
import sqlite3
import requests
import streamlit as str_lit
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE PÁGINA ---
str_lit.set_page_config(
    page_title=(
        "AngeL Solana Intelligence: Auditoría de Tokens, Contratos y"
        " Transacciones"
    ),
    page_icon="🪽",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- INICIALIZACIÓN DE BASE DE DATOS SQLITE PARA MÉTRICAS ---
def init_db():
    conn = sqlite3.connect("angel_metrics.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

def log_audit(query):
    try:
        conn = sqlite3.connect("angel_metrics.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO audit_logs (query, timestamp) VALUES (?, ?)", (query, datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
    except Exception:
        pass

str_lit.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at center, #1e3a8a 0%, #0c2340 100%) !important;
        color: #FFFFFF;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    .header-box { 
        text-align: center; 
        padding: 25px 20px; 
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.95), rgba(12, 35, 64, 0.98));
        border: 2px solid #FACC15;
        border-radius: 16px;
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.6), inset 0 0 20px rgba(250, 204, 21, 0.4);
        margin-bottom: 25px;
    }
    
    h1 { 
        color: #FFFFFF !important; 
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.9), 0 0 35px rgba(56, 189, 248, 1); 
        font-weight: 900; 
        font-size: 2.2rem; 
    }
    
    h3, .stsubheader { 
        color: #38BDF8 !important; 
        border-bottom: 2px solid #FACC15; 
        padding-bottom: 8px; 
        text-shadow: 0 0 12px rgba(56, 189, 248, 0.9);
    }

    .stButton>button, .stDownloadButton>button, .stLinkButton>a {
        background: linear-gradient(135deg, #38BDF8 0%, #1d4ed8 100%) !important;
        color: #FFFFFF !important; 
        font-weight: 900 !important; 
        border-top: 2px solid #FFFFFF !important;
        border-left: 2px solid #FFFFFF !important;
        border-right: 2px solid #1e40af !important;
        border-bottom: 4px solid #FACC15 !important; 
        border-radius: 12px !important;
        padding: 12px 20px !important; 
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.8), inset 0 0 12px rgba(255, 255, 255, 0.9) !important;
        transition: all 0.2s ease-in-out !important; 
        text-transform: uppercase !important; 
        width: 100% !important;
        text-align: center !important;
        text-decoration: none !important;
        display: inline-block !important;
        box-sizing: border-box !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 1);
    }
    .stButton>button:hover, .stDownloadButton>button:hover, .stLinkButton>a:hover {
        background: linear-gradient(135deg, #60a5fa 0%, #38BDF8 100%) !important;
        box-shadow: 0 0 35px rgba(250, 204, 21, 1), inset 0 0 18px rgba(255, 255, 255, 1) !important; 
        transform: translateY(-3px) !important;
    }

    .stTextInput>div>div>input {
        background-color: rgba(12, 35, 64, 0.95); 
        color: #FFFFFF;
        border: 2px solid #FFFFFF !important;
        border-radius: 10px; 
        padding: 14px;
        font-weight: bold;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.8), inset 0 0 12px rgba(56, 189, 248, 0.6);
    }
    .stTextInput>div>div>input:focus {
        border-color: #FACC15 !important;
        box-shadow: 0 0 30px rgba(250, 204, 21, 1), inset 0 0 15px rgba(255, 255, 255, 0.9);
    }

    .content-card {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.8), rgba(12, 35, 64, 0.95));
        border: 2px solid #38BDF8;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 18px;
        backdrop-filter: blur(12px);
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
    }

    .data-metric-box {
        background: linear-gradient(135deg, rgba(12, 35, 64, 0.98), rgba(30, 58, 138, 0.9));
        border: 2px solid #FACC15;
        border-radius: 14px;
        padding: 22px;
        color: #FFFFFF;
        margin-top: 18px;
        box-shadow: 0 0 35px rgba(250, 204, 21, 0.5), inset 0 0 20px rgba(56, 189, 248, 0.4);
    }

    .info-tooltip {
        font-size: 0.85rem;
        color: #e2e8f0;
        margin-top: 4px;
        margin-bottom: 14px;
        border-left: 3px solid #38BDF8;
        padding-left: 10px;
        background: rgba(56, 189, 248, 0.15);
        border-radius: 0 6px 6px 0;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.3);
    }

    .status-safe {
        color: #FACC15;
        font-weight: 900;
        text-shadow: 0 0 15px rgba(250, 204, 21, 1);
    }
    .status-active {
        color: #38BDF8;
        font-weight: 900;
        text-shadow: 0 0 15px rgba(56, 189, 248, 1);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- BARRA LATERAL ---
with str_lit.sidebar:
    str_lit.markdown("### 🪽 Panel de Control AngeL")
    str_lit.markdown("Sistema autónomo de inteligencia de contratos y auditoría on-chain en Solana.")
    
    menu_choice = str_lit.radio(
        "Navegación Principal",
        ["🔍 Buscador y Auditoría On-Chain"]
    )
    
    str_lit.markdown("---")
    str_lit.markdown("<p style='font-size:0.75rem; color:#93c5fd;'>Conectado a la red principal de Solana Mainnet-Beta.</p>", unsafe_allow_html=True)

# --- CABECERA 3D NEÓN ---
str_lit.markdown(
    """
    <div class='header-box'>
        <h1>🪽 AngeL <span style='color: #FACC15; font-size: 1.1rem; text-shadow: 0 0 20px rgba(250, 204, 21, 1);'>Solana Intelligence</span></h1>
        <p style='color: #FFFFFF; font-size: 0.95rem; margin-top: 5px; margin-bottom: 0; text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);'>
            Plataforma de Auditoría On-Chain 3D Universal: Análisis en tiempo real de cualquier token, contrato o transacción en Solana.
        </p>
    </div>
""",
    unsafe_allow_html=True,
)
str_lit.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN PRINCIPAL: BUSCADOR Y AUDITORÍA AVANZADA ---
str_lit.subheader("🔍 Buscador Universal y Auditoría On-Chain de Alto Rendimiento")
str_lit.markdown(
    "<p style='font-size: 0.9rem; color: #FFFFFF;'>Escribe el <b>nombre, símbolo o Mint address</b> de <u>cualquier token existente en Solana</u> en tiempo real. Obtén datos en vivo, direcciones para copiar y explicaciones claras en cada cartola.</p>",
    unsafe_allow_html=True,
)

target_input = str_lit.text_input(
    "Busca cualquier Token por Nombre, Símbolo, Mint o TXID:",
    value="BONK",
)

if str_lit.button("✨ Consultar Auditoría en Vivo con AngeL"):
    log_audit(target_input.strip())
    with str_lit.spinner("Escaneando el ecosistema global de Solana en tiempo real..."):
        raw_query = target_input.strip()
        query = raw_query

        if len(raw_query) < 32:
            try:
                search_res = requests.get(
                    f"https://api.dexscreener.com/latest/dex/search?q={raw_query}",
                    timeout=5,
                )
                solana_pairs = [
                    p
                    for p in search_res.json().get("pairs", [])
                    if p.get("chainId") == "solana"
                ]
                if solana_pairs:
                    query = solana_pairs[0].get("baseToken", {}).get(
                        "address", raw_query
                    )
            except Exception:
                pass

        if len(query) >= 80:
            str_lit.markdown("### 📌 Información Detallada de Transacción (TXID)")
            str_lit.code(query, language="text")
            try:
                rpc_payload = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "getTransaction",
                    "params": [
                        query,
                        {
                            "encoding": "jsonParsed",
                            "maxSupportedTransactionVersion": 0,
                        },
                    ],
                }
                res = requests.post(
                    "https://api.mainnet-beta.solana.com",
                    json=rpc_payload,
                    timeout=8,
                )
                tx_data = res.json().get("result")
                if tx_data:
                    err = tx_data.get("meta", {}).get("err")
                    status_text = (
                        "Transacción Fallida / Con Errores en Ejecución"
                        if err
                        else "Transacción 100% Exitosa y Confirmada en Bloque"
                    )
                    fee = tx_data.get("meta", {}).get("fee", 0) / 1e9
                    slot = tx_data.get("slot")
                    block_time = tx_data.get("blockTime")
                    time_str = (
                        datetime.fromtimestamp(block_time).strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                        if block_time
                        else "N/A"
                    )
                    str_lit.markdown(
                        f"""
                        <div class='data-metric-box'>
                            <h3 style='color: #FACC15; margin-top:0;'>🪽 Reporte de Firma / Transacción</h3>
                            <hr style='border-color: rgba(250, 204, 21, 0.4);'>
                            • <b>Estado en Red:</b> <span class='status-safe'>{status_text}</span><br>
                            <div class='info-tooltip'><b>¿Qué significa?:</b> Indica si la transferencia o ejecución de contrato inteligente concluyó correctamente o si falló en la red.</div>
                            • <b>Número de Bloque (Slot):</b> {slot}<br>
                            <div class='info-tooltip'><b>¿Qué significa?:</b> El identificador exacto del bloque secuencial de la red donde se procesó la transacción.</div>
                            • <b>Fecha y Hora UTC:</b> {time_str}<br>
                            <div class='info-tooltip'><b>¿Qué significa?:</b> Marca temporal exacta en la que el validador firmó e incluyó la operación.</div>
                            • <b>Comisión Pagada (Fee):</b> {fee} SOL<br>
                            <div class='info-tooltip'><b>¿Qué significa?:</b> Costo en SOL cobrado por la red de Solana para priorizar y procesar la instrucción.</div>
                        </div>
                    """,
                    unsafe_allow_html=True,
                )
                else:
                    str_lit.error(
                        "La firma ingresada no se encuentra registrada o no ha sido propagada en la red principal."
                    )
            except Exception as e:
                str_lit.error(f"Error de conexión RPC: {e}")

        else:
            str_lit.markdown("### 🛡️ Auditoría Informativa y Cartola de Movimientos On-Chain")
            str_lit.code(query, language="text")

            mint_auth_html = ""
            freeze_auth_html = ""
            account_owner = "Desconocido"
            balance_sol = 0.0

            try:
                rpc_payload = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "getAccountInfo",
                    "params": [query, {"encoding": "jsonParsed"}],
                }
                rpc_res = requests.post(
                    "https://api.mainnet-beta.solana.com",
                    json=rpc_payload,
                    timeout=6,
                )
                account_info = rpc_res.json().get("result", {}).get("value")
                if account_info:
                    balance_sol = account_info.get("lamports", 0) / 1e9
                    account_owner = account_info.get("owner", "N/A")
                    data_parsed = account_info.get("data", {}).get("parsed", {})
                    if isinstance(data_parsed, dict) and data_parsed.get("type") == "mint":
                        info = data_parsed.get("info", {})
                        m_auth = info.get("mintAuthority")
                        f_auth = info.get("freezeAuthority")

                        if m_auth is None:
                            mint_auth_html = """
                                • <b>Mint Authority (Autoridad de Emisión):</b> <span class='status-safe'>REVOCADO (Seguro)</span><br>
                                <div class='info-tooltip'><b>¿Qué significa?:</b> La autoridad de emisión ha sido eliminada permanentemente. Nadie puede crear nuevos tokens de la nada, protegiendo a los inversores contra la devaluación masiva o inflación fraudulenta.</div>
                            """
                        else:
                            mint_auth_html = f"""
                                • <b>Mint Authority (Autoridad de Emisión):</b> <span class='status-active'>ACTIVO ({m_auth})</span><br>
                                <div class='info-tooltip'><b>¿Qué significa?:</b> La billetera creadora conserva permisos activos para acuñar nuevos tokens. El emisor tiene la capacidad técnica de generar suministro adicional en cualquier momento.</div>
                            """

                        if f_auth is None:
                            freeze_auth_html = """
                                • <b>Freeze Authority (Autoridad de Congelamiento):</b> <span class='status-safe'>REVOCADO (Seguro)</span><br>
                                <div class='info-tooltip'><b>¿Qué significa?:</b> Se ha renunciado a la capacidad de congelar fondos. El creador no puede bloquear ni confiscar tokens en las billeteras particulares de los usuarios.</div>
                            """
                        else:
                            freeze_auth_html = f"""
                                • <b>Freeze Authority (Autoridad de Congelamiento):</b> <span class='status-active'>ACTIVO ({f_auth})</span><br>
                                <div class='info-tooltip'><b>¿Qué significa?:</b> El contrato permite bloquear las cuentas que posean el token. Los inversores podrían quedar incapacitados para transferir o vender sus activos si el emisor decide congelar cuentas.</div>
                            """
                    else:
                        mint_auth_html = "• <b>Mint Authority:</b> No aplicable (Cuenta de Usuario / Sistema)<br>"
                        freeze_auth_html = "• <b>Freeze Authority:</b> No aplicable (Cuenta de Usuario / Sistema)<br>"
            except Exception:
                mint_auth_html = "• <b>Mint Authority:</b> No disponible temporalmente<br>"
                freeze_auth_html = "• <b>Freeze Authority:</b> No disponible temporalmente<br>"

            pair_data = None
            try:
                res = requests.get(
                    f"https://api.dexscreener.com/latest/dex/tokens/{query}",
                    timeout=5,
                )
                pairs = res.json().get("pairs", [])
                if pairs:
                    pair_data = pairs[0]
                else:
                    res_search = requests.get(
                        f"https://api.dexscreener.com/latest/dex/search?q={query}",
                        timeout=5,
                    )
                    solana_pairs = [
                        p
                        for p in res_search.json().get("pairs", [])
                        if p.get("chainId") == "solana"
                    ]
                    if solana_pairs:
                        pair_data = solana_pairs[0]
            except Exception:
                pass

            if pair_data:
                token_name = pair_data.get("baseToken", {}).get("name", "Desconocido")
                token_symbol = pair_data.get("baseToken", {}).get("symbol", "TOKEN")
                mint_address = pair_data.get("baseToken", {}).get("address", query)
                price_usd = pair_data.get("priceUsd", "0.00")
                liquidity = pair_data.get("liquidity", {}).get("usd", 0)
                volume_h24 = pair_data.get("volume", {}).get("h24", 0)
                fdv = pair_data.get("fdv", 0)
                dex_name = pair_data.get("dexId", "DEX").upper()

                # Emblema exclusivo de Alitas de Ángel (🪽)
                logo_html = "<span style='font-size:1.5rem; margin-right:8px;'>🪽</span>"

                str_lit.markdown(
                    f"""
                    <div class='data-metric-box'>
                        <h3 style='color: #FACC15; margin-top:0;'>{logo_html}Radiografía de Mercado y Contrato del Token</h3>
                        <hr style='border-color: rgba(250, 204, 21, 0.4);'>
                        • <b>Nombre del Token:</b> {token_name} ({token_symbol})<br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Nombre oficial y símbolo registrado en el contrato de la blockchain.</div>
                        • <b>Mint Address (Dirección del Contrato):</b> <code style='color:#FDE047;'>{mint_address}</code><br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Identificador único del token en la red de Solana. Copie esta dirección para operar o verificar.</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                str_lit.code(mint_address, language="text")

                str_lit.markdown(
                    f"""
                    <div class='data-metric-box'>
                        • <b>Exchange Descentralizado (DEX):</b> {dex_name}<br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Plataforma principal de intercambio donde cotiza activamente el par de liquidez.</div>
                        • <b>Precio Actual en Vivo:</b> ${price_usd} USD<br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Cotización actual en tiempo real obtenida directamente de los pools de liquidez.</div>
                        • <b>Liquidez Total (Pool):</b> ${liquidity:,.2f} USD<br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Capital total bloqueado en los pools de intercambio para respaldar compras y ventas sin deslizamiento excesivo.</div>
                        • <b>Volumen de Operación (24h):</b> ${volume_h24:,.2f} USD<br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Monto total transaccionado por los usuarios en el último día completo.</div>
                        • <b>Valor Total Diluido (FDV):</b> ${fdv:,.2f} USD<br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Valor teórico de mercado si el suministro total de tokens estuviera en circulación.</div>
                        <br>
                        <h3 style='color: #38BDF8; margin-top:0;'>🔒 Control de Autoridades y Seguridad del Contrato</h3>
                        <hr style='border-color: rgba(56, 189, 248, 0.4);'>
                        {mint_auth_html}
                        {freeze_auth_html}
                    </div>
                """,
                    unsafe_allow_html=True,
                )
            else:
                str_lit.markdown(
                    f"""
                    <div class='data-metric-box'>
                        <h3 style='color: #38BDF8; margin-top:0;'>🪽 Información de Cuenta / Wallet Analizada</h3>
                        <hr style='border-color: rgba(56, 189, 248, 0.4);'>
                        • <b>Dirección de Billetera:</b> <code style='color:#FDE047;'>{query}</code><br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Clave pública única de la cuenta en la red de Solana.</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                str_lit.code(query, language="text")

                str_lit.markdown(
                    f"""
                    <div class='data-metric-box'>
                        • <b>Programa Propietario (Owner):</b> {account_owner}<br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Contrato o sistema que administra lógicamente esta cuenta (ej. Sistema nativo o Token Program).</div>
                        • <b>Balance Disponible:</b> {balance_sol:,.4f} SOL<br>
                        <div class='info-tooltip'><b>¿Qué significa?:</b> Cantidad de Solana nativo disponible en la cuenta para pagar comisiones o transferencias.</div>
                        {mint_auth_html}
                        {freeze_auth_html}
                    </div>
                """,
                    unsafe_allow_html=True,
                )

            # --- CARTOLA DE MOVIMIENTOS RECIENTES ---
            str_lit.markdown("#### 📜 Cartola Interactiva de Movimientos Recientes (Historial On-Chain en Vivo)")
            str_lit.markdown(
                "<p class='info-tooltip'>Registro cronológico directo de los últimos bloques validados para esta dirección en la red de Solana.</p>",
                unsafe_allow_html=True,
            )
            try:
                sig_payload = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "getSignaturesForAddress",
                    "params": [query, {"limit": 5}],
                }
                sig_res = requests.post(
                    "https://api.mainnet-beta.solana.com",
                    json=sig_payload,
                    timeout=6,
                )
                signatures_list = sig_res.json().get("result", [])
                if signatures_list:
                    for idx, tx_item in enumerate(signatures_list, 1):
                        sig = tx_item.get("signature", "N/A")
                        slot = tx_item.get("slot", "N/A")
                        err = tx_item.get("err")
                        status_str = "Con Error en Red" if err else "Exitosa y Confirmada"
                        block_time = tx_item.get("blockTime")
                        time_str = (
                            datetime.fromtimestamp(block_time).strftime("%Y-%m-%d %H:%M:%S")
                            if block_time
                            else "Registrada"
                        )
                        str_lit.markdown(
                            f"""
                            <div style='background: rgba(12, 35, 64, 0.95); border-left: 4px solid #FACC15; border-right: 1px solid #38BDF8; padding: 12px; margin-bottom: 10px; border-radius: 6px; font-size: 0.85rem;'>
                                <b style='color: #FACC15;'>🪽 Movimiento #{idx}</b> | Estado: <span class='status-safe'>{status_str}</span><br>
                                • <b>Fecha y Hora UTC:</b> {time_str} (Bloque Slot: {slot})<br>
                                <div class='info-tooltip' style='margin-top: 5px; margin-bottom: 5px;'><b>¿Qué significa?:</b> Momento exacto y bloque secuencial en que se procesó esta transferencia o interacción.</div>
                                • <b>Firma de Transacción (TXID):</b> <code style='color:#FDE047;'>{sig}</code>
                            </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    str_lit.info("No se registran transacciones recientes públicas para este objetivo en este momento.")
            except Exception as e:
                str_lit.warning(f"No se pudo cargar la cartola en vivo: {e}")
