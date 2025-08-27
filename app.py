import streamlit as st
from game import Move, play_round, move_to_emoji

# Page setup
st.set_page_config(page_title="Stone · Paper · Scissors", page_icon="🎮", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color:#F0FFFF   ;'>🪨 📄 ✂️ Stone · Paper · Scissors</h1>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.subheader("📖 How to play")
    st.info("""
    - Stone beats Scissors  
    - Paper beats Stone  
    - Scissors beat Paper  
    """)
    st.markdown("---")
    st.write("Click a button below to play. Score updates automatically.")
    st.markdown("---")
    if st.button("🔄 Reset Score"):
        st.session_state.update({"wins": 0, "losses": 0, "draws": 0})
        if "last" in st.session_state:
            st.session_state.pop("last")

# Initialize session state
for key in ["wins", "losses", "draws"]:
    if key not in st.session_state:
        st.session_state[key] = 0

# UI buttons
st.subheader("👉 Make your move")
cols = st.columns(3)

if cols[0].button("🪨 Stone", use_container_width=True):
    st.session_state.last = play_round(Move.STONE)
if cols[1].button("📄 Paper", use_container_width=True):
    st.session_state.last = play_round(Move.PAPER)
if cols[2].button("✂️ Scissors", use_container_width=True):
    st.session_state.last = play_round(Move.SCISSORS)

st.markdown("---")

# Show result
if "last" in st.session_state:
    result, player, comp = st.session_state.last
    st.markdown(
        f"<h3 style='text-align: center;'>You {move_to_emoji(player)} vs Computer {move_to_emoji(comp)}</h3>",
        unsafe_allow_html=True
    )

    if result == "draw":
        st.session_state.draws += 1
        st.warning("It's a draw! 😐")
    elif result == "player":
        st.session_state.wins += 1
        st.success("You Win 🎉")
    else:
        st.session_state.losses += 1
        st.error("Computer Wins 😅")

# Scoreboard
st.markdown("---")
st.subheader("📊 Scoreboard")
c1, c2, c3 = st.columns(3)
c1.metric("Wins", st.session_state.wins)
c2.metric("Losses", st.session_state.losses)
c3.metric("Draws", st.session_state.draws)
