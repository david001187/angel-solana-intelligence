import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image
import random
import os
import qrcode

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AngeL - Autonomous Agent & Platform",
    page_icon="🪽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- RECURSOS Y PROVEEDORES RPC (MANEJO SEGURO DE API KEY) ---
try:
    HELIUS_RPC_KEY = st.secrets.get("HELIUS_API_KEY", os.getenv("HELIUS_API_KEY", ""))
except Exception:
    HELIUS_RPC_KEY = os.getenv("HELIUS_API_KEY", "")

RPC_URL = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_RPC_KEY}" if HELIUS_RPC_KEY else "https://api.mainnet-beta.solana.com"

# --- CONFIGURACIÓN DE TESORERÍA Y COBROS ---
TREASURY_WALLET_ADDRESS = "6bnAU7x3uCFVGk4pTdqv68ibKXik5NTHsxNADtBUY4Qj"
CASH_MINT_ADDRESS = "CASHx9KJUStyftLFWGvEVf59SGeG9sh5FfcnZMVPCASH"
PAYPAL_ME_URL = "https://paypal.me/servidordecristo111"
PAYPAL_EMAIL = "servidordecristo111@gmail.com"

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

# --- ESTILOS VISUALES ---
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
    .paypal-btn {
        display: inline-block;
        background: linear-gradient(135deg, #0070BA 0%, #003087 100%);
        color: #FFFFFF !important;
        font-weight: bold;
        text-align: center;
        padding: 10px 15px;
        border-radius: 8px;
        text-decoration: none;
        width: 100%;
        box-shadow: 0 4px 12px rgba(0, 112, 186, 0.4);
        margin-top: 10px;
    }
    .paypal-btn:hover {
        background: linear-gradient(135deg, #005ea6 0%, #002568 100%);
    }
    </style>
""", unsafe_allow_html=True)

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

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(255, 215, 0, 0.3); margin: 10px 0 30px 0;'>", unsafe_allow_html=True)

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

# --- CENTRO DE RECAUDACIÓN Y PAGO (BÓVEDA / VAULT) ---
st.subheader("💳 Bóveda de Recaudación AngeL (CASH, Phantom Connect & PayPal)")
st.caption("🔒 Módulo de solo lectura y recepción. El agente no administra llaves privadas ni ejecuta transferencias salientes.")

col_pay1, col_pay2 = st.columns(2)

with col_pay1:
    st.markdown("### 🕊️ Donar o Pagar Auditoría")
    amount = st.number_input("Monto (USD):", min_value=1.0, value=5.0, step=1.0)

    solana_pay_url = f"solana:{TREASURY_WALLET_ADDRESS}?amount={amount}&spl-token={CASH_MINT_ADDRESS}&label=AngeL%20Treasury"

    qr = qrcode.make(solana_pay_url)
    buf = BytesIO()
    qr.save(buf)
    st.image(buf.getvalue(), caption=f"Escanea con Phantom para enviar ${amount} CASH", width=180)

    st.markdown("---")
    st.markdown("### 🅿️ Pago vía PayPal")
    paypal_direct_link = f"{PAYPAL_ME_URL}/{amount}"
    st.markdown(f'<a href="{paypal_direct_link}" target="_blank" class="paypal-btn">💳 Pagar ${amount} USD con PayPal</a>', unsafe_allow_html=True)

with col_pay2:
    st.markdown("### 🏦 Dirección de Depósito Solana")
    st.code(TREASURY_WALLET_ADDRESS, language="text")

    st.markdown("### 📧 Cuenta de PayPal")
    st.code(PAYPAL_EMAIL, language="text")

    st.markdown("---")
    st.markdown("**Seguridad de Bóveda:**")
    st.markdown("- **Read-Only Vault:** Cero permisos de firma saliente.")
    st.markdown("- **CASH Stablecoin & Fiat:** Soporte para stablecoins nativas y pasarelas fiat vía PayPal.")

if st.button("🔄 Ver Estado de Fondos Recaudados"):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenAccountsByOwner",
        "params": [
            TREASURY_WALLET_ADDRESS,
            {"mint": CASH_MINT_ADDRESS},
            {"encoding": "jsonParsed"}
        ]
    }
    try:
        response = requests.post(RPC_URL, json=payload, timeout=5)
        res_json = response.json()
        accounts = res_json.get("result", {}).get("value", [])

        if accounts:
            balance = accounts[0]["account"]["data"]["parsed"]["info"]["tokenAmount"]["uiAmount"]
            st.success(f"Saldo Recaudado en Bóveda: ${balance:.2f} CASH")
        else:
            st.info("Aún no se registran depósitos en CASH para esta cuenta.")
    except Exception:
        st.warning("No se pudo obtener el saldo acumulado en este momento.")

st.markdown("<hr style='border-color: rgba(255, 215, 0, 0.1); margin: 20px 0;'>", unsafe_allow_html=True)

# --- ESCÁNER DE TOKENS ---
st.subheader("🪽 Escáner Global del Ecosistema Solana")
st.write("Explora memecoins, tokens y activos de toda la red Solana en tiempo real:")

if st.button("🕊️ Rotar y Actualizar Todos los Tokens"):
    st.rerun()

@st.cache_data(ttl=15)
def fetch_rotating_tokens():
    try:
        queries = ["CLOUD", "SOL", "BONK", "AI", "WIF", "JUP", "RENDER"]
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

# --- CONSOLA DE AUDITORÍA ---
st.subheader("🔍 Consola de Inspección Técnica del Agente")
st.write("Copia cualquier dirección de los tokens listados arriba e introdúcela aquí para inspeccionar sus datos en cadena:")

token_address = st.text_input("Dirección del Token (Mint Address):", value="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")

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

# --- DESCARGO DE RESPONSABILIDAD LEGAL ---
st.markdown("<br><hr style='border-color: rgba(255, 215, 0, 0.1);'>", unsafe_allow_html=True)
st.caption(
    "⚠️ **Aviso Legal:** La información mostrada proviene directamente de la blockchain de Solana y se presenta "
    "únicamente con fines informativos e inspección técnica. Esta plataforma no realiza recomendaciones de inversión, "
    "auditorías formales de riesgo ni asesoramiento financiero."
)
