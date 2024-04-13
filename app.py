import streamlit as st
import requests

# Define Streamlit UI components
def main():
    st.title("Online Voting System")
    page = st.sidebar.selectbox("Select Page", ["Register", "Login", "Select Party", "Vote"])

    if page == "Register":
        register_page()
    elif page == "Login":
        login_page()
    elif page == "Select Party":
        party_selection_page()
    elif page == "Vote":
        voting_page()

# User registration page
def register_page():
    st.title("User Registration")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        # Call backend API to register user
        response = requests.post("https://your-backend-api/register", json={"username": username, "password": password})
        if response.status_code == 201:
            st.success("User registered successfully")
        else:
            st.error("User registration failed")

# User login page
def login_page():
    st.title("User Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Call backend API to authenticate user
        response = requests.post("https://your-backend-api/login", json={"username": username, "password": password})
        if response.status_code == 200:
            st.success("Login successful")
        else:
            st.error("Invalid username or password")

# Party selection page
def party_selection_page():
    st.title("Party Selection")
    # Display list of parties fetched from backend
    parties = requests.get("https://your-backend-api/parties").json()
    for party in parties:
        st.write(party['name'])
    # Allow user to select a party

# Voting page
def voting_page():
    st.title("Voting")
    # Display selected party and confirm vote
    if st.button("Vote"):
        # Call backend API to submit vote
        pass

if __name__ == "__main__":
    main()
