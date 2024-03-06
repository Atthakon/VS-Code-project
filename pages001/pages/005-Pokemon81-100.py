import pandas as pd
import streamlit as st

data_df = (
    {
   "apps": [
            "https://www.serebii.net/pokemon/art/081.png",
            "https://www.serebii.net/pokemon/art/082.png",
            "https://www.serebii.net/pokemon/art/083.png",
            "https://www.serebii.net/pokemon/art/084.png",
            "https://www.serebii.net/pokemon/art/085.png",
            "https://www.serebii.net/pokemon/art/086.png",
            "https://www.serebii.net/pokemon/art/087.png",
            "https://www.serebii.net/pokemon/art/088.png",
            "https://www.serebii.net/pokemon/art/089.png",
            "https://www.serebii.net/pokemon/art/090.png",
            "https://www.serebii.net/pokemon/art/091.png",
            "https://www.serebii.net/pokemon/art/092.png",
            "https://www.serebii.net/pokemon/art/093.png",
            "https://www.serebii.net/pokemon/art/094.png",
            "https://www.serebii.net/pokemon/art/095.png",
            "https://www.serebii.net/pokemon/art/096.png",
            "https://www.serebii.net/pokemon/art/097.png",
            "https://www.serebii.net/pokemon/art/098.png",
            "https://www.serebii.net/pokemon/art/099.png",
            "https://www.serebii.net/pokemon/art/100.png",

        ],
        "ชื่อ Pokemon": ["81.Coil","82.Rarecoil","83.Kamonegi","84.Dodo","85.Dodorio","86.Pawou","87.Jugon","88.Betbeter",
                        "89.Betbeton","90.Shellder","91.Parshen","92.Ghos","93.Ghost","94.Gangar","95.Iwark","96.Sleepe","97.Sleeper",
                        "98.Crab","99.Kingler","100.Biriridama"],

    "HP": [25, 50, 52, 35, 60, 65, 90, 80, 105, 30, 50, 30, 45, 60, 35, 60, 85, 30, 55, 40],
    "Atk": [35, 60, 90, 85, 110, 45, 70, 80, 105, 65, 90, 35, 50, 65, 45, 48, 73, 105, 130, 30],
    "Def": [70, 95, 55, 45, 70, 55, 80, 50, 75, 100, 180, 30, 45, 60, 160, 45, 70, 90, 115, 50],
    "Sp. Atk":[95, 120, 58, 35, 60, 45, 70, 40, 65, 45, 85, 100, 115, 130, 30, 43, 73, 25, 50, 55],
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