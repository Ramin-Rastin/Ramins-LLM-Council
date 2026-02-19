import streamlit as st
from openai import OpenAI

# 1. SETUP: Connect to the AI Hub
# We will put your actual key in a "Secret" box later for safety!
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"],
)

st.set_page_config(page_title="LLM Council", page_icon="🏛️")
st.title("🏛️ The Executive LLM Council")
st.write("This council uses three different AI 'Experts' to double-check each other.")

# 2. THE INPUT: What do you want to ask?
user_query = st.text_area("Ask the Council a complex question:", placeholder="e.g., What are the risks of this data strategy?")

if st.button("Consult the Council"):
    if not user_query:
        st.warning("Please enter a question first!")
    else:
        # These are our three expert models for 2026
        experts = {
            "Expert 1 (The Logician)": "anthropic/claude-3.5-sonnet",
            "Expert 2 (The Data King)": "google/gemini-2.0-flash-exp:free",
            "Expert 3 (The Strategist)": "meta-llama/llama-3.3-70b-instruct"
        }
        
        answers = {}
        
        # STEP 1: All Experts think independently
        for name, model_id in experts.items():
            with st.status(f"Consulting {name}...", expanded=False):
                response = client.chat.completions.create(
                    model=model_id,
                    messages=[{"role": "user", "content": user_query}]
                )
                answers[name] = response.choices[0].message.content
                st.write("✅ Response received.")

        # STEP 2: The Final Review (Consensus)
        st.divider()
        with st.spinner("Council Manager is summarizing the final verdict..."):
            manager_prompt = f"""
            Compare these 3 expert answers to the question: '{user_query}'
            
            Expert 1: {answers['Expert 1 (The Logician)']}
            Expert 2: {answers['Expert 2 (The Data King)']}
            Expert 3: {answers['Expert 3 (The Strategist)']}
            
            Identify any contradictions. Then, provide one final, authoritative 'Executive Summary' that combines their best points.
            """
            
            final_verdict = client.chat.completions.create(
                model="anthropic/claude-3.5-sonnet",
                messages=[{"role": "user", "content": manager_prompt}]
            )
            
            st.subheader("🏁 Final Council Recommendation")
            st.markdown(final_verdict.choices[0].message.content)
            
            # Show individual notes in case you want to see the details
            with st.expander("View individual expert reasoning"):
                for name, text in answers.items():
                    st.write(f"**{name}**")
                    st.info(text)
