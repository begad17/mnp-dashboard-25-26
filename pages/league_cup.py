import streamlit as st
import random
import graphviz

st.title("The Mickey Cup (Starting GW10?)")

# Fixed managers
bye_managers = ["Jordan", "Begad"]
others = ["Michael", "Logan", "Chase", "Alex", "Fawzi", "Moe", "Emmett", "Connor"]

# Randomize seeds (can later lock this in)
random.shuffle(others)

# Build quarterfinals matchups
qf_matchups = [(others[i], others[i+1]) for i in range(0, len(others), 2)]

# Create Graphviz Digraph
dot = graphviz.Digraph(format="png")
dot.attr(rankdir="LR", size="10", nodesep="0.6", ranksep="1")

# 🎯 Styling
dot.attr("node", shape="rect", style="filled", fontsize="12", fontname="Helvetica-Bold")

# --- ROUND LABELS ---
dot.node("GW10", "GW10 (Quarterfinals)", shape="plaintext", fontsize="14")
dot.node("GW11", "GW11 (Semifinals)", shape="plaintext", fontsize="14")
dot.node("GW12", "GW12 (Finalists)", shape="plaintext", fontsize="14")
dot.node("GW13", "GW13 (Champion)", shape="plaintext", fontsize="14")

# --- QUARTERFINALS (GW10) ---
for i, (m1, m2) in enumerate(qf_matchups, 1):
    qf_node = f"QF{i}"
    dot.node(m1, m1, fillcolor="lightblue")
    dot.node(m2, m2, fillcolor="lightblue")
    dot.node(qf_node, f"Winner QF{i}", fillcolor="white")
    dot.edge(m1, qf_node)
    dot.edge(m2, qf_node)

# --- SEMIFINALS (GW11) ---
dot.node("SF1", "Winner SF1", fillcolor="lightgrey")
dot.node("SF2", "Winner SF2", fillcolor="lightgrey")

# Jordan (bye) vs QF1
dot.node("Jordan", "Jordan", fillcolor="palegreen")
dot.edge("Jordan", "SF1")
dot.edge("QF1", "SF1")

# Begad (bye) vs QF2
dot.node("Begad", "Begad", fillcolor="palegreen")
dot.edge("Begad", "SF2")
dot.edge("QF2", "SF2")

# --- FINAL (GW12) ---
dot.node("Final", "Champion", fillcolor="gold")
dot.edge("SF1", "Final")
dot.edge("SF2", "Final")

# --- CONNECT ROUND LABELS TO BRACKET (acts as separators) ---
dot.edge("GW10", "GW11", style="dashed", arrowhead="none")
dot.edge("GW11", "GW12", style="dashed", arrowhead="none")
dot.edge("GW12", "GW13", style="dashed", arrowhead="none")

# Render in Streamlit
st.graphviz_chart(dot)
