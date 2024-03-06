import pandas as pd
import streamlit as st

data_df = (
    {
   "apps": [
            "https://www.serebii.net/pokemon/art/101.png",
            "https://www.serebii.net/pokemon/art/102.png",
            "https://www.serebii.net/pokemon/art/103.png",
            "https://www.serebii.net/pokemon/art/104.png",
            "https://www.serebii.net/pokemon/art/105.png",
            "https://www.serebii.net/pokemon/art/106.png",
            "https://www.serebii.net/pokemon/art/107.png",
            "https://www.serebii.net/pokemon/art/108.png",
            "https://www.serebii.net/pokemon/art/109.png",
            "https://www.serebii.net/pokemon/art/110.png",
            "https://www.serebii.net/pokemon/art/111.png",
            "https://www.serebii.net/pokemon/art/112.png",
            "https://www.serebii.net/pokemon/art/113.png",
            "https://www.serebii.net/pokemon/art/114.png",
            "https://www.serebii.net/pokemon/art/115.png",
            "https://www.serebii.net/pokemon/art/116.png",
            "https://www.serebii.net/pokemon/art/117.png",
            "https://www.serebii.net/pokemon/art/118.png",
            "https://www.serebii.net/pokemon/art/119.png",
            "https://www.serebii.net/pokemon/art/120.png",
        ],
        "ชื่อ Pokemon": ["101.Marumine","102.Tamatama","103.Nassy","104.Karakara","105.Garagara","106.Sawamular",
                        "107.Ebiwalar","108.Beroringa","109.Dogars","110.Matadogas","111.Sihorn","112.Sidon","113.Lucky","114.Monjara","115.Garura","116.Tattu",
                        "117.Seadra","118.Tosakinto","119.Azumao","120.Hitodeman"],

    "HP": [25, 50, 52, 35, 60, 65, 90, 80, 105, 30, 50, 30, 45, 60, 35, 60, 85, 30, 55, 40],
    "Atk": [50, 40, 95, 50, 80, 120, 105, 55, 65, 90, 85, 130, 5, 55, 95, 40, 65, 67, 92, 45],
    "Def": [70, 80, 85, 95, 110, 53, 79, 75, 95, 120, 95, 120, 5, 115, 80, 70, 95, 60, 65, 55],
    "Sp. Atk":[80, 60, 125, 40, 50, 35, 35, 60, 60, 85, 30, 45, 35, 100, 40, 70, 95, 35, 65, 70],
    "Spd": [30, 67, 76, 50, 110, 40, 85, 65, 68, 85, 40, 60, 90, 30, 80, 100, 140, 100, 130, 100],
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