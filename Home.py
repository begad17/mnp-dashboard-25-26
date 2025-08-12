import streamlit as st
from datetime import datetime, timedelta

st.title("Welcome to the 25/26 season")

# Set your kickoff datetime here (replace with actual kickoff datetime)
# Example: Sept 1, 2025, 19:00
kickoff = datetime(2025, 8, 15, 15, 0, 0)

now = datetime.now()
time_left = kickoff - now

if time_left.total_seconds() > 0:
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    st.markdown(f"### GW1 kicks off in: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
else:
    st.markdown("### GW1 has kicked off! 🎉")

# Display draft results image
st.image("draft_results.png", caption="Draft Results", use_column_width=True)
