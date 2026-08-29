import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image
import random

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="AngeL - Solana Intelligence",
    page_icon="🪽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- PRECARGA DE IMAGEN DE REMBRANDT EN BASE64 ---
IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Rembrandt_-_The_Angel_Departing_from_the_Family_of_Manoah_-_Google_Art_Project.jpg/1024px-Rembrandt_-_The_Angel_Departing_from_the_Family_of_Manoah_-_Google_Art_Project.jpg"

@st.cache_resource
def get_image_base64():
    try:
        response = requests.get(IMAGE_URL, timeout=5)
        img = Image.open(BytesIO(response.content))
        img.thumbnail((350, 350), Image.LANCZOS)
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
    except Exception:
        return None

img_base64 = get_image_base64()
IMAGE_SRC = f"data:image/jpeg;base64,{img_base64}" if img_base64 else ""

# --- ESTILOS: FONDO CELESTE/AZUL CLARO Y ALAS DE ÁNGEL ---
st.markdown(f"""
    <style>
    .stApp {{
        background: radial-gradient(circle at center, #1b3b6f 0%, #0b1d3a 100%);
        color: #FFFFFF;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }}

    .angelic-header-container {{
        text-align: center;
        padding: 20px 0;
    }}

    h1 {{
        color: #FFFFFF;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.8), 0 0 10px rgba(255, 255, 255, 0.6);
        font-weight: 900;
    }}
    
    h3, .stsubheader {{
        color: #FFD700 !important;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }}

    /* Botones de Oro Brillante */
    .stButton>button {{
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        color: #0b1d3a;
        font-weight: 900;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
        transition: all 0.2s ease;
        text-transform: uppercase;
        width: 100%;
    }}
    .stButton>button:hover {{
        background: linear-gradient(135deg, #FFEE55 0%, #FFB733 100%);
        box-shadow: 0 6px 20px rgba(255, 215, 0, 0.7);
        transform: translateY(-1px);
    }}

    .stTextInput>div>div>input {{
        background-color: rgba(11, 29, 58, 0.9);
        color: #FFFFFF;
        border: 2px solid rgba(255, 215, 0, 0.5);
        border-radius: 8px;
        padding: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- CABECERA CON ARTE Y ALAS (SIN RECTÁNGULOS) ---
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
    st.markdown("<h1>🪽 AngeL <span style='color: #FFD700; font-size: 20px;'>Solana Intelligence</span> 🪽</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #E2E8F0; font-size: 1.05rem;'>Agente autónomo de auditoría técnica y análisis global de tokens en tiempo real.</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(255, 215, 0, 0.3); margin: 10px 0 30px 0;'>", unsafe_allow_html=True)

# --- ESCÁNER DE TOKENS ROTATIVOS CON UN SOLO BOTÓN MAESTRO ---
st.subheader("🪽 Escáner Global del Ecosistema Solana")
st.write("Explora memecoins, tokens y activos de toda la red Solana en tiempo real:")

# Único botón maestro para rotar todo el flujo de tokens globales
if st.button("🕊️ Rotar y Actualizar Todos los Tokens"):
    st.rerun()

def fetch_rotating_tokens():
    try:
        # Ampliamos las categorías para barrer todo tipo de memecoins, tokens y activos en Solana
        queries = ["SOL", "BONK", "AI", "CAT", "DOG", "MEME", "WIF", "POPCAT", "BOME", "USDC", "JUP", "RAY", "RENDER", "CLOUD"]
        q = random.choice(queries)
        url = f"https://api.dexscreener.com/latest/dex/search?q={q}"
        response = requests.get(url, timeout=5)
        data = response.json()
        pairs = data.get("pairs", [])
        
        solana_pairs = [
            p for p in pairs 
            if p.get("chainId") == "solana" and p.get("baseToken", {}).get("address") != "So11111111111111111111111111111111111111112"
        ]
        random.shuffle(solana_pairs)
        return solana_pairs[:5] # Muestra 5 tokens dinámicos y variados
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
st.subheader("🔍 Consola de Auditoría de Tokens")
st.write("Copia cualquier dirección de los tokens listados arriba e introdúcela aquí para auditar sus autoridades de seguridad:")

token_address = st.text_input("Dirección del Token (Mint Address):", value="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")

if st.button("🚀 Ejecutar Análisis con AngeL"):
    if not token_address:
        st.error("Por favor, introduce una dirección válida.")
    else:
        with st.spinner("Consultando la red RPC de Solana..."):
            url = "https://api.mainnet-beta.solana.com"
            payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getAccountInfo",
                "params": [
                    token_address,
                    {"encoding": "jsonParsed"}
                ]
            }

            try:
                response = requests.post(url, json=payload)
                data = response.json()
                
                result_obj = data.get('result', {})
                account_info = result_obj.get('value') if isinstance(result_obj, dict) else None

                if account_info:
                    parsed_data = account_info['data']['parsed']['info']
                    mint_auth = parsed_data.get('mintAuthority')
                    freeze_auth = parsed_data.get('freezeAuthority')
                    supply = parsed_data.get('supply')
                    decimals = parsed_data.get('decimals')

                    st.success("¡Datos extraídos con éxito!")

                    st.markdown("### 📊 Métricas Técnicas Obtenidas:")
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.metric(label="Suministro Total", value=supply if supply else "N/A")
                        st.metric(label="Decimales", value=decimals if decimals is not None else "N/A")
                    with col_b:
                        st.metric(label="Autoridad de Acuñación", value="Revocada" if not mint_auth else "Activa")
                        st.metric(label="Autoridad de Congelamiento", value="Ninguna" if not freeze_auth else "Activa")

                    with st.expander("Ver JSON Técnico Completo"):
                        st.json({
                            "Mint Authority": mint_auth if mint_auth else "Revocada / Ninguna",
                            "Freeze Authority": freeze_auth if freeze_auth else "Revocada / Ninguna",
                            "Supply": supply,
                            "Decimals": decimals
                        })
                else:
                    st.warning("No se encontró información para la dirección proporcionada (es posible que el mint sea antiguo o inválido).")
            except Exception as e:
                st.error(f"Error al conectar con la red: {e}")
