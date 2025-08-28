import streamlit as st
import random
import graphviz

st.title("The Mickey Cup")

# Fixed managers
bye_managers = ["Jordan", "Begad"]
others = ["Michael", "Logan", "Chase", "Alex", "Fawzi", "Moe", "Emmett", "Connor"]

# Randomize seeds
random.shuffle(others)

# Build quarterfinals matchups
qf_matchups = [(others[i], others[i+1]) for i in range(0, len(others), 2)]

# Create Graphviz Digraph
dot = graphviz.Digraph(format="png")
dot.attr(rankdir="LR", size="8")

# Quarterfinals
for i, (m1, m2) in enumerate(qf_matchups, 1):
    qf_node = f"QF{i}"
    dot.node(f"{m1}", m1, shape="box", style="filled", color="lightblue")
    dot.node(f"{m2}", m2, shape="box", style="filled", color="lightblue")
    dot.node(qf_node, f"QF{i} Winner", shape="ellipse", style="filled", color="lightgrey")
    dot.edge(m1, qf_node)
    dot.edge(m2, qf_node)

# Semifinals
dot.node("SF1", "Winner SF1", shape="ellipse", style="filled", color="orange")
dot.node("SF2", "Winner SF2", shape="ellipse", style="filled", color="orange")

# Jordan vs QF1
dot.node("Jordan", "Jordan", shape="box", style="filled", color="lightgreen")
dot.edge("Jordan", "SF1")
dot.edge("QF1", "SF1")

# Begad vs QF2
dot.node("Begad", "Begad", shape="box", style="filled", color="lightgreen")
dot.edge("Begad", "SF2")
dot.edge("QF2", "SF2")

# Final
dot.node("Final", "Champion", shape="ellipse", style="filled", color="gold")
dot.edge("SF1", "Final")
dot.edge("SF2", "Final")

# Render in Streamlit
st.graphviz_chart(dot)
