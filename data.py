import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
    "Image":["https://www.serebii.net/pokemon/art/001.png","https://www.serebii.net/pokemon/art/002.png","https://www.serebii.net/pokemon/art/003.png","https://www.serebii.net/pokemon/art/004.png","https://www.serebii.net/pokemon/art/005.png"
              ,"https://www.serebii.net/pokemon/art/006.png","https://www.serebii.net/pokemon/art/007.png","https://www.serebii.net/pokemon/art/008.png","https://www.serebii.net/pokemon/art/009.png","https://www.serebii.net/pokemon/art/010.png"
             
             ],
    
    }
)
df = pd.DataFrame(
    [
       {"Name": "Fushigidane", "Base Stats" : "Type grass poison" , "HP" : 45, "Att" : 49},
       {"Name": "Fushigisou", "Base Stats" : "Type grass poison" , "HP" : 60, "Att" : 62},
       {"Name": "Fushigibana", "Base Stats" : "Type grass poison" , "HP" : 80, "Att" : 82},
   ]
)


st.data_editor(
    data_df,
    column_config={
        "Image": st.column_config.ImageColumn("Preview Image", width = "medium" ),
        "Name": st.column_config.TextColumn("Name" ),
        
    },

    hide_index=True,
)

