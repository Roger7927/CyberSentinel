# (c) 2026 Guillermo Roger Hernandez Chandia - ADS
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time
from datetime import datetime

# 1. Setup de Cockpit: Identidade Independente
st.set_page_config(page_title="ROGER SENTINEL v190", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    .main { background: radial-gradient(circle, #001a00 0%, #000000 100%); }
    header {visibility: hidden;}
    .block-container {padding-top: 0.5rem;}
    [data-testid="stMetricValue"] { color: #00ff00; font-family: 'Courier New'; text-shadow: 0 0 10px #00ff00aa; }
    h4 { color: #00ff00; font-family: 'Courier New'; border-bottom: 1px solid #00ff0033; padding-bottom: 5px; }
    .stCodeBlock { border: 1px solid #00ff0044 !important; background: rgba(0,0,0,0.8) !important; }
    .auth-box { border: 2px solid #00ff00; padding: 15px; border-radius: 10px; background: rgba(0, 255, 0, 0.05); box-shadow: 0 0 15px #00ff0033; }
</style>
""", unsafe_allow_html=True)

# 2. Estrutura HUD (Full Professional)
st.markdown("<h3 style='text-align: center; color: #00ff00; letter-spacing: 5px;'>🛰️ ROGER_TACTICAL_SYSTEMS // CORE_OS_v1.9</h3>", unsafe_allow_html=True)

col_auth, col_radar, col_data = st.columns([0.8, 2, 0.8])

with col_auth:
    st.markdown("#### 👤 OPERATOR_ID")
    st.markdown("""
    <div class='auth-box'>
        <b style='color:#00ff00; font-family: Courier;'>DEVELOPER:</b> <span style='color:white; font-family: Courier;'>GUILLERMO ROGER</span><br>
        <b style='color:#00ff00; font-family: Courier;'>PROJECT:</b> <span style='color:white; font-family: Courier;'>CYBER_SENTINEL</span><br>
        <b style='color:#00ff00; font-family: Courier;'>CLEARANCE:</b> <span style='color:#00ff00; text-shadow: 0 0 5px;'>GOD_MODE</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 🛡️ THREAT_MONITOR")
    m_risk = st.empty()
    chart_risk = st.empty()

with col_radar:
    radar_placeholder = st.empty()

with col_data:
    st.markdown("#### 📡 NETWORK_PULSE")
    chart_net = st.empty()
    m_net = st.empty()
    st.markdown("---")
    st.markdown("#### 📜 KERNEL_LOGS")
    log_placeholder = st.empty()

# 3. Lógica de Varredura Estável
angle = 0
risk_history = np.random.randint(20, 40, 20)
net_history = np.random.randint(50, 100, 20)

while True:
    # A) O RADAR (Bolinhas e Caixas)
    fig_rd = go.Figure()
    
    fig_rd.update_layout(
        template="plotly_dark",
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, range=[0, 1], gridcolor="rgba(0,255,0,0.1)", showticklabels=False),
            angularaxis=dict(gridcolor="rgba(0,255,0,0.2)", rotation=90, direction="clockwise",
                             tickvals=[0, 90, 180, 270], ticktext=["N", "E", "S", "W"])
        ),
        showlegend=False, height=700, margin=dict(t=20, b=20, l=20, r=20)
    )

    # Rastro de Persistência
    for i in range(12):
        op = max(0.0, 0.4 - (i * 0.03))
        trail_ang = (angle - (i * 4)) % 360
        fig_rd.add_trace(go.Scatterpolar(r=[0, 1], theta=[trail_ang, trail_ang], mode='lines', 
                                       line=dict(color=f'rgba(0, 255, 0, {op})', width=max(1, 10-i))))

    # Varredura Principal
    fig_rd.add_trace(go.Scatterpolar(r=[0, 1], theta=[angle, angle], mode='lines', line=dict(color='#00ff00', width=5)))
    fig_rd.add_trace(go.Scatterpolar(r=[0.7, 0.45], theta=[60, 230], mode='markers', 
                                   marker=dict(color='#ff2d55', size=18, symbol='circle-open', line=dict(width=3))))

    with radar_placeholder.container():
        st.plotly_chart(fig_rd, use_container_width=True, key=f"final_rd_{time.time()}")

    # B) GRÁFICOS DINÂMICOS
    risk_val = np.random.randint(10, 95 if angle > 300 else 40)
    risk_history = np.append(risk_history[1:], risk_val)
    fig_risk = go.Figure(go.Scatter(y=risk_history, fill='tozeroy', line=dict(color='#00ff00')))
    fig_risk.update_layout(template="plotly_dark", height=130, margin=dict(t=0,b=0,l=0,r=0), xaxis=dict(visible=False), yaxis=dict(visible=False), paper_bgcolor='rgba(0,0,0,0)')
    chart_risk.plotly_chart(fig_risk, use_container_width=True, key=f"risk_{time.time()}")

    net_val = np.random.randint(200, 800)
    net_history = np.append(net_history[1:], net_val)
    fig_net = go.Figure(go.Scatter(y=net_history, line=dict(color='#00ff00', width=2)))
    fig_net.update_layout(template="plotly_dark", height=130, margin=dict(t=0,b=0,l=0,r=0), xaxis=dict(visible=False), yaxis=dict(visible=False), paper_bgcolor='rgba(0,0,0,0)')
    chart_net.plotly_chart(fig_net, use_container_width=True, key=f"net_{time.time()}")

    # C) MÉTRICAS E LOGS
    m_risk.metric("LOCAL_THREAT", f"{risk_val}%")
    m_net.metric("UPLINK_STATUS", f"{net_val} Mbps", "OPTIMAL")
    
    now = datetime.now().strftime("%H:%M:%S")
    log_placeholder.code(f">> SYSTEM_OWNER: ROGER_LABS\n>> VECTOR_{angle:03d}_SECURE\n>> STATUS: NOMINAL\n>> CLOCK: {now}")

    angle = (angle + 12) % 360
    time.sleep(0.04)
