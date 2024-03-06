import pandas as pd
import streamlit as st

data_df = (
    {
   "apps": [
            "https://www.serebii.net/pokemon/art/001.png", 
            "https://www.serebii.net/pokemon/art/002.png",
            "https://www.serebii.net/pokemon/art/003.png",
            "https://www.serebii.net/pokemon/art/004.png",
            "https://www.serebii.net/pokemon/art/005.png",
            "https://www.serebii.net/pokemon/art/006.png",
            "https://www.serebii.net/pokemon/art/007.png",
            "https://www.serebii.net/pokemon/art/008.png",
            "https://www.serebii.net/pokemon/art/009.png",
            "https://www.serebii.net/pokemon/art/010.png",
            "https://www.serebii.net/pokemon/art/011.png",
            "https://www.serebii.net/pokemon/art/012.png",
            "https://www.serebii.net/pokemon/art/013.png",
            "https://www.serebii.net/pokemon/art/014.png",
            "https://www.serebii.net/pokemon/art/015.png",
            "https://www.serebii.net/pokemon/art/016.png",
            "https://www.serebii.net/pokemon/art/017.png",
            "https://www.serebii.net/pokemon/art/018.png",
            "https://www.serebii.net/pokemon/art/019.png",
            "https://www.serebii.net/pokemon/art/020.png",
        
        ],
        "ชื่อ Pokemon": ["1.Fushigidane","2.Fushigisou","3.Fushigibana","4.Hitokage","5.Lizardo","6.Lizardon",
                        "7.Zenigame","8.Kameil","9.Kamex","10.Caterpie","11.Transel","12.Butterfree","13.Beedle","14.Cocoon",
                        "15.Spear","16.Poppo","17.Pigeon","18.Pigeot","19.Koratta","20.Ratta"],

    "HP": [45, 60, 80, 39, 58, 78, 44, 59, 79, 45, 50, 60, 40, 45, 65, 40, 63, 83, 30, 55],
    "Atk": [49, 62, 82, 52, 64, 84, 48, 63, 83, 30, 20, 45, 35, 25, 90, 45, 60, 80, 56, 81],
    "Def": [49, 63, 83, 43, 58, 78, 65, 80, 100, 30, 55, 50, 30, 50, 40, 40, 55, 75, 35, 60],
    "Sp. Atk": [65, 80, 100, 60, 80, 109, 50, 65, 85, 20, 25, 90, 20, 25, 45, 35, 50, 70, 25, 50],
    "Sp. def": [65, 80, 100, 50, 65, 85 ,64, 80, 105, 20, 25, 80, 20, 25, 80, 35, 50, 70, 35, 70],
    "Spd": [45, 60, 80, 65, 80, 100, 43, 58, 78, 45, 30, 70, 50, 35, 75, 56, 71, 101, 72, 97],
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