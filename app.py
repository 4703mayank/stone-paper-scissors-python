
import streamlit as st
from game import Move, play_round, move_to_emoji

st.set_page_config(page_title="Stone · Paper · Scissors", page_icon="🎮", layout="centered")

st.title("Stone · Paper · Scissors")
st.caption("Python · Streamlit · From scratch")


with st.sidebar:
    st.subheader("How to play")
    st.write("Choose a move and play against the computer.")
    st.write("""
    Rules:
    - Stone beats Scissors
    - Paper beats Stone
    - Scissors beat Paper
    """)
    st.markdown("---")
    st.info("Tip: Share this app link after deploying!")


# Session state for scoreboard
if "wins" not in st.session_state:
    st.session_state.wins = 0
if "losses" not in st.session_state:
    st.session_state.losses = 0
if "draws" not in st.session_state:
    st.session_state.draws = 0


st.subheader("Make your move")

cols = st.columns(3)
with cols[0]:
    if st.button("🪨 Stone", use_container_width=True):
        result, player, comp = play_round(Move.STONE)
        st.session_state.last = (result, player, comp)
with cols[1]:
    if st.button("📄 Paper", use_container_width=True):
        result, player, comp = play_round(Move.PAPER)
        st.session_state.last = (result, player, comp)
with cols[2]:
    if st.button("✂️ Scissors", use_container_width=True):
        result, player, comp = play_round(Move.SCISSORS)
        st.session_state.last = (result, player, comp)

st.markdown("---")


if "last" in st.session_state:
    result, player, comp = st.session_state.last
    st.subheader("Result")
    st.write(f"You {move_to_emoji(player)}  vs  Computer {move_to_emoji(comp)}")

    if result == "draw":
        st.session_state.draws += 1
        st.warning("It's a draw!")
    elif result == "player":
        st.session_state.wins += 1
        st.success("You win! 🎉")
    else:
        st.session_state.losses += 1
        st.error("Computer wins. 😅")


# Scoreboard
st.markdown("---")
st.subheader("Scoreboard")
c1, c2, c3 = st.columns(3)
c1.metric("Wins", st.session_state.wins)
c2.metric("Losses", st.session_state.losses)
c3.metric("Draws", st.session_state.draws)

# Reset button
st.button("Reset Score", on_click=lambda: (st.session_state.update({"wins":0,"losses":0,"draws":0}), st.session_state.pop("last", None)))
