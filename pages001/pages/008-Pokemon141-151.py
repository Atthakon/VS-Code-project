import pandas as pd
import streamlit as st

data_df = (
    {
   "apps": [
             "https://www.serebii.net/pokemon/art/141.png",
            "https://www.serebii.net/pokemon/art/142.png",
            "https://www.serebii.net/pokemon/art/143.png",
            "https://www.serebii.net/pokemon/art/144.png",
            "https://www.serebii.net/pokemon/art/145.png",
            "https://www.serebii.net/pokemon/art/146.png",
            "https://www.serebii.net/pokemon/art/147.png",
            "https://www.serebii.net/pokemon/art/148.png",
            "https://www.serebii.net/pokemon/art/149.png",
            "https://www.serebii.net/pokemon/art/150.png",
            "https://www.serebii.net/pokemon/art/151.png",

        ],
        "ชื่อ Pokemon": ["141.Kabutops","142.Ptera","143.Kabigon","144.Freezer","145.Thunder","146.Fire","147.Miniryu",
                        "148.Hakuryu","149.Kairyu","150.Mewtwo","151.Mew"],

    "HP": [60, 80, 160, 90, 90, 90, 41, 61, 91, 106, 100],
    "Atk": [115, 105, 110, 85, 90, 100, 64, 84, 134, 110, 100],
    "Def": [105, 60, 60, 100, 85, 90, 45, 65, 95, 90, 100],
    "Sp. Atk":[60, 60, 65, 95, 120, 125, 50, 70, 100, 154, 100],
    "Sp. def": [70, 75, 110, 125, 90, 85, 50, 70, 100, 90, 100],
    "Spd": [80, 130, 30, 85, 100, 90, 50, 70, 80, 130, 100],
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