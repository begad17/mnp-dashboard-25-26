import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("League Statistics & History")
# TODO: Add actual carousel code

# Example manager names and team totals—replace with your data!
manager_names = ['Alex', 'Begad', 'Chase', 'Connor', 'Emmett', 'Fawzi', 'Jordan', 'Logan', 'Michael', 'Moe']
team_totals = [.08, .08, .03, .11, .03, .14, .17, .09, .08, .19]  # Replace with actual values

# Calculate win percentages
# total_points = sum(team_totals)
win_percentages = [value  * 100 for value in team_totals]

# Create pie chart using matplotlib
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(win_percentages, labels=manager_names, autopct='%1.1f%%', startangle=140)
ax.set_title('Probability To Win The League')
ax.axis('equal')  # Ensures pie is a circle

# Display the matplotlib figure in Streamlit
# st.pyplot(fig)

# Carousel Slide Selector
slide = st.radio("League Statistics:", ["League Titles", "TBD"])

# League Titles Pie Chart
if slide == "League Titles":
    leagueWins = {'Team':['Jordan (1)','Begad (1)','Moe (1)'], 'Championships':[1,1,1]}
    df = pd.DataFrame(leagueWins)
    teamColours = ['#f40206','#0560b5','#ce0000']

    fig, ax = plt.subplots()
    ax.pie(
        df['Championships'],
        labels=df['Team'],
        colors=teamColours,
        startangle=90,
        autopct='%1.1f%%'
    )
    ax.set_title("MoneyNotPassion League Titles")
    ax.axis('equal')

    st.pyplot(fig)

st.set_page_config(layout="wide")

# Carousel navigation
slide = st.radio(
    "League Table History",
    ["22/23 Season", "23/24 Season", "24/25 Season"],
    horizontal=True
)

def make_table(title, managers):
    """Helper to create position table from list of managers"""
    df = pd.DataFrame({
        "Position": list(range(1, len(managers) + 1)),
        "Manager": managers
    })
    st.subheader(title)
    st.table(df)

# --- SLIDE 1 ---
if slide == "22/23 Season":
    st.title("22/23 Season Review")
    col1, col2 = st.columns(2)

    with col1:
        make_table("Preseason Predictions", [
            "Chase", "Jordan", "Mustafa", "Fawzi", "Begad",
            "Alex", "Emmett", "Moe", "Connor", "Michael"
        ])

    with col2:
        make_table("Final Standings", [
            "Jordan", "Michael", "Begad", "Moe", "Connor",
            "Chase", "Emmett", "Alex", "Fawzi", "Mustafa"
        ])

# --- SLIDE 2 ---
elif slide == "23/24 Season":
    st.title("23/24 Season Review")
    col1, col2 = st.columns(2)

    with col1:
        make_table("Preseason Predictions", [
            "Fawzi", "Emmett", "Logan", "Michael", "Jordan",
            "Begad", "Alex", "Connor", "Moe", "Chase"
        ])

    with col2:
        make_table("Final Standings", [
            "Begad", "Moe", "Logan", "Jordan", "Fawzi",
            "Michael", "Emmett", "Chase", "Connor", "Alex"
        ])

# --- SLIDE 3 ---
elif slide == "24/25 Season":
    st.title("24/25 Season Review")
    col1, col2 = st.columns(2)

    with col1:
        make_table("Preseason Predictions", [
            "Logan", "Jordan", "Moe", "Begad", "Chase",
            "Michael", "Connor", "Fawzi", "Emmett", "Alex"
        ])

    with col2:
        make_table("Final Standings", [
            "Moe", "Connor", "Fawzi", "Michael", "Logan",
            "Alex", "Jordan", "Begad", "Emmett", "Chase"
        ])
