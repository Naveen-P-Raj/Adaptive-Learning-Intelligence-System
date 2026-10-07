import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import hashlib
import os

# ---------------- CONFIG ----------------
st.set_page_config(page_title="ALIS", layout="wide")

st.title("🧠 Adaptive Learning Intelligence System")

# ---------------- HASH ----------------
def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()

# ---------------- USER DB ----------------
cols = ["username","password","pin","name","class"]

if not os.path.exists("users.csv"):
    pd.DataFrame(columns=cols).to_csv("users.csv", index=False)

users = pd.read_csv("users.csv")

# ---------------- SESSION ----------------
if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- LOGIN SYSTEM ----------------
st.sidebar.title("🔐 Account")
menu = st.sidebar.radio("Menu", ["Login","Register"])

# REGISTER
if menu == "Register":
    st.subheader("Create Account")

    name = st.text_input("Full Name")
    student_class = st.text_input("Class (11/12)")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    new_pin = st.text_input("PIN (4 digits)", type="password")

    if st.button("Register"):
        if new_user in users["username"].values:
            st.error("Username already exists")
        elif len(new_pin) != 4:
            st.error("PIN must be 4 digits")
        else:
            users.loc[len(users)] = [new_user, hash_password(new_pass), new_pin, name, student_class]
            users.to_csv("users.csv", index=False)
            st.success("Account created successfully")

# LOGIN
if menu == "Login":
    st.subheader("Login")

    user = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        match = users[
            (users["username"] == user.strip()) &
            (users["password"] == hash_password(password))
        ]

        if not match.empty:
            st.session_state.user = user
            st.success("Login successful")
        else:
            st.error("Invalid credentials")

# ---------------- MAIN SYSTEM ----------------
if st.session_state.user:

    st.subheader(f"👋 Welcome {st.session_state.user}")

    file = f"{st.session_state.user}_data.csv"

    if not os.path.exists(file):
        pd.DataFrame(columns=["subject","topic","date","score","revision"]).to_csv(file, index=False)

    df = pd.read_csv(file)

    # ---------------- SUBJECT LIST ----------------
    subjects = [
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "English",
        "Hindi",
        "Economics",
        "Business Studies",
        "Accountancy",
        "Political Science",
        "History",
        "Geography",
        "Sociology",
        "Psychology",
        "Physical Education"
    ]

    # ---------------- ADD TOPIC ----------------
    st.markdown("### 📥 Add Study Topic")

    subject = st.selectbox("Select Subject", subjects)
    topic = st.text_input("Topic / Chapter")
    score = st.slider("Score (%)", 0, 100)

    if st.button("Add Topic"):
        new = {
            "subject": subject,
            "topic": topic,
            "date": str(datetime.now().date()),
            "score": score,
            "revision": 1
        }
        df = pd.concat([df, pd.DataFrame([new])])
        df.to_csv(file, index=False)
        st.success("Topic added!")

    # ---------------- PROCESS ----------------
    if len(df) > 0:

        # SIMPLE RETENTION MODEL (NO DAYS)
        df["retention"] = df["score"] * 0.8 + df["revision"] * 5
        df["retention"] = df["retention"].clip(0, 100)

        def get_status(x):
            if x < 40:
                return "🔴 Revise Now"
            elif x < 70:
                return "🟡 Revise Soon"
            else:
                return "🟢 Good"

        df["status"] = df["retention"].apply(get_status)

        # ---------------- ALERTS ----------------
        st.markdown("### 🔔 Alerts")

        urgent = df[df["status"] == "🔴 Revise Now"]

        if len(urgent) > 0:
            st.error(f"{len(urgent)} topics need revision!")
            st.dataframe(urgent[["subject","topic"]])
        else:
            st.success("No urgent revisions!")

        # ---------------- DASHBOARD ----------------
        st.markdown("### 📊 Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("Topics", len(df))
        col2.metric("Avg Score", int(df["score"].mean()))
        col3.metric("Retention", f"{df['retention'].mean():.1f}%")

        # ---------------- RECOMMENDATIONS ----------------
        st.markdown("### 🎯 Recommendations")

        st.dataframe(df[["subject","topic","status"]])

        # ---------------- GRAPH ----------------
        st.markdown("### 📈 Memory Trend")

        st.line_chart(df["retention"])

        # ---------------- SUBJECT ANALYSIS ----------------
        st.markdown("### 📚 Subject Performance")

        st.bar_chart(df.groupby("subject")["score"].mean())

        # ---------------- LOGOUT ----------------
        if st.button("Logout"):
            st.session_state.user = None
            st.rerun()

else:
    st.info("Please login to continue")
