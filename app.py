import streamlit as st
import sqlite3

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create a new table
def create_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS candidates
                     (id INTEGER PRIMARY KEY, name TEXT, votes INTEGER)''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Function to insert candidates into the table
def insert_candidate(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO candidates (name, votes) VALUES (?, 0)", (name,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Function to get all candidates from the table
def get_candidates(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM candidates")
        return c.fetchall()
    except sqlite3.Error as e:
        print(e)

# Function to update the vote count for a candidate
def update_vote(conn, candidate_id):
    try:
        c = conn.cursor()
        c.execute("UPDATE candidates SET votes = votes + 1 WHERE id = ?", (candidate_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Main function to run the application
def main():
    conn = create_connection("voting.db")
    if conn is not None:
        create_table(conn)

        st.title("Online Voting System")

        # Authentication
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if username == "admin" and password == "admin123":
            st.sidebar.success("Logged in as admin")
            st.sidebar.write("You can add or remove candidates.")
            
            # Add candidate
            new_candidate = st.sidebar.text_input("New Candidate Name")
            if st.sidebar.button("Add Candidate"):
                if new_candidate:
                    insert_candidate(conn, new_candidate)
                    st.sidebar.success(f"Added {new_candidate} as a candidate.")
                    st.sidebar.write("Refresh the page to see the updated list of candidates.")
        
        # Display the list of candidates
        candidates = get_candidates(conn)
        st.write("## Candidates:")
        for candidate in candidates:
            st.write(f"- {candidate[1]}")

        # Display the voting form
        vote_choice = st.radio("Select a candidate to vote for:", [candidate[1] for candidate in candidates])

        # Process the vote when the user clicks the "Vote" button
        if st.button("Vote"):
            candidate_id = [candidate[0] for candidate in candidates if candidate[1] == vote_choice][0]
            update_vote(conn, candidate_id)
            st.success("Thank you for voting!")
        
        # Display the current vote count for each candidate
        st.write("## Current Vote Count:")
        for candidate in candidates:
            st.write(f"- {candidate[1]}: {candidate[2]} votes")

if __name__ == "__main__":
    main()
