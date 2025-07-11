import streamlit as st

# Custom CSS to inject
custom_css = """
<style>
    /* Custom style for the active tab */
    .stTabs > .tablist > .react-tabs__tab--selected {
        background-color: #f505cd;
        color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
    }
    /* Custom style for all tabs */
    .stTabs > .tablist > .st-emotion-cache-bfgnao {
        background-color: #e8e8e8;
        color: #f50202;
        font-family: 'Courier New', Courier, monospace;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
# Example usage of tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Content in tab 1")

with tab2:
    st.write("Content in tab 2")



