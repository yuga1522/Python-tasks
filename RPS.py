# Rock Paper Scissors — Upgraded (fixed rerun)
# Features: Single-player vs Computer, Two-player local, Best-of-N match, Animated reveal
import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="Rock Paper Scissors — Upgraded", layout="centered")

# -------------------------
# Compatibility helper for rerun
# -------------------------
def rerun_app():
    """
    Call Streamlit's rerun in a way that works across versions.
    Prefer st.rerun(); fall back to st.experimental_rerun() if present.
    """
    if hasattr(st, "rerun"):
        st.rerun()
    elif hasattr(st, "experimental_rerun"):
        st.experimental_rerun()
    else:
        # If neither exists, do nothing (app will re-run on next interaction)
        return

# -------------------------
# Helper functions
# -------------------------
def init_state():
    if "mode" not in st.session_state:
        st.session_state.mode = "Single Player"
    if "best_of" not in st.session_state:
        st.session_state.best_of = 3
    if "scores" not in st.session_state:
        st.session_state.scores = {"Player 1": 0, "Player 2": 0, "Computer": 0, "Draws": 0}
    if "history" not in st.session_state:
        st.session_state.history = []  # list of dicts
    if "current_round" not in st.session_state:
        st.session_state.current_round = 1
    if "player_turn" not in st.session_state:
        st.session_state.player_turn = 1  # used in two-player mode
    if "match_over" not in st.session_state:
        st.session_state.match_over = False
    if "last_result" not in st.session_state:
        st.session_state.last_result = None  # store last round result dict

def choice_emoji(choice):
    return {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}.get(choice, "")

def decide_winner(p1, p2):
    if p1 == p2:
        return "Draw"
    wins = {("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")}
    return "Player1" if (p1, p2) in wins else "Player2"

def compute_result(player_choice, opponent_choice, p1_label="You", p2_label="Computer"):
    if player_choice == opponent_choice:
        return "Draw", f"{p1_label} {choice_emoji(player_choice)} = {p2_label} {choice_emoji(opponent_choice)}"
    wins = {("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")}
    if (player_choice, opponent_choice) in wins:
        return "Win", f"{p1_label} {choice_emoji(player_choice)} beats {p2_label} {choice_emoji(opponent_choice)}"
    else:
        return "Lose", f"{p2_label} {choice_emoji(opponent_choice)} beats {p1_label} {choice_emoji(player_choice)}"

def record_round(winner_label, p1_choice, p2_choice, p1_name="Player 1", p2_name="Player 2"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rec = {
        "Time": timestamp,
        "P1": f"{choice_emoji(p1_choice)} {p1_choice}",
        "P2": f"{choice_emoji(p2_choice)} {p2_choice}",
        "Winner": winner_label
    }
    st.session_state.history.insert(0, rec)
    st.session_state.last_result = rec

def reset_match():
    st.session_state.scores = {"Player 1": 0, "Player 2": 0, "Computer": 0, "Draws": 0}
    st.session_state.history = []
    st.session_state.current_round = 1
    st.session_state.player_turn = 1
    st.session_state.match_over = False
    st.session_state.last_result = None

def check_match_over():
    required = st.session_state.best_of // 2 + 1
    if st.session_state.mode == "Single Player":
        if st.session_state.scores.get("You", 0) >= required or st.session_state.scores.get("Computer", 0) >= required:
            st.session_state.match_over = True
    else:
        if st.session_state.scores.get("Player 1", 0) >= required or st.session_state.scores.get("Player 2", 0) >= required:
            st.session_state.match_over = True

# Animated reveal (simple)
def animated_reveal():
    with st.spinner("Choosing..."):
        for _ in range(3):
            time.sleep(0.25)
    time.sleep(0.15)

# -------------------------
# Initialize state
# -------------------------
init_state()

# -------------------------
# Page UI
# -------------------------
st.title("🪨📄✂️ Rock Paper Scissors — Upgraded")
st.write("Choose a mode, pick best-of rounds, and play. Two-player local mode lets two people play on the same device.")

# Settings
with st.expander("Game Settings", expanded=True):
    col_a, col_b = st.columns(2)
    with col_a:
        mode = st.selectbox("Mode", ["Single Player", "Two Player (Local)"], index=0 if st.session_state.mode=="Single Player" else 1)
    with col_b:
        bo = st.selectbox("Best of", [1,3,5,7,9], index=[1,3,5,7,9].index(st.session_state.best_of) if st.session_state.best_of in [1,3,5,7,9] else 1)
    if st.button("Apply Settings"):
        st.session_state.mode = mode
        st.session_state.best_of = bo
        reset_match()
        st.success(f"Mode set to {mode}; Best of {bo}. Match reset.")

st.markdown("---")

# Scoreboard
st.subheader("Scoreboard")
if st.session_state.mode == "Single Player":
    if "You" not in st.session_state.scores:
        st.session_state.scores["You"] = 0
    if "Computer" not in st.session_state.scores:
        st.session_state.scores["Computer"] = 0
    scores = {"You": st.session_state.scores["You"], "Computer": st.session_state.scores["Computer"], "Draws": st.session_state.scores.get("Draws", 0)}
else:
    scores = {"Player 1": st.session_state.scores.get("Player 1", 0), "Player 2": st.session_state.scores.get("Player 2", 0), "Draws": st.session_state.scores.get("Draws", 0)}

c1, c2, c3, c4 = st.columns([1,1,1,2])
c1.metric(list(scores.keys())[0], list(scores.values())[0])
c2.metric(list(scores.keys())[1], list(scores.values())[1])
c3.metric("Draws", scores.get("Draws", 0))
with c4:
    if st.button("🔄 Reset Match"):
        reset_match()
        st.success("Match reset")

st.markdown("---")

# Play area
st.subheader(f"Round {st.session_state.current_round} — {st.session_state.mode}")

# Single Player Mode
if st.session_state.mode == "Single Player":
    st.write("Pick your move:")
    col_r, col_p, col_s = st.columns(3)
    player_choice = None
    if col_r.button("✊ Rock"):
        player_choice = "Rock"
    if col_p.button("✋ Paper"):
        player_choice = "Paper"
    if col_s.button("✌️ Scissors"):
        player_choice = "Scissors"

    if player_choice and not st.session_state.match_over:
        animated_reveal()
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])
        result, desc = compute_result(player_choice, comp_choice, p1_label="You", p2_label="Computer")
        if result == "Win":
            st.session_state.scores["You"] = st.session_state.scores.get("You", 0) + 1
            winner_label = "You"
        elif result == "Lose":
            st.session_state.scores["Computer"] = st.session_state.scores.get("Computer", 0) + 1
            winner_label = "Computer"
        else:
            st.session_state.scores["Draws"] = st.session_state.scores.get("Draws", 0) + 1
            winner_label = "Draw"

        record_round(winner_label, player_choice, comp_choice, p1_name="You", p2_name="Computer")

        if result == "Win":
            st.success(f"You Win! {desc}")
        elif result == "Lose":
            st.error(f"You Lose! {desc}")
        else:
            st.info(f"Draw! {desc}")

        st.session_state.current_round += 1
        check_match_over()
        if st.session_state.match_over:
            if st.session_state.scores.get("You", 0) > st.session_state.scores.get("Computer", 0):
                st.balloons()
                st.success(f"Match Over — You win Best of {st.session_state.best_of}!")
            elif st.session_state.scores.get("You", 0) < st.session_state.scores.get("Computer", 0):
                st.error(f"Match Over — Computer wins Best of {st.session_state.best_of}!")
            else:
                st.info("Match Over — It's a tie!")

