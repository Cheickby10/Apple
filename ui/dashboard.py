import streamlit as st
from core.simulator import run_crash_sim, run_mines_sim
from core.bayesian_edge import BayesianEdge
from risk.kelly import kelly

def show_dashboard():

    game = st.selectbox("Select Game", ["Crash", "Mines"])
    rounds = st.slider("Simulation rounds", 100, 20000, 1000)

    if st.button("Run Analysis"):

        if game == "Crash":
            history, edge = run_crash_sim(rounds)
        else:
            history, edge = run_mines_sim(rounds)

        st.line_chart(history)
        st.metric("Bayesian Edge", round(edge, 4))
        st.metric("Kelly Fraction", round(kelly(edge, 1), 4))
