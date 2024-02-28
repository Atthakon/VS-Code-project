import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
    "Image":["https://drive.google.com/drive/u/0/folders/1dPEWQgmABTK7SOUlphXi39zkZqvPHHQf"],
    
    }
)


st.data_editor(
    data_df,
    column_config={
        "Image": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    hide_index=True,
)