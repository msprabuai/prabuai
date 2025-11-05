import streamlit as st
st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit demo application.")
name= st.text_input("Enter your name:")
if st.button("hello button"):
    if name:
        st.success(f"Hello, {name}!")
    else:
        st.warning("Please enter your name.")
   

 #  import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Quiz App", page_icon="🧩", layout="centered")

# --- QUIZ DATA ---
quiz_data = [
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML"
    },
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What year was Python first released?",
        "options": ["1989", "1991", "2000", "2010"],
        "answer": "1991"
    },
    {
        "question": "Which library is best for Machine Learning?",
        "options": ["TensorFlow", "Django", "Flask", "Numpy"],
        "answer": "TensorFlow"
    }
]

# --- SESSION STATE INITIALIZATION ---
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "selected" not in st.session_state:
    st.session_state.selected = None
if "completed" not in st.session_state:
    st.session_state.completed = False

# --- FUNCTION TO RESET QUIZ ---
def restart_quiz():
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.selected = None
    st.session_state.completed = False

# --- MAIN APP LOGIC ---
st.title("🧠 Streamlit Quiz App")
st.markdown("Welcome! Test your knowledge with this fun quiz.")

if not st.session_state.completed:
    q = quiz_data[st.session_state.q_index]
    st.subheader(f"Q{st.session_state.q_index + 1}. {q['question']}")
    st.session_state.selected = st.radio("Choose your answer:", q["options"], index=None)

    if st.button("Submit Answer"):
        if st.session_state.selected:
            if st.session_state.selected == q["answer"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! The correct answer is **{q['answer']}**")

            # Go to next question
            if st.session_state.q_index + 1 < len(quiz_data):
                st.session_state.q_index += 1
            else:
                st.session_state.completed = True
        else:
            st.warning("⚠️ Please select an option before submitting.")
else:
    st.success("🎉 Quiz Completed!")
    st.write(f"Your final score: **{st.session_state.score} / {len(quiz_data)}**")

    if st.button("Restart Quiz"):
        restart_quiz()
