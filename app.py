import streamlit as st
from groq import Groq

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

MODEL_NAME = "openai/gpt-oss-120b"

client = Groq(api_key=GROQ_API_KEY)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎓",
    layout="wide"
)


# ==========================================
# HEADER
# ==========================================

st.title("🎓 AI Learning Roadmap Generator")

st.write(
    "Create a personalized learning roadmap based on "
    "your field, skill level, and available learning time."
)


# ==========================================
# USER INPUTS
# ==========================================

domain = st.text_input(
    "📚 Domain / Field",
    placeholder="Example: Machine Learning"
)

level = st.selectbox(
    "📊 Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

duration = st.selectbox(
    "⏱️ Available Learning Time",
    [
        "1 Week",
        "2 Weeks",
        "1 Month",
        "2 Months",
        "3 Months",
        "6 Months"
    ]
)


# ==========================================
# ROADMAP GENERATION FUNCTION
# ==========================================

def generate_roadmap(domain, level, duration):

    if not domain or not domain.strip():
        return "⚠️ Please enter a domain or field."

    prompt = f"""
You are an expert learning roadmap designer.

Create a personalized learning roadmap for the user.

USER INFORMATION:

Domain / Field: {domain}
Skill Level: {level}
Available Learning Time: {duration}

Create a practical and realistic roadmap.

The roadmap must include:

## 1. Learning Goal

Explain what the learner will achieve.

## 2. Prerequisites

List the knowledge required before starting.

## 3. Learning Roadmap

Organize the topics in the correct learning order.

## 4. Weekly Learning Plan

Create a chronological plan that fits the available time.

## 5. Practical Exercises

Give hands-on exercises for the learner.

## 6. Tools and Technologies

List important tools and technologies.

## 7. Projects

Suggest practical projects appropriate for the learner's skill level.

## 8. Final Project

Give one meaningful final project that combines the skills learned.

## 9. Expected Skills

Explain what the learner should be able to do after completing the roadmap.

SKILL LEVEL RULES:

Beginner:
Start from fundamentals and assume little prior knowledge.

Intermediate:
Assume the learner understands the fundamentals and focus on practical
and intermediate concepts.

Advanced:
Focus on advanced concepts, architecture, optimization,
real-world applications, and complex projects.

TIME RULE:

The roadmap must realistically fit within the available learning time.

FORMATTING:

Use clear Markdown headings, numbered sections, bullet points,
and concise explanations.
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert educational curriculum designer."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error generating roadmap: {str(e)}"


# ==========================================
# GENERATE BUTTON
# ==========================================

if st.button("🚀 Generate My Roadmap", type="primary"):

    with st.spinner("🤖 Creating your personalized roadmap..."):
        roadmap = generate_roadmap(domain, level, duration)

    st.markdown("---")
    st.subheader("📚 Your Learning Roadmap")
    st.markdown(roadmap)
