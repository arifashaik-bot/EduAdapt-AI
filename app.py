import streamlit as st

# Page settings
st.set_page_config(
    page_title="EduAdapt AI",
    page_icon="🎓",
    layout="centered"
)

# Project title
st.title("🎓 EduAdapt AI")
st.subheader("Smart Learning Assistant")

st.write(
    "Learn the same topic in simple, intermediate, "
    "or technical language."
)

st.info(
    "Choose a topic and learning level to see "
    "an explanation suited to your needs."
)

# Explanations for different topics and levels
lessons = {
    "Artificial Intelligence": {
        "Beginner": (
            "AI means making computers perform tasks "
            "that usually require human intelligence."
        ),
        "Intermediate": (
            "Artificial Intelligence enables machines "
            "to learn, solve problems, and make decisions."
        ),
        "Technical": (
            "Artificial Intelligence uses computational "
            "methods to perform tasks involving learning, "
            "reasoning, perception, and decision-making."
        )
    },

    "Natural Language Processing": {
        "Beginner": (
            "NLP helps computers understand and work "
            "with human languages."
        ),
        "Intermediate": (
            "NLP is a field of AI that processes and "
            "analyzes human language."
        ),
        "Technical": (
            "NLP combines computational linguistics and "
            "machine learning to analyze, interpret, "
            "and generate human language."
        )
    },

    "Cloud Computing": {
        "Beginner": (
            "Cloud computing lets you use internet-based "
            "services to store files and run applications."
        ),
        "Intermediate": (
            "Cloud computing provides computing resources "
            "such as storage and servers over the internet."
        ),
        "Technical": (
            "Cloud computing delivers configurable computing "
            "resources on demand through scalable network "
            "infrastructure."
        )
    },

    "Cybersecurity": {
        "Beginner": (
            "Cybersecurity protects computers and data "
            "from digital attacks."
        ),
        "Intermediate": (
            "Cybersecurity uses tools and practices to "
            "protect systems, networks, and information."
        ),
        "Technical": (
            "Cybersecurity applies security controls and "
            "risk-management techniques to protect the "
            "confidentiality, integrity, and availability "
            "of digital assets."
        )
    },

    "Data Science": {
        "Beginner": (
            "Data science helps us find useful information "
            "from data."
        ),
        "Intermediate": (
            "Data science uses statistics, programming, "
            "and analysis to discover patterns in data."
        ),
        "Technical": (
            "Data science integrates statistical analysis, "
            "computational methods, and domain knowledge "
            "to extract insights from structured and "
            "unstructured data."
        )
    }
}

# Topic selection
topic = st.selectbox(
    "📚 Choose a Topic",
    list(lessons.keys())
)

# Learning level selection
level = st.radio(
    "🎯 Choose Your Learning Level",
    ["Beginner", "Intermediate", "Technical"],
    horizontal=True
)

# Display adapted explanation
if st.button("Explain This Topic", type="primary"):

    st.markdown("---")

    st.subheader(f"📖 {topic}")

    st.success(f"Learning Level: {level}")

    st.write(lessons[topic][level])

    st.caption(
        "The explanation changes according to "
        "the selected learning level."
    )

# Compare all levels
with st.expander("🔍 Compare All Three Levels"):

    for current_level, explanation in lessons[topic].items():

        st.markdown(f"**{current_level}**")

        st.write(explanation)

        st.markdown("---")

# Footer
st.caption("EduAdapt AI | NLP Mini Project")