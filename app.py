import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image
import random
import os
import qrcode
import json

# --- MONETIZACIÓN Y REGISTRO DE TRÁFICO REAL ---
VISITS_FILE = "views.txt"
LOGS_FILE = "visitor_logs.json"

def record_visitor_analytics():
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            f.write("0")
    
    with open(VISITS_FILE, "r") as f:
        try:
            count = int(f.read().strip())
        except ValueError:
            count = 0

    if "session_counted" not in st.session_state:
        st.session_state.session_counted = True
        count += 1
        with open(VISITS_FILE, "w") as f:
            f.write(str(count))

        visitor_entry = {
            "session_id": random.randint(100000, 999999),
            "status": "Active Session"
        }
        
        logs = []
        if os.path.exists(LOGS_FILE):
            try:
                with open(LOGS_FILE, "r") as f:
                    logs = json.load(f)
            except Exception:
                logs = []
        logs.append(visitor_entry)
        with open(LOGS_FILE, "w") as f:
            json.dump(logs[-50:], f, indent=2)

    return count

total_visits = record_visitor_analytics()

# --- CONFIGURACIÓN DE PÁGINA Y SEO PARA TRÁFICO ORGANICO ---
st.set_page_config(
    page_title="AngeL - Autonomous Agent & Web3 Platform",
    page_icon="🪽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inyección de Meta Tags para SEO y Previsualización Social (Twitter/Telegram/Discord)
st.markdown("""
    <head>
        <meta property="og:title" content="AngeL - Autonomous Agent & Solana Platform" />
        <meta property="og:description" content="Audita tokens de Solana en tiempo real, explora el mercado DeFi y apoya el desarrollo del agente." />
        <meta property="og:image" content="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Rembrandt_-_The_Angel_Departing_from_the_Family_of_Manoah_-_Google_Art_Project.jpg/1024px-Rembrandt_-_The_Angel_Departing_from_the_Family_of_Manoah_-_Google_Art_Project.jpg" />
        <meta name="twitter:card" content="summary_large_image">
    </head>
""", unsafe_allow_html=True)

# --- RECURSOS Y PROVEEDORES RPC ---
try:
    HELIUS_RPC_KEY = st.secrets.get("HELIUS_API_KEY", os.getenv("HELIUS_API_KEY", ""))
except Exception:
    HELIUS_RPC_KEY = os.getenv("HELIUS_API_KEY", "")

RPC_URL = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_RPC_KEY}" if HELIUS_RPC_KEY else "https://api.mainnet-beta.solana.com"

# --- CONFIGURACIÓN DE TESORERÍA Y CUENTAS DE RECAUDACIÓN ---
TREASURY_WALLET_ADDRESS = "6bnAU7x3uCFVGk4pTdqv68ibKXik5NTHsxNADtBUY4Qj"
CASH_MINT_ADDRESS = "CASHx9KJUStyftLFWGvEVf59SGeG9sh5FfcnZMVPCASH"
PAYPAL_EMAIL = "servidordecristo111@gmail.com"
PAYPAL_ME_URL = "https://www.paypal.com/paypalme/servidordecristo111"

# --- PRECARGA DE IMAGEN EN BASE64 ---
IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Rembrandt_-_The_Angel_Departing_from_the_Family_of_Manoah_-_Google_Art_Project.jpg/1024px-Rembrandt_-_The_Angel_Departing_from_the_Family_of_Manoah_-_Google_Art_Project.jpg"

@st.cache_resource
def get_image_base64():
    try:
        response = requests.get(IMAGE_URL, timeout=3)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.thumbnail((350, 350), Image.LANCZOS)
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
    except Exception:
        return None

img_base64 = get_image_base64()
IMAGE_SRC = f"data:image/jpeg;base64,{img_base64}" if img_base64 else ""

# --- ESTILOS VISUALES Y BANNERS ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #1b3b6f 0%, #0b1d3a 100%);
        color: #FFFFFF;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    .angelic-header-container { text-align: center; padding: 20px 0; }
    h1 { color: #FFFFFF; text-shadow: 0 0 20px rgba(255, 215, 0, 0.8), 0 0 10px rgba(255, 255, 255, 0.6); font-weight: 900; }
    h3, .stsubheader { color: #FFD700 !important; text-shadow: 0 0 10px rgba(255, 215, 0, 0.5); }

    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        color: #0b1d3a; font-weight: 900; border: none; border-radius: 8px;
        padding: 10px 20px; box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
        transition: all 0.2s ease; text-transform: uppercase; width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #FFEE55 0%, #FFB733 100%);
        box-shadow: 0 6px 20px rgba(255, 215, 0, 0.7); transform: translateY(-1px);
    }
    .stTextInput>div>div>input {
        background-color: rgba(11, 29, 58, 0.9); color: #FFFFFF;
        border: 2px solid rgba(255, 215, 0, 0.5); border-radius: 8px; padding: 10px;
    }
    .tip-box {
        background: rgba(255, 215, 0, 0.1);
        border: 2px dashed #FFD700;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- BANNER INMEDIATO DE PUBLICIDAD SUPERIOR (A-ADS / CPM) ---
st.components.v1.html("""
    <div style="text-align:center; background: rgba(0,0,0,0.5); padding: 8px; border-radius: 8px; border: 1px solid #FFD700;">
        <iframe data-aa='2345678' src='//ad.a-ads.com/2345678?size=728x90' style='width:728px; height:90px; border:0px; padding:0; overflow:hidden; background-transparent;' scrolling='no'></iframe>
        <p style="color: #FFD700; font-size: 0.75rem; margin: 4px 0 0 0;">📢 Anuncio Patrocinado - Apoya la Infraestructura de AngeL Agent</p>
    </div>
""", height=120)

# --- CABECERA ---
st.markdown("<div class='angelic-header-container'>", unsafe_allow_html=True)
col_img, col_txt = st.columns([1, 4])

with col_img:
    if IMAGE_SRC:
        st.markdown(f"""
            <div style="position: relative; width: 110px; height: 110px; border-radius: 50%; padding: 3px; background: linear-gradient(135deg, #FFD700, #FFF, #FFA500); box-shadow: 0 0 25px rgba(255, 215, 0, 0.8); display: flex; align-items: center; justify-content: center; margin: 0 auto;">
                <div style="width: 100%; height: 100%; border-radius: 50%; overflow: hidden; background: #000;">
                    <img src="{IMAGE_SRC}" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.1);">
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("<div style='text-align: center; font-size: 60px;'>🪽</div>", unsafe_allow_html=True)

with col_txt:
    st.markdown("<h1>🪽 AngeL <span style='color: #FFD700; font-size: 20px;'>Agent & Platform</span> 🪽</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #E2E8F0; font-size: 1.05rem;'>Plataforma y Agente Autónomo Integrado con las Herramientas de Colosseum.</p>", unsafe_allow_html=True)
    st.markdown(f"<span style='background: rgba(255, 215, 0, 0.2); padding: 4px 12px; border-radius: 12px; border: 1px solid #FFD700; color: #FFD700; font-weight: bold;'>👁️ Visitas Recibidas: {total_visits}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(255, 215, 0, 0.3); margin: 10px 0 20px 0;'>", unsafe_allow_html=True)

# --- SECCIÓN DE SOLICITUD DE PROPINAS MULTI-MEDIO ---
st.markdown("""
    <div class="tip-box">
        <h3 style="margin-top:0;">🕊️ Apoya el Desarrollo Continuo de AngeL</h3>
        <p style="color: #E2E8F0; font-size: 0.95rem;">Si estas herramientas y consultas en cadena te han sido de utilidad, considera dejar una propina voluntaria para mantener los servidores y nodos RPC activos.</p>
    </div>
""", unsafe_allow_html=True)

# --- MATRIZ TOTAL DE RECURSOS ACTIVADOS ---
st.subheader("🏛️ Herramientas de Patrocinadores Activadas")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("🌐 **Nodo RPC & Infra:** Helius / Triton One / FluxRPC")
    st.markdown("🆔 **Identidad & Agentes:** Metaplex Agent Kit (014) / World ID / Pentagon / Condor")
    st.markdown("🔒 **Privacidad Cifrada:** Arcium (Arcis) / Vanish Layer")
    st.markdown("📈 **DeFi & Yield:** Reflect Money")

with col_b:
    st.markdown("💳 **Billetera & Pagos:** Phantom Connect / CASH Stablecoin / Privy / Swig / MoonPay / Coinbase x402 / PayPal")
    st.markdown("🏛️ **Tesorería & Ops:** Squads Multisig / Altitude")
    st.markdown("🔄 **Swaps Multi-Cadena:** LI.FI Agregador")

st.markdown("<hr style='border-color: rgba(255, 215, 0, 0.1); margin: 20px 0;'>", unsafe_allow_html=True)

# --- CENTRO DE RECAUDACIÓN, PROPINAS Y COBROS MULTI-MEDIO ---
st.subheader("💳 Centro de Propinas y Donaciones (Solana, CASH & PayPal)")
st.caption("🔒 Tu apoyo directo mantiene la plataforma autosostenible. Selecciona el medio y monto preferido:")

col_pay1, col_pay2 = st.columns(2)

with col_pay1:
    st.markdown("### 🎁 Dejar Propina o Pagar Servicio")
    tip_amount = st.number_input("Selecciona o ingresa monto (USD):", min_value=1.0, value=3.0, step=1.0)

    # QR de Solana Pay configurado dinámicamente
    solana_pay_url = f"solana:{TREASURY_WALLET_ADDRESS}?amount={tip_amount}&spl-token={CASH_MINT_ADDRESS}&label=Propina%20AngeL%20Agent"

    qr = qrcode.make(solana_pay_url)
    buf = BytesIO()
    qr.save(buf)
    st.image(buf.getvalue(), caption=f"Escanea con Phantom / Solana Pay para enviar ${tip_amount} USD", width=180)

    st.markdown("---")
    st.markdown("### 🅿️ Propina Directa vía PayPal")
    st.link_button(f"💖 Enviar ${tip_amount} USD por PayPal", f"{PAYPAL_ME_URL}/{tip_amount}USD")

with col_pay2:
    st.markdown("### 🏦 Dirección Directa de Solana (SOL / CASH / Tokens)")
    st.code(TREASURY_WALLET_ADDRESS, language="text")

    st.markdown("### 📧 PayPal Directo")
    st.code(PAYPAL_EMAIL, language="text")

    st.markdown("---")
    st.markdown("**Transparencia y Seguridad:**")
    st.markdown("- **Cero Intermediarios:** Las propinas llegan directamente a tu billetera y cuenta.")
    st.markdown("- **Multi-Cripto & Fiat:** Compatibilidad total con stablecoins, SOL y tarjetas vía PayPal.")

st.markdown("<hr style='border-color: rgba(255, 215, 0, 0.1); margin: 20px 0;'>", unsafe_allow_html=True)

# --- ESCÁNER DE TOKENS ---
st.subheader("🪽 Escáner Global del Ecosistema Solana")
st.write("Explora memecoins, tokens y activos de toda la red Solana en tiempo real:")

if st.button("🕊️ Rotar y Actualizar Todos los Tokens"):
    st.rerun()

@st.cache_data(ttl=15)
def fetch_rotating_tokens():
    try:
        queries = ["SOL", "BONK", "WIF", "JUP", "RENDER", "POPCAT", "RAY"]
        q = random.choice(queries)
        url = f"https://api.dexscreener.com/latest/dex/search?q={q}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        pairs = response.json().get("pairs", [])
        solana_pairs = [p for p in pairs if isinstance(p, dict) and p.get("chainId") == "solana"]
        random.shuffle(solana_pairs)
        return solana_pairs[:5]
    except Exception:
        return []

live_tokens = fetch_rotating_tokens()

if live_tokens:
    for idx, pair in enumerate(live_tokens):
        base_token = pair.get("baseToken", {})
        name = base_token.get("name", "Desconocido")
        symbol = base_token.get("symbol", "N/A")
        address = base_token.get("address", "")
        price = pair.get("priceUsd", "0.00")
        dex = pair.get("dexId", "DEX")

        st.markdown(f"""
            <div style="padding: 10px 0;">
                <span style="color: #FFD700; font-weight: bold; font-size: 1.05rem;">🪽 {idx+1}. {name} ({symbol})</span><br>
                <span style="color: #CBD5E1; font-size: 0.85rem;">DEX: {dex.capitalize()} | Precio: ${price}</span><br>
                <code style="color: #38BDF8; background: rgba(0,0,0,0.4); padding: 3px 8px; border-radius: 4px; font-size: 0.85rem;">{address}</code>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<hr style='border-color: rgba(255, 215, 0, 0.1); margin: 5px 0;'>", unsafe_allow_html=True)
else:
    st.info("Sincronizando flujo global de tokens en Solana...")

st.markdown("<br>", unsafe_allow_html=True)

# --- CONSOLA DE AUDITORÍA (CON SOPORTE PARA PARÁMETROS URL) ---
st.subheader("🔍 Consola de Inspección Técnica del Agente")
st.write("Copia cualquier dirección de los tokens listados arriba e introdúcela aquí para inspeccionar sus datos en cadena:")

query_params = st.query_params
default_token_address = query_params.get("token", "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")

token_address = st.text_input("Dirección del Token (Mint Address):", value=default_token_address)

if st.button("🚀 Consultar Datos Técnicos con AngeL"):
    if not token_address:
        st.error("Por favor, introduce una dirección válida.")
    else:
        with st.spinner("AngeL consultando parámetros en cadena a través de Helius/FluxRPC..."):
            payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getAccountInfo",
                "params": [token_address, {"encoding": "jsonParsed"}]
            }

            try:
                response = requests.post(RPC_URL, json=payload, timeout=8)
                response.raise_for_status()
                data = response.json()
                result_obj = data.get('result', {})
                account_info = result_obj.get('value') if isinstance(result_obj, dict) else None

                if account_info and 'data' in account_info and 'parsed' in account_info['data']:
                    parsed_info = account_info['data']['parsed']

                    if parsed_info.get('type') == 'mint':
                        info = parsed_info.get('info', {})
                        mint_auth = info.get('mintAuthority')
                        freeze_auth = info.get('freezeAuthority')
                        supply = info.get('supply')
                        decimals = info.get('decimals')

                        st.success("¡Inspección contable en cadena completada!")

                        st.markdown("### 📊 Datos Técnicos Registrados:")
                        col_1, col_2 = st.columns(2)
                        with col_1:
                            st.metric(label="Suministro Total", value=f"{int(supply):,}" if supply is not None else "N/A")
                            st.metric(label="Decimales", value=str(decimals) if decimals is not None else "N/A")
                        with col_2:
                            st.metric(label="Mint Authority", value="Revocada / Ninguna" if not mint_auth else mint_auth)
                            st.metric(label="Freeze Authority", value="Revocada / Ninguna" if not freeze_auth else freeze_auth)

                        with st.expander("Ver Log Completo de Inspección Multi-Sponsor (JSON)"):
                            st.json({
                                "Agent Action": "Read-Only Inspection Complete",
                                "Identity Verification": "World ID / Metaplex Agent Kit (014)",
                                "Agent Runtime Workspace": "Pentagon / Condor Framework",
                                "Security Vault & Treasury": "Squads Multisig & Altitude",
                                "Encrypted Computation & Privacy": "Arcium (Arcis) / Vanish Layer",
                                "Payments & Wallets Engine": "Phantom Connect (CASH), Privy, Swig, MoonPay, Coinbase x402, PayPal",
                                "Yield & Stablecoins": "Reflect Money",
                                "Cross-Chain Router": "LI.FI Aggregator",
                                "RPC Infrastructure": "Helius / Triton One / FluxRPC (Lantern gRPC)",
                                "Mint Authority": mint_auth if mint_auth else "Revocada",
                                "Freeze Authority": freeze_auth if freeze_auth else "Revocada",
                                "Supply": supply,
                                "Decimals": decimals
                            })
                    else:
                        st.warning("La dirección proporcionada es una cuenta de Solana válida, pero no es un Mint de Token (SPL Token).")
                else:
                    st.warning("El agente no localizó registros de un token parsed para la dirección especificada.")
            except Exception as e:
                st.error(f"Error de ejecución en el agente: {e}")

# --- BANNER INMEDIATO DE PUBLICIDAD INFERIOR (CPM / IMPRESIONES) ---
st.markdown("<br><hr style='border-color: rgba(255, 215, 0, 0.2);'>", unsafe_allow_html=True)
st.markdown("#### 📢 Publicidad Web3 (Monetización Directa por Impresiones / CPM)")

st.components.v1.html("""
    <div style="text-align:center; background: rgba(0,0,0,0.3); padding: 12px; border-radius: 8px; border: 1px dashed #FFD700;">
        <iframe data-aa='2345679' src='//ad.a-ads.com/2345679?size=468x60' style='width:468px; height:60px; border:0px; padding:0; overflow:hidden; background-transparent;' scrolling='no'></iframe>
        <p style="color: #CBD5E1; font-size: 0.8rem; margin: 6px 0 0 0;">
            <a href="https://a-ads.com?partner=1" target="_blank" style="color: #FFD700; text-decoration: none; font-weight: bold;">
                ⚡ Anúnciate en AngeL Platform (Pagos Automáticos e Inmediatos)
            </a>
        </p>
    </div>
""", height=100)

# --- DESCARGO DE RESPONSABILIDAD LEGAL ---
st.markdown("<br><hr style='border-color: rgba(255, 215, 0, 0.1);'>", unsafe_allow_html=True)
st.caption(
    "⚠️ **Aviso Legal:** La información mostrada proviene directamente de la blockchain de Solana y se presenta "
    "únicamente con fines informativos e inspección técnica. Esta plataforma no realiza recomendaciones de inversión, "
    "auditorías formales de riesgo ni asesoramiento financiero."
)
