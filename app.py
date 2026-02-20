import streamlit as st
from openai import OpenAI

# 1. Setup
st.set_page_config(page_title="Ramins LLM Council", page_icon="🏛️")
st.title("🏛️ Ramins Executive LLM Council")

# Connect to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"],
)

user_query = st.text_area("Ask the Council a complex question:", height=150)

if st.button("Consult the Council"):
    if not user_query:
        st.warning("Please enter a question first!")
    else:
        # These are the most stable 2026 IDs
        experts = {
            "Expert 1 (The Logician)": "anthropic/claude-3-haiku",
            "Expert 2 (The Data King)": "google/gemini-2.0-flash-001",
            "Expert 3 (The Strategist)": "meta-llama/llama-3.1-8b-instruct"
        }

        answers = {}

        # STEP 1: Consulting the Experts with a Safety Blanket
        for name, model_id in experts.items():
            with st.status(f"Consulting {name}...") as status:
                try:
                    response = client.chat.completions.create(
                        model=model_id,
                        messages=[{"role": "user", "content": user_query}]
                    )
                    answers[name] = response.choices[0].message.content
                    status.update(label=f"✅ {name} Finished!", state="complete")
                except Exception as e:
                    answers[name] = f"Error: This expert was unavailable (Details: {str(e)})"
                    status.update(label=f"❌ {name} Failed", state="error")

        # STEP 2: The Manager Summary
        st.subheader("🏁 Final Council Recommendation")
        
        manager_prompt = f"Summarize these views:\n\n" + "\n".join([f"{n}: {a}" for n, a in answers.items()])
        
        try:
            final_verdict = client.chat.completions.create(
                model="anthropic/claude-3-haiku",
                messages=[{"role": "user", "content": manager_prompt}]
            )
            st.markdown(final_verdict.choices[0].message.content)
        except:
            st.error("The Manager is currently offline. Please see individual expert notes below.")

        # Show detailed notes
        with st.expander("View individual expert reasoning"):
            for name, text in answers.items():
                st.write(f"**{name}**")
                st.info(text)

# THE PANIC BUTTON (Outside the main 'if' so it always shows!)
st.divider()
if st.button("🔄 Clear & Retry Council Meeting"):
    st.rerun()
