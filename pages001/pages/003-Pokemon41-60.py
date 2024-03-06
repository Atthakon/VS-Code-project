import pandas as pd
import streamlit as st

data_df = (
    {
   "apps": [
            "https://www.serebii.net/pokemon/art/041.png",
            "https://www.serebii.net/pokemon/art/042.png",
            "https://www.serebii.net/pokemon/art/044.png",
            "https://www.serebii.net/pokemon/art/044.png",
            "https://www.serebii.net/pokemon/art/045.png",
            "https://www.serebii.net/pokemon/art/046.png",
            "https://www.serebii.net/pokemon/art/047.png",
            "https://www.serebii.net/pokemon/art/048.png",
            "https://www.serebii.net/pokemon/art/049.png",
            "https://www.serebii.net/pokemon/art/050.png",
            "https://www.serebii.net/pokemon/art/051.png",
            "https://www.serebii.net/pokemon/art/052.png",
            "https://www.serebii.net/pokemon/art/053.png",
            "https://www.serebii.net/pokemon/art/054.png",
            "https://www.serebii.net/pokemon/art/055.png",
            "https://www.serebii.net/pokemon/art/056.png",
            "https://www.serebii.net/pokemon/art/057.png",
            "https://www.serebii.net/pokemon/art/058.png",
            "https://www.serebii.net/pokemon/art/059.png",
            "https://www.serebii.net/pokemon/art/060.png",
        

        ],
        "ชื่อ Pokemon": ["41.Zubat","42.Golbat","43.Nazonokusa","44.Kusaihana","45.Ruffresia","46.Paras",
                        "47.Parasect","48.Kongpang","49.Morphon","50.Digda","51.Dugtrio","52.Nyarth","53.Persian","54.Koduck","55.Golduck",
                        "56.Mankey","57.Okorizaru","58.Gardie","59.Windie","60.Nyoromo"],

    "HP": [115, 140, 40, 75, 45, 60, 75, 35, 60, 60, 70, 10, 35, 40, 65, 50, 80, 40, 65, 90],
    "Atk": [45, 80, 50, 65, 80, 70, 95, 55, 65, 55, 100, 45, 70, 52, 82, 80, 105, 70, 110, 50],
    "Def": [35, 70, 55, 70, 85, 55, 80, 50, 60, 50, 35, 40, 60, 48, 78, 35, 60, 45, 80, 40],
    "Sp. Atk": [30, 65, 75, 85, 110, 45, 60, 40, 90, 35, 50, 40, 65, 65, 95, 35, 60, 70, 100, 40],
    "Spd": [65, 100, 70, 100, 20, 90, 75, 100, 30, 50, 35, 45, 45, 55, 90, 95, 70, 70, 100, 90],
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