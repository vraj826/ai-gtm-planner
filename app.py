import streamlit as st
import google.generativeai as genai
import os


# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AI Go-To-Market Planner",
    layout="centered"
)

# -------------------------
# GEMINI CONFIG
# -------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# -------------------------
# SYSTEM PROMPT (FINAL)
# -------------------------
SYSTEM_PROMPT = """
You are a senior Go-To-Market strategist who has helped early-stage startups acquire their first 50–500 users.

Your mission is to create highly contextual, execution-focused GTM plans for pre-seed startups with limited resources.

Rules:
- Avoid generic startup advice.
- Recommend only channels that fit the given startup context.
- Optimize for speed, learning, and low cost.
- Clearly label assumptions when user data is inferred.
- Rank all recommended channels explicitly.
- If budget is low or zero, justify any paid tool or exclude it entirely.
- Never change or replace the user-provided startup idea.
- If the startup idea is unclear, ask a clarification question.
- Treat validation and revenue as separate phases with different goals.
- Prioritize founder-led sales before paid ads for revenue goals.
- Use paid ads only after early traction or ROI signals.

Output format:
1. Startup Understanding
2. Recommended Channels (Ranked)
3. GTM Experiments
4. Metrics That Matter
5. Key Risks & Assumptions
"""

# -------------------------
# GEMINI MODEL
# -------------------------
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

# -------------------------
# UI
# -------------------------
st.title("🚀 AI Go-To-Market Planner")
st.write("Generate a contextual GTM plan for early-stage startups using Gemini 2.5.")

st.subheader("Startup Details")

startup_idea = st.text_area(
    "Startup Idea",
    placeholder="Describe your startup in 2–3 lines"
)

target_customer = st.selectbox(
    "Target Customer",
    ["B2B", "B2C"]
)

geography = st.text_input(
    "Geography",
    placeholder="India / US / Global"
)

budget = st.text_input(
    "Budget Range",
    placeholder="₹0–₹5,000 / $500–$1000"
)

goal = st.selectbox(
    "Primary Goal",
    ["Validation", "Revenue", "First Users"]
)

# -------------------------
# GENERATE BUTTON
# -------------------------
if st.button("Generate GTM Plan"):
    if not startup_idea.strip():
        st.warning("Please enter a startup idea.")
    else:
        user_prompt = f"""
Startup idea: {startup_idea}
Target customer: {target_customer}
Geography: {geography}
Budget range: {budget}
Primary goal: {goal}

Create a Go-To-Market plan to acquire the first 50–500 users.
"""

        with st.spinner("Thinking like a GTM strategist..."):
            response = model.generate_content(user_prompt)

        st.subheader("📊 Your GTM Plan")
        st.markdown(response.text)
