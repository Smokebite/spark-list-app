
import streamlit as st

st.set_page_config(page_title="The Spark List – Full Test", layout="centered")
st.title("✨ The Spark List: Full Test Experience")
st.markdown("Let’s discover what lights you up emotionally and hormonally.")

# Question bank
questions = [
    ("You feel most alive when you...", [
        "Try something you've never done before",
        "Have deep emotional conversations",
        "Create or design something meaningful",
        "Organize or lead something important"
    ]),
    ("You're happiest when...", [
        "You're traveling or exploring",
        "You're hugging or bonding with someone",
        "You're making art, writing, or building something",
        "You're mentoring or supporting others"
    ]),
    ("Your ideal Saturday looks like...", [
        "A spontaneous road trip",
        "Cuddling and watching movies",
        "Tinkering with a project",
        "Planning for the week ahead"
    ]),
    ("When you're stressed, you tend to...", [
        "Get impulsive or do something bold",
        "Reach out to someone close",
        "Focus intensely on a task or distraction",
        "Withdraw and reflect silently"
    ]),
    ("What usually soothes you?", [
        "Something exciting and distracting",
        "A deep talk or loving hug",
        "Finishing a task or cleaning up",
        "Silence, nature, or journaling"
    ]),
    ("Which feels most rewarding?", [
        "Adventure or thrills",
        "Love and connection",
        "Getting things done",
        "Peace and stability"
    ]),
    ("Which hobby appeals to you most?", [
        "Skydiving, dance, or martial arts",
        "Spending time with loved ones",
        "Painting, writing, or coding",
        "Gardening or planning"
    ]),
    ("Which word feels most like home?", [
        "Adventure",
        "Intimacy",
        "Creativity",
        "Wisdom"
    ])
]

# Initialize scores
driver_scores = {"Explorer": 0, "Lover": 0, "Creator": 0, "Queen": 0}
hormone_scores = {"Adrenaline": 0, "Oxytocin": 0, "Dopamine": 0, "Serotonin": 0}

# Show questions
for i, (q, options) in enumerate(questions):
    answer = st.radio(f"{i+1}. {q}", options, key=f"q{i}")
    if answer == options[0]:
        driver_scores["Explorer"] += 1
        hormone_scores["Adrenaline"] += 1
    elif answer == options[1]:
        driver_scores["Lover"] += 1
        hormone_scores["Oxytocin"] += 1
    elif answer == options[2]:
        driver_scores["Creator"] += 1
        hormone_scores["Dopamine"] += 1
    elif answer == options[3]:
        driver_scores["Queen"] += 1
        hormone_scores["Serotonin"] += 1

if st.button("Reveal My Spark"):
    top_driver = max(driver_scores, key=driver_scores.get)
    top_hormone = max(hormone_scores, key=hormone_scores.get)

    st.markdown("## 🔍 Your Results")
    st.markdown(f"**Excitement Driver:** {top_driver}")
    st.markdown(f"**Primary Hormone:** {top_hormone}")

    spark_library = {
        "Oxytocin-Lover": "💞 Call someone you love and share something you're grateful for.",
        "Dopamine-Creator": "🎨 Start a small creative ritual, like 10 minutes of journaling with music.",
        "Adrenaline-Explorer": "🧭 Take a walk in a direction you've never gone before.",
        "Serotonin-Queen": "📚 Create a calming evening ritual with tea, a book, and candlelight."
    }

    key = f"{top_hormone}-{top_driver}"
    spark = spark_library.get(key, "✨ Your spark: Do one thing today that brings you both comfort and excitement.")

    st.markdown("## ✨ Your Spark")
    st.success(spark)
    st.markdown("_There are 60+ Sparks in the full version. This is just your beginning._")
