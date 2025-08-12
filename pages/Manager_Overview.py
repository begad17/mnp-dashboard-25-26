import streamlit as st
import pandas as pd

# --- Define your 10 managers and their data manually ---
managers = [
    "Alex",
    "Begad",
    "Chase",
    "Connor",
    "Emmett",
    "Fawzi",
    "Jordan",
    "Logan",
    "Michael",
    "Moe"
]

# Example data for each manager (replace with your actual data)
# Data format: List of dicts or a DataFrame for each manager
manager_data = {
    "Manager 1": pd.DataFrame([
        {"Result": "W", "For": 3, "Against": 1},
        {"Result": "L", "For": 0, "Against": 2},
        {"Result": "D", "For": 2, "Against": 2},
    ]),
    "Manager 2": pd.DataFrame([
        {"Result": "W", "For": 2, "Against": 0},
        {"Result": "W", "For": 1, "Against": 0},
        {"Result": "L", "For": 0, "Against": 3},
    ]),
    # Add data for other managers similarly...
}

# --- STREAMLIT UI ---
st.sidebar.title("Manager Selector")
selected_manager = st.sidebar.selectbox("Select Manager", managers)

st.title(f"📊 {selected_manager} Overview")

# Load the data for the selected manager
df = manager_data.get(selected_manager, pd.DataFrame())

if not df.empty:
    # Defensive check for columns
    for col in ["Result", "For", "Against"]:
        if col not in df.columns:
            st.error(f"Column '{col}' missing for {selected_manager}.")
            st.stop()

    # Calculate stats
    wins = (df["Result"] == "W").sum()
    losses = (df["Result"] == "L").sum()
    draws = (df["Result"] == "D").sum() if "D" in df["Result"].values else 0

    avg_for = df["For"].mean()
    avg_against = df["Against"].mean()

    # Show the table and stats
    st.dataframe(df)

    st.markdown(f"""
    **Wins:** {wins} | **Losses:** {losses} | **Draws:** {draws}  
    **Average For:** {avg_for:.1f} | **Average Against:** {avg_against:.1f}
    """)

    st.bar_chart(df[["For", "Against"]])

else:
    st.warning("No data available for this manager.")
