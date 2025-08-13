import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

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
# st.image("draft_results.png", caption="Draft Results", use_column_width=True)


st.set_page_config(layout="wide")

# --- SLIDE SELECTOR (acts like a carousel) ---
slide = st.radio("Select View:", ["Preseason Predictions", "Draft Results"], horizontal=True)

# =========================
# SLIDE 1: PRESEASON PREDICTIONS
# =========================
if slide == "Preseason Predictions":
    # Data
    managers = ["Fawzi", "Connor", "Chase", "Emmett", "Krabbe", "Moe", "Cabs", "Jordan", "Akey", "Begad"]
    predicted_points = [1289.7, 1470.6, 1323.9, 1428.3, 1377.9, 1219.3, 1499.4, 1182.7, 1327.5, 1377.9]

    df = pd.DataFrame({
        "Manager": managers,
        "Predicted Points": predicted_points
    })

    # Sort by points
    df = df.sort_values(by="Predicted Points", ascending=False).reset_index(drop=True)
    df.index += 1
    df.insert(0, "Position", df.index)

    # Highlight top 3
    def highlight_top3(row):
        if row.Position == 1:
            return ['background-color: gold'] * len(row)
        elif row.Position == 2:
            return ['background-color: silver'] * len(row)
        elif row.Position == 3:
            return ['background-color: #cd7f32'] * len(row)  # bronze
        else:
            return [''] * len(row)

    st.title("Preseason Predictions")
    st.dataframe(df.style.apply(highlight_top3, axis=1), use_container_width=True)

# =========================
# SLIDE 2: DRAFT RESULTS
# =========================
elif slide == "Draft Results":
    draft_data = {
        "Manager": ["Draft order", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"],
        "Fawzi": ["1","Salah","Strand Larsen","Semenyo","Amad","Barry","Lewis-Skelly","Milenkovic","Hudson-Odoi","Ruben Dias","Becker","Cherki","Isidor","Konsa","Bayindir","Lamptey"],
        "Connor": ["2","Haaland","Solanke","Evanilson","Neto","Sarr","Brennan Johnson","Kerkez","Murphy","Schar","Adingra","Kadiaglu","Ederson","Kelleher","Lewis-Potter","Van Hecke"],
        "Chase": ["3","Palmer","Wirtz","Welbeck","Havertz","Madueke","Cucurella","Pedro Porro","Iwobi","Grealish","Mitchell","De Ligt","Pope","Guehi","Broja","Areola"],
        "Emmett": ["4","Bruno","Wissa","Mbuemo","Schade","Kluivert","Igor Jesus","Lacroix","Aina","Bruno G","Henderson","Richarlison","De Cuyper","Truffert","Esteve","Onana"],
        "Krabbe": ["5","Watkins","Mateta","Gibbs-White","Delap","Rice","Foden","Timber","Livramento","Mac Allister","Dorgu","Udogie","Mainoo","Wan-Bisaaka","Leno","Mamardashvili"],
        "Moe": ["6","Gyokeres","Sesko","Rogers","Ndiaye","Frimpong","Gvardiol","Branthwaite","Raya","Estevao","Dango","Yoro","Romero","Damsgaard","Verbruggen","Marc Guiu"],
        "Cabs": ["7","Saka","Cunha","Raul","Gakpo","Savinho","Tarkowski","Hall","Enzo","Pickford","Robinson","Beto","Collins","Piroe","Richards","Jose Sa"],
        "Jordan": ["8","Bowen","Joao Pedro","Eze","Virgil","Thiago","Munoz","Georginio","Reijnders","Malen","Sels","O'Brien","Vicario","Diouf","Van de Ven","Arias"],
        "Akey": ["9","Isak","Marmoush","Ode","Gordon","Jackson","Saliba","Murillo","Fullkrug","Calafiori","Konate","Martinez","Martinelli","James","Trafford","McNeil"],
        "Begad": ["10","Hugo","Wood","Elanga","Kudus","Ait-Nouri","Gabriel","Mitoma","N. Williams","Sanchez","Caicedo","Tielemans","Burn","Muniz","Senesi","Meslier"]
    }

    df_draft = pd.DataFrame(draft_data)

    st.title("📋 Draft Results")
    st.dataframe(df_draft, use_container_width=True)

