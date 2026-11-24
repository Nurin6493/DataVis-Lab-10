
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Lab 10 | Framing the Data Story",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# 2. DATA PREPARATION
# ==================================================

skills = [
    "Data storytelling",
    "Python",
    "Chart selection",
    "Color and labels",
    "Data cleaning"
]

# Changed Python rating from 3.0 to 2.8
ratings = [2.4, 2.8, 3.2, 3.7, 4.1]

df = pd.DataFrame({
    "Skill": skills,
    "Average rating": ratings
})

# Identify lowest-rated skill automatically
lowest_index = df["Average rating"].idxmin()
lowest_skill = df.loc[lowest_index, "Skill"]
lowest_rating = df.loc[lowest_index, "Average rating"]

# ==================================================
# 3. AUDIENCE CONFIGURATION
# ==================================================

audience_options = {
    "Students": {
        "title": "Students Need More Support in Data storytelling",
        "subtitle": "Understanding students' data visualization skills",
        "purpose": (
            "Help students identify which data visualization "
            "skill they should improve."
        ),
        "takeaway": (
            f"{lowest_skill} received the lowest average "
            f"self-rating of {lowest_rating:.1f} out of 5. "
            "Students should focus on improving this skill."
        )
    },

    "Workshop Instructor": {
        "title": "Prioritize Data Storytelling in the Next Workshop",
        "subtitle": "Identifying the skills that need more teaching support",
        "purpose": (
            "Help workshop instructors identify which topics "
            "require more teaching time and practical exercises."
        ),
        "takeaway": (
            f"{lowest_skill} has the lowest average rating "
            f"of {lowest_rating:.1f} out of 5. "
            "Allocate additional workshop time to this skill."
        )
    },

    "Department Manager": {
        "title": "Invest in Improving Data Visualization Skills",
        "subtitle": "Using student feedback to guide training decisions",
        "purpose": (
            "Help department managers identify training gaps "
            "and prioritize resources for staff or student development."
        ),
        "takeaway": (
            f"{lowest_skill} has the lowest average rating "
            f"of {lowest_rating:.1f} out of 5. "
            "Consider providing additional training and resources "
            "to strengthen this area."
        )
    }
}

# ==================================================
# 4. SIDEBAR - DASHBOARD SETTINGS
# ==================================================

st.sidebar.title("Dashboard Settings")

st.sidebar.write("Select target audience")

selected_audience = st.sidebar.selectbox(
    "Target Audience",
    options=list(audience_options.keys()),
    label_visibility="collapsed"
)

# Get selected audience content
content = audience_options[selected_audience]

st.sidebar.markdown("---")

st.sidebar.caption(
    "Lab 10 | TFB3133 / TEB3133"
)

st.sidebar.write("**Data Visualization Skills**")

st.sidebar.caption(
    "Fictional practice data for audience-focused storytelling."
)

# ==================================================
# 5. MAIN DASHBOARD HEADER
# ==================================================

st.title("Framing the Data Story")

st.caption(content["subtitle"])

st.markdown("---")

# ==================================================
# 6. AUDIENCE-FOCUSED STORY
# ==================================================

st.header(content["title"])

st.markdown(
    f"**Audience:** {selected_audience}"
)

st.markdown(
    f"**Purpose:** {content['purpose']}"
)

# Key takeaway box
st.info(
    f"**Key takeaway:** {content['takeaway']}"
)

# ==================================================
# 7. CREATE THE HORIZONTAL BAR CHART
# ==================================================

fig, ax = plt.subplots(figsize=(10, 5))

# Highlight the lowest-rated skill in orange
bar_colors = [
    "#E07A3F" if i == lowest_index else "#4C78A8"
    for i in range(len(skills))
]

bars = ax.barh(
    df["Skill"],
    df["Average rating"],
    color=bar_colors,
    height=0.65
)

# ==================================================
# 8. CHART FORMATTING
# ==================================================

ax.set_xlim(0, 5)

ax.set_xticks(range(0, 6))

ax.set_xlabel(
    "Average self-rating (1 = Beginner, 5 = Confident)",
    fontsize=11,
    labelpad=12
)

ax.set_title(
    f"{lowest_skill} received the lowest average rating",
    fontsize=14,
    pad=15
)

# Display first category at the top
ax.invert_yaxis()

# Add subtle gridlines
ax.grid(
    axis="x",
    color="#DDDDDD",
    linewidth=0.7
)

ax.set_axisbelow(True)

# Remove unnecessary borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# White chart background
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Dark chart text
ax.tick_params(axis="both", colors="#222222")
ax.xaxis.label.set_color("#222222")
ax.yaxis.label.set_color("#222222")
ax.title.set_color("#222222")

# ==================================================
# 9. ADD VALUE LABELS
# ==================================================

for bar, value in zip(bars, ratings):

    ax.text(
        value + 0.05,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}",
        va="center",
        fontsize=11,
        color="#222222"
    )

fig.tight_layout()

# ==================================================
# 10. DISPLAY CHART
# ==================================================

st.pyplot(fig, use_container_width=True)

plt.close(fig)

# ==================================================
# 11. EXPLANATION OF THE GRAPH
# ==================================================

with st.expander("Understanding the Visualization"):

    st.write(
        "**Category axis:** Lists the five data visualization skills."
    )

    st.write(
        "**Numeric axis:** Shows average self-ratings "
        "on a scale of 0 to 5."
    )

    st.write(
        "**Bar lengths:** Represent the average rating "
        "for each skill, not individual student responses."
    )

    st.write(
        f"**Highlighted bar:** {lowest_skill} is highlighted "
        "in orange because it has the lowest average rating."
    )

# ==================================================
# 12. CLASSMATE FEEDBACK
# ==================================================

st.markdown("---")

st.header("Audience Understanding and Feedback")

st.write(
    "Show this visualization to a classmate without "
    "explaining the takeaway. Record their feedback below."
)

with st.form("feedback_form"):

    understood = st.text_area(
        "1. What did your classmate understand?",
        placeholder="Example: They understood that orange represents the lowest-rated skill."
    )

    unclear = st.text_area(
        "2. What was unclear?",
        placeholder="Example: They were unsure whether the values represented averages or individual responses."
    )

    improvement = st.text_area(
        "3. What change did you make after receiving feedback?",
        placeholder="Describe the change you made to improve the visualization."
    )

    submitted = st.form_submit_button("Submit Feedback")

    if submitted:

        if understood and unclear and improvement:

            st.success("Feedback submitted for this session.")

            st.write("**Understood:**", understood)
            st.write("**Unclear:**", unclear)
            st.write("**Improvement:**", improvement)

        else:

            st.warning("Please complete all feedback fields.")

# ==================================================
# 13. SOURCE
# ==================================================

st.markdown("---")

st.caption(
    "Source: Fictional practice values created for "
    "TFB3133/TEB3133 Data Visualization Lab 10. "
    "Ratings represent illustrative average self-ratings "
    "on a scale of 1–5, not findings from a real survey."
)
