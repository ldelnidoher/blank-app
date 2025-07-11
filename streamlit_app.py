import streamlit as st

# Custom CSS to inject
custom_css = """
<style>
    /* Custom style for the active tab */
    .stTabs > .tablist > .react-tabs__tab--selected {
        background-color: #0e1117;
        color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
    }
    /* Custom style for all tabs */
    .stTabs > .tablist > .react-tabs__tab {
        background-color: #e8e8e8;
        color: #4f4f4f;
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
