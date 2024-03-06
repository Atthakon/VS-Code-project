import pandas as pd
import streamlit as st

data_df = (
    {
   "apps": [
            "https://www.serebii.net/pokemon/art/021.png",
            "https://www.serebii.net/pokemon/art/022.png",
            "https://www.serebii.net/pokemon/art/023.png",
            "https://www.serebii.net/pokemon/art/024.png",
            "https://www.serebii.net/pokemon/art/025.png",
            "https://www.serebii.net/pokemon/art/026.png",
            "https://www.serebii.net/pokemon/art/027.png",
            "https://www.serebii.net/pokemon/art/028.png",
            "https://www.serebii.net/pokemon/art/029.png",
            "https://www.serebii.net/pokemon/art/030.png",
            "https://www.serebii.net/pokemon/art/031.png",
            "https://www.serebii.net/pokemon/art/032.png",
            "https://www.serebii.net/pokemon/art/033.png",
            "https://www.serebii.net/pokemon/art/034.png",
            "https://www.serebii.net/pokemon/art/035.png",
            "https://www.serebii.net/pokemon/art/036.png",
            "https://www.serebii.net/pokemon/art/037.png",
            "https://www.serebii.net/pokemon/art/038.png",
            "https://www.serebii.net/pokemon/art/039.png",
            "https://www.serebii.net/pokemon/art/040.png",
        

        ],
        "ชื่อ Pokemon": ["21.Onisuzume","22.Onidrill","23.Arbo","24.Arbok","25.Pikachu","26.Raichu","27.Sand","28.Sandpan","29.Nidoran(Women)","30.Nidorina(Women)",
                        "31.Nidoqueen(Women)","32.Nidoran(men)","33.Nidorino(men)","34.Nidoking(men)","35.Pippi","36.Pixy","37.Rokon",
                        "38.Kyukon","39.Purin","40.Pukurin"],

    "HP": [40, 65, 35, 60, 35, 60, 40, 75, 50, 55, 90, 46, 61, 81, 70, 95, 30, 95, 38, 73],
    "Atk": [60, 90, 60, 95, 55, 90, 75, 100, 47, 62, 92, 57, 72, 102, 45, 70, 41, 76, 45, 70],
    "Def": [30, 65, 44, 69, 40, 55, 85, 110, 52, 67, 87, 40, 57, 77, 48, 73, 40, 75, 20, 45],
    "Sp. Atk": [31, 61, 40, 65, 50, 90, 20, 45, 40, 55, 75, 40, 55, 85, 60, 95, 50, 81, 45, 85],
    "Spd": [70, 100, 55, 80, 90, 110, 40, 65, 41, 56, 76, 50, 65, 85, 35, 45, 60, 60, 35, 45],
        }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", width="medium", help="Streamlit app preview screenshots",
        ),
        "ชื่อ Pokemon": st.column_config.TextColumn(
            "ชื่อ Pokemon",
            help="Streamlit **widget** commands 🎈",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        ),
         "HP": st.column_config.NumberColumn(
            "HP",
            help="HP",
            min_value=0,
            max_value=1000,
            step=1,
        ),
         "Atk": st.column_config.NumberColumn(
            "ATK",
            help="ATK",
            min_value=0,
            max_value=1000,
            step=1,
         ),
    },
    hide_index=True,
    num_rows="dynamic",
)