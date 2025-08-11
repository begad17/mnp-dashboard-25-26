import streamlit as st
import matplotlib.pyplot as plt

st.title("League Statistics & History")
st.write("Carousel of images will go here.")
# TODO: Add actual carousel code

# Example manager names and team totals—replace with your data!
manager_names = ['Alex', 'Begad', 'Chase', 'Connor', 'Emmett', 'Fawzi', 'Jordan', 'Logan', 'Michael', 'Moe']
team_totals = [180, 175, 170, 165, 160, 155, 150, 145, 140, 135]  # Replace with actual values

# Calculate win percentages
total_points = sum(team_totals)
win_percentages = [value / total_points * 100 for value in team_totals]

# Create pie chart using matplotlib
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(win_percentages, labels=manager_names, autopct='%1.1f%%', startangle=140)
ax.set_title('Probability To Win The League')
ax.axis('equal')  # Ensures pie is a circle

# Display the matplotlib figure in Streamlit
st.pyplot(fig)
