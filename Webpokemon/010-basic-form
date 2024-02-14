import streamlit as st

with st.form('feedback_form'):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input('Enter your name:')
        rating = st.slider('Rate this app:', 0, 10, 5)
    with col2:
        dob = st.date_input('Enter your date of birth:')
        buy = st.radio('Will you buy this app?', ('Yes', 'No'))
    submitted = st.form_submit_button('Submit')

    if submitted:
        st.write('**Name:**', name, '**DOB**', dob, \
            '**Rating**',rating, '**Buy**', buy)