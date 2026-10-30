import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="DevStudio | Python Playground",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}
.block-container {
    padding-top: 2rem;
}
[data-testid="stSidebar"] {
    background-color: #111827;
}
[data-testid="stSidebar"] * {
    color: white;
}
div.stButton > button {
    border-radius: 8px;
    font-weight: 600;
    padding: 0.5rem 1.2rem;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("💻 DevStudio")
st.sidebar.caption("Python Development Workspace")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "Code Editor",
        "Variables",
        "Functions",
        "Loops",
        "API Testing",
        "Console"
    ]
)

st.sidebar.markdown("---")

st.sidebar.subheader("⚙️ Preferences")

theme = st.sidebar.selectbox(
    "Editor Theme",
    ["Light", "Dark"]
)

font_size = st.sidebar.slider(
    "Font Size",
    10, 24, 14
)

st.sidebar.markdown("---")
st.sidebar.caption("DevStudio v1.0")

# ============================================================
# HEADER
# ============================================================

st.title("💻 DevStudio")

st.caption(
    "A clean workspace for experimenting with Python "
    "and exploring programming concepts."
)

st.markdown("---")

# ============================================================
# OVERVIEW PAGE
# ============================================================

if page == "Overview":

    st.subheader("Welcome to your workspace")

    col1, col2, col3 = st.columns(3)

    col1.info("🐍 Python\n\nExperiment with Python code.")
    col2.info("🧪 Testing\n\nExplore inputs and outputs.")
    col3.info("⚡ Workspace\n\nOrganize your experiments.")

    st.markdown("### Quick Access")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Open Code Editor", use_container_width=True):
            st.session_state.page = "Code Editor"
            st.rerun()

    with col2:
        if st.button("Open Console", use_container_width=True):
            st.session_state.page = "Console"
            st.rerun()

# ============================================================
# CODE EDITOR
# ============================================================

elif page == "Code Editor":

    st.subheader("📝 Code Editor")

    code = st.text_area(
        "Write your Python code",
        height=350,
        placeholder="Write your Python code here...",
        value="print('Hello, World!')"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "▶ Run Code",
            type="primary",
            use_container_width=True
        )

    with col2:
        st.button(
            "Clear Editor",
            use_container_width=True
        )

    st.markdown("### Output")

    st.code(
        "Output will appear here...",
        language="text"
    )

# ============================================================
# VARIABLES
# ============================================================

elif page == "Variables":

    st.subheader("📦 Variable Explorer")

    variable_name = st.text_input(
        "Variable Name"
    )

    variable_value = st.text_input(
        "Variable Value"
    )

    variable_type = st.selectbox(
        "Variable Type",
        ["String", "Integer", "Float", "Boolean", "List"]
    )

    st.button(
        "Create Variable",
        type="primary"
    )

    st.markdown("### Variable Information")

    st.info("Variable information will appear here.")

# ============================================================
# FUNCTIONS
# ============================================================

elif page == "Functions":

    st.subheader("⚙️ Function Workspace")

    function_name = st.text_input(
        "Function Name",
        placeholder="Enter function name"
    )

    parameters = st.text_input(
        "Parameters",
        placeholder="a, b"
    )

    function_code = st.text_area(
        "Function Body",
        height=200,
        placeholder="Write your function logic..."
    )

    st.button(
        "Create Function",
        type="primary"
    )

# ============================================================
# LOOPS
# ============================================================

elif page == "Loops":

    st.subheader("🔁 Loop Playground")

    loop_type = st.selectbox(
        "Select Loop Type",
        ["For Loop", "While Loop"]
    )

    iterations = st.slider(
        "Number of Iterations",
        1, 100, 10
    )

    loop_code = st.text_area(
        "Loop Code",
        height=200,
        placeholder="Write your loop code..."
    )

    st.button(
        "Test Loop",
        type="primary"
    )

# ============================================================
# API TESTING
# ============================================================

elif page == "API Testing":

    st.subheader("🌐 API Testing Interface")

    api_url = st.text_input(
        "API Endpoint",
        placeholder="https://api.example.com"
    )

    method = st.selectbox(
        "HTTP Method",
        ["GET", "POST", "PUT", "DELETE", "PATCH"]
    )

    headers = st.text_area(
        "Request Headers",
        placeholder="Enter request headers..."
    )

    payload = st.text_area(
        "Request Body",
        placeholder="Enter JSON payload..."
    )

    st.button(
        "Send Request",
        type="primary"
    )

    st.markdown("### Response")

    st.info("API response will appear here.")

# ============================================================
# CONSOLE
# ============================================================

elif page == "Console":

    st.subheader("🖥️ Console")

    command = st.text_input(
        "Enter command",
        placeholder="Enter a command..."
    )

    st.button(
        "Execute",
        type="primary"
    )

    st.markdown("### Console Output")

    st.code(
        "Console output will appear here...",
        language="text"
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "DevStudio | Python Development Workspace"
)