# Two Player Local Mode
else:
    st.write("Two-player local: Player 1 goes first each round, then Player 2. Choose privately when it's your turn.")
    p1_choice = None
    p2_choice = None

    if st.session_state.player_turn == 1:
        st.info("Player 1's turn — pick a move")
        c1, c2, c3 = st.columns(3)
        if c1.button("✊ Rock", key="p1_rock"):
            p1_choice = "Rock"
        if c2.button("✋ Paper", key="p1_paper"):
            p1_choice = "Paper"
        if c3.button("✌️ Scissors", key="p1_scissors"):
            p1_choice = "Scissors"
        if p1_choice:
            st.session_state._p1_choice = p1_choice
            st.session_state.player_turn = 2
            # trigger immediate rerun to switch view
            rerun_app()
    else:
        st.info("Player 2's turn — pick a move")
        c1, c2, c3 = st.columns(3)
        if c1.button("✊ Rock", key="p2_rock"):
            p2_choice = "Rock"
        if c2.button("✋ Paper", key="p2_paper"):
            p2_choice = "Paper"
        if c3.button("✌️ Scissors", key="p2_scissors"):
            p2_choice = "Scissors"
        if p2_choice:
            p1_choice_val = st.session_state.get("_p1_choice", None)
            if p1_choice_val is None:
                st.error("Player 1 choice missing. Resetting turn.")
                st.session_state.player_turn = 1
            else:
                animated_reveal()
                comp_result = decide_winner(p1_choice_val, p2_choice)
                if comp_result == "Draw":
                    winner_label = "Draw"
                    st.session_state.scores["Draws"] = st.session_state.scores.get("Draws", 0) + 1
                    st.info(f"Draw! {choice_emoji(p1_choice_val)} = {choice_emoji(p2_choice)}")
                elif comp_result == "Player1":
                    winner_label = "Player 1"
                    st.session_state.scores["Player 1"] = st.session_state.scores.get("Player 1", 0) + 1
                    st.success(f"Player 1 wins! {choice_emoji(p1_choice_val)} beats {choice_emoji(p2_choice)}")
                else:
                    winner_label = "Player 2"
                    st.session_state.scores["Player 2"] = st.session_state.scores.get("Player 2", 0) + 1
                    st.error(f"Player 2 wins! {choice_emoji(p2_choice)} beats {choice_emoji(p1_choice_val)}")

                record_round(winner_label, p1_choice_val, p2_choice, p1_name="Player 1", p2_name="Player 2")

                if "_p1_choice" in st.session_state:
                    del st.session_state["_p1_choice"]
                st.session_state.player_turn = 1
                st.session_state.current_round += 1
                check_match_over()
                if st.session_state.match_over:
                    if st.session_state.scores.get("Player 1", 0) > st.session_state.scores.get("Player 2", 0):
                        st.balloons()
                        st.success(f"Match Over — Player 1 wins Best of {st.session_state.best_of}!")
                    elif st.session_state.scores.get("Player 1", 0) < st.session_state.scores.get("Player 2", 0):
                        st.success(f"Match Over — Player 2 wins Best of {st.session_state.best_of}!")
                    else:
                        st.info("Match Over — It's a tie!")

st.markdown("---")

# History and controls
st.subheader("Recent Rounds")
if not st.session_state.history:
    st.info("No rounds played yet.")
else:
    hist = st.session_state.history[:10]
    st.table(hist)

st.markdown("---")
st.write("Tips:")
st.write("- Use Best-of to set the match length (e.g., Best of 3 means first to 2 wins).")
st.write("- In Two-player local mode, Player 1 chooses first, then Player 2. Keep choices private between turns.")
st.write("- Click Reset Match to clear scores and history.")
