import pandas as pd
import streamlit as st

data_df = (
    {
   "apps": [
            "https://www.serebii.net/pokemon/art/061.png",
            "https://www.serebii.net/pokemon/art/062.png",
            "https://www.serebii.net/pokemon/art/063.png",
            "https://www.serebii.net/pokemon/art/064.png",
            "https://www.serebii.net/pokemon/art/065.png",
            "https://www.serebii.net/pokemon/art/066.png",
            "https://www.serebii.net/pokemon/art/067.png",
            "https://www.serebii.net/pokemon/art/068.png",
            "https://www.serebii.net/pokemon/art/069.png",
            "https://www.serebii.net/pokemon/art/070.png",
            "https://www.serebii.net/pokemon/art/071.png",
            "https://www.serebii.net/pokemon/art/072.png",
            "https://www.serebii.net/pokemon/art/072.png",
            "https://www.serebii.net/pokemon/art/074.png",
            "https://www.serebii.net/pokemon/art/075.png",
            "https://www.serebii.net/pokemon/art/076.png",
            "https://www.serebii.net/pokemon/art/077.png",
            "https://www.serebii.net/pokemon/art/078.png",
            "https://www.serebii.net/pokemon/art/079.png",
            "https://www.serebii.net/pokemon/art/080.png",

        ],
        "ชื่อ Pokemon": ["61.Nyorozo","62.Nyorobon","63.Casey","64.Yungerer",
                        "65.Foodin","66.Wanriky","67.Goriky","68.Kairiky","69.Madatsubomi","70.Utsudon","71.Utsubot","72.Menokurage",
                        "73.Dokukurage","74.Isitsubute","75.Golone","76.Golonya","77.Ponyta","78.Gallop","79.Yadon","80.Yadoran"],

    "HP": [25, 40, 55, 25, 50, 90, 40, 65, 90, 30, 65, 90, 30, 55, 80, 105, 50, 65, 65, 80],
    "Atk": [65, 95, 20, 35, 50, 80, 100, 130, 75, 90, 105, 40, 70, 80, 95, 120, 85, 100, 65, 75],
    "Def": [65, 95, 15, 30, 45, 50, 70, 80, 35, 50, 65, 35, 65, 100, 115, 130, 55, 70, 65, 110],
    "Sp. Atk":[50, 70, 105, 120, 135, 35, 50, 65, 70, 85, 100, 50, 80, 30, 45, 55, 65, 80, 40, 100],
    "Spd": [80, 40, 105, 90, 95, 35, 60, 80, 70, 80, 95, 50, 40, 70, 45, 45, 25, 75, 100, 60],
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