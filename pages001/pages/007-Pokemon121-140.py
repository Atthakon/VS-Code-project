import pandas as pd
import streamlit as st

data_df = (
    {
   "apps": [
            "https://www.serebii.net/pokemon/art/121.png",
            "https://www.serebii.net/pokemon/art/122.png",
            "https://www.serebii.net/pokemon/art/123.png",
            "https://www.serebii.net/pokemon/art/124.png",
            "https://www.serebii.net/pokemon/art/125.png",
            "https://www.serebii.net/pokemon/art/126.png",
            "https://www.serebii.net/pokemon/art/127.png",
            "https://www.serebii.net/pokemon/art/128.png",
            "https://www.serebii.net/pokemon/art/129.png",
            "https://www.serebii.net/pokemon/art/130.png",
            "https://www.serebii.net/pokemon/art/131.png",
            "https://www.serebii.net/pokemon/art/132.png",
            "https://www.serebii.net/pokemon/art/133.png",
            "https://www.serebii.net/pokemon/art/134.png",
            "https://www.serebii.net/pokemon/art/135.png",
            "https://www.serebii.net/pokemon/art/136.png",
            "https://www.serebii.net/pokemon/art/137.png",
            "https://www.serebii.net/pokemon/art/138.png",
            "https://www.serebii.net/pokemon/art/139.png",
            "https://www.serebii.net/pokemon/art/140.png",
        ],
        "ชื่อ Pokemon": ["121.Starmie","122.Barrierde","123.Strike","124.Rougela","125.Eleboo","126.Boober",
                        "127.Kailios","128.Kentauros","129.Koiking","130.Gyarados","131.Laplace","132.Metamon","133.Eievui","134.Showers","135.Thunders","136.Booster",
                        "137.Porygon","138.Omnite","139.Omstar","140.Kabuto"],

    "HP": [25, 50, 52, 35, 60, 65, 90, 80, 105, 30, 50, 30, 45, 60, 35, 60, 85, 30, 55, 40],
    "Atk": [75, 45, 110, 50, 83, 95, 125, 100, 10, 125, 85, 48, 55, 65, 65, 130, 60, 40, 60, 80],
    "Def": [85, 65, 80, 35, 57, 57, 100, 95, 55, 79, 80, 48, 50, 60, 60, 60, 70, 100, 125, 90],
    "Sp. Atk":[100, 100, 55, 115, 95, 100, 55, 40, 15, 60, 85, 48, 45, 110, 110, 90, 85, 90, 115, 55],
    "Sp. def": [85, 120, 80, 95, 85, 85, 70, 70, 20, 100, 95, 48, 65, 95, 95, 110, 75, 55, 70, 45],
    "Spd": [115, 90, 105, 95, 105, 93, 85, 110, 80, 81, 60, 48, 55, 65, 130, 65, 40, 35, 55, 55],
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