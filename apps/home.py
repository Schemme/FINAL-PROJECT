import streamlit as st
import 6moy
import mvp
import per_stats

def main():
    st.title('NBA Data Viz Dashboard')
    st.write("This is our final project")
    
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('') # Adding some space for better UI
    
    st.header('Choose an App')
    app_choice = st.selectbox('Select an app to run', ['6moy', 'mvp', 'per-stats'])
    
    if app_choice == '6moy':
        6moy.main()
    elif app_choice == 'mvp':
        mvp.main()
    elif app_choice == 'per-stats':
        per_stats.main()

if __name__ == "__main__":
    main()
