# 🚀 AI Go-To-Market Planner

An AI-powered decision assistant that helps early-stage founders acquire their first 50–500 users by generating context-aware, execution-ready Go-To-Market (GTM) strategies based on startup inputs like goal, budget, market, and geography.

# 🧠 Problem Statement

Early-stage founders struggle with:
- Generic, one-size-fits-all GTM advice
- Choosing the right acquisition channels
- Knowing what experiments to run first
- Avoiding wasted time and money

Most existing resources are blog posts or templates that don’t adapt to context.

# 💡 Solution

AI Go-To-Market Planner is a Gemini-powered AI decision assistant that:

- Understands startup context (B2B/B2C, geography, budget, goal)
- Recommends ranked acquisition channels
- Converts strategy into concrete GTM experiments
- Explains why each recommendation is made
- Adapts its reasoning for validation vs revenue goals

This is not a content generator — it is a decision-making assistant for founders.

# ✨ Key Features
## ✅ Context-Aware Strategy Generation

- Adapts output based on:
  - Startup idea
  - Target customer (B2B / B2C)
  - Geography (India / US / Global)
  - Budget constraints
  - Primary goal (Validation, Revenue, First Users)

## ✅ Execution-Ready GTM Plans

Each generated plan includes:
1. Startup Understanding – Clear articulation of the problem, user, and value proposition
2. Recommended Channels (Ranked) – Only context-appropriate channels
3. GTM Experiments – Actionable, step-by-step experiments founders can run immediately
4. Metrics That Matter – Learning and revenue metrics, not vanity metrics
5. Key Risks & Assumptions – Transparent assumptions and risk mitigation strategies

## ✅ Founder-Realistic Recommendations

- Prioritizes founder-led, low-cost experiments
- Avoids paid ads when budget is low or zero
- Separates validation tactics from scaling tactics
- Enforces revenue-first thinking when revenue is the goal

## ✅ Secure & Production-Safe

- No API keys stored in code
- Uses Streamlit Secrets for secure key management
- Includes error handling for quota or API failures

# 🛠️ How It Works

1. User enters startup details via a simple UI
2. Inputs are combined into a structured prompt
3. A hardened system prompt guides Gemini’s reasoning
4. Gemini generates a structured, contextual GTM plan
5. Results are displayed instantly in the app

# 🖥️ Live Demo

## 👉 Live App URL:
https://ai-gtm-planner-bjwsxxf52gpfghyw7iopvh.streamlit.app/

# 📸 Example Use Cases

- B2B SaaS startup validating first users in India
- B2C student app with zero marketing budget
- Global founder targeting revenue via founder-led sales
- Pre-seed startup choosing between LinkedIn vs communities vs ads

# 🧪 Prompt Engineering & AI Governance

- This project was built using Prompt-to-Prototype principles:
- Stress-tested across multiple startup scenarios
- Explicit rules to prevent hallucination or generic advice
- Clear separation between validation and revenue strategies
- Strict adherence to user-provided startup ideas
- Graceful handling of quota and model availability

# 🧩 Tech Stack

- Frontend: Streamlit
- AI Model: Google Gemini (via Generative AI API)
- Backend Logic: Python
- Deployment: Streamlit Cloud
- Secrets Management: Streamlit Secrets

# 📂 Project Structure
```
ai-gtm-planner/
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
├── .gitignore          # Ignored files & secrets
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

# 🚀 Getting Started (Local Setup)
## 1️⃣ Clone the repo
```
git clone https://github.com/vraj826/ai-gtm-planner
cd ai-gtm-planner
```

## 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

## 3️⃣ Set API key (local only)
```
export GEMINI_API_KEY="your_api_key_here"
```

## 4️⃣ Run the app
```
python -m streamlit run app.py
```

# 🔐 Security Notes

- API keys are never committed to the repository
- All secrets are managed securely via environment variables
- Compromised keys are immediately rotated and revoked

# 📈 Future Improvements

- Save GTM plans as downloadable PDFs
- Compare GTM strategies across multiple startup ideas
- Add experiment tracking & iteration history
- Support multiple languages and regions

# 📜 License

This project is licensed under the MIT License.

# 🙌 Acknowledgements

Built as part of Google for Startups – Prompt to Prototype using Gemini.
Special thanks to the open-source and startup communities for inspiration.

# ⭐ If you like this project, consider giving it a star!
