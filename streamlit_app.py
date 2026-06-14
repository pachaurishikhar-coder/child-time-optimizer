import streamlit as st
from pulp import *

st.set_page_config(page_title="Child Time Optimizer")

st.title("🧒 Child Time Optimizer")

st.write("AI + Linear Programming based child routine optimization")


# -----------------------------
# INPUTS
# -----------------------------

child_name = st.text_input("Child Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=18,
    value=7
)

sleep_time = st.slider(
    "Sleep Time (Hours)",
    6,
    12,
    10
)

school_time = st.slider(
    "School Time (Hours)",
    0,
    8,
    4
)

max_screen_time = st.slider(
    "Max Screen Time",
    0,
    5,
    1
)

study_priority = st.slider(
    "Study Priority",
    1,
    10,
    7
)

play_priority = st.slider(
    "Play Priority",
    1,
    10,
    8
)

creativity_priority = st.slider(
    "Creativity Priority",
    1,
    10,
    7
)

spritual_priority = st.slider(
    "Spritual Priority",
    1,
    10,
    6
)

# -----------------------------
# BUTTON
# -----------------------------

if st.button("Generate Optimized Schedule"):

    # LP Problem
    prob = LpProblem(
        "Child_Time_Optimization",
        LpMaximize
    )

    # Variables
    study = LpVariable("Study", lowBound=0)

    play = LpVariable("Play", lowBound=0)

    creativity = LpVariable("Creativity", lowBound=0)

    screen = LpVariable("Screen", lowBound=0)

    sleep = LpVariable("Sleep", lowBound=0)

    school = LpVariable("School", lowBound=0)

    spritual = LpVariable("Spritual", lowBound=0)


    # Objective Function
    prob += (
        study_priority * study
        + play_priority * play
        + creativity_priority * creativity
        + spritual_priority * spritual
        - 2.55 * screen
    )

    # Constraints
    prob += (
        study
        + play
        + creativity
        + screen
        + sleep
        + school
        + spritual
        == 24
    )

    prob += sleep == sleep_time

    prob += school == school_time

    prob += screen <= max_screen_time

    prob += play >= 1

    prob += play <= 4

    prob += study <= 4

    prob += study >= 1

    prob += creativity >= 1

    prob += spritual >= 1

    prob += screen >= 0.25

    # Solve
    prob.solve()

    # Results
    st.success("Optimization Complete!")

    st.subheader("📊 Optimization Score")

    st.write(round(value(prob.objective), 2))

    st.subheader("⏰ Recommended Time Allocation")

    st.write(
        f"📘 Study Hours: {round(value(study), 2)}"
    )

    st.write(
        f"⚽ Play Hours: {round(value(play), 2)}"
    )

    st.write(
        f"🎨 Creativity Hours: {round(value(creativity), 2)}"
    )

    st.write(
        f"📱 Screen Hours: {round(value(screen), 2)}"
    )

    st.write(
        f"😴 Sleep Hours: {round(value(sleep), 2)}"
    )

    st.write(
        f"🙏 Spritual Hours: {round(value(spritual), 2)}"
    )

    st.write(
        f"🏫 School Hours: {round(value(school), 2)}"
    )

    st.subheader("🧠 AI Insight")

    if value(screen) > 2:
        st.warning(
            "Screen exposure is relatively high."
        )

    else:
        st.success(
            "Healthy screen balance detected."
        )

    if value(sleep) < 8:
        st.warning(
            "Sleep duration may be insufficient."
        )

    else:
        st.success(
            "Sleep allocation looks healthy."
        )
