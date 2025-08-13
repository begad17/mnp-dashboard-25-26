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

# Page Title
st.title("Statistics & League History")

# Carousel Slide Selector
slide = st.radio("Select Statistic View:", ["League Titles", "TBD"])

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
