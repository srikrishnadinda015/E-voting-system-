import streamlit as st

# Mock candidate data
candidates = ["Candidate A", "Candidate B", "Candidate C"]

# Title
st.title("Online Voting System")

# Authentication
def authenticate(username, password):
    # Replace this with your actual authentication logic
    return username == "admin" and password == "admin"

def login():
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            return True
        else:
            st.sidebar.error("Invalid username or password")
    return False

if not login():
    st.stop()

# Voting Interface
if "voted" not in st.session_state:
    st.session_state.voted = False

st.write("Select your candidate:")
selected_candidate = st.selectbox("Candidates", candidates)

if not st.session_state.voted:
    if st.button("Vote"):
        st.session_state.voted = True
        st.success(f"Voted for {selected_candidate}!")
else:
    st.warning("You have already voted!")

# Results Display
st.subheader("Current Voting Results")
# Fetch and display current voting results (can be a simple vote count)
