import streamlit as st
from contentgen_app import content_main
from summary_app import summary_main
col1, col2, col3, col4 = st.columns([1,1,6,1])
with col1:
    st.write("")

with col2:
    st.write("")

with col4:
    st.write("")

# Radio buttons for selecting the section
selected_section = st.sidebar.radio("Select Section", ["Generate Blog","Summary"])

def main():
    if selected_section == "Generate Blog":
        content_main()
    elif selected_section == "Summary":
        summary_main()

if __name__ == "__main__":
    main()
