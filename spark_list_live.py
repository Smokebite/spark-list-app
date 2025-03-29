
import streamlit as st
import random

st.set_page_config(page_title="The Spark List – Full Test + Real Sparks", layout="centered")
st.title("✨ The Spark List: Full Test Experience")
st.markdown("Let’s discover what lights you up emotionally and hormonally.")

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

driver_scores = {"Explorer": 0, "Lover": 0, "Creator": 0, "Queen": 0}
hormone_scores = {"Adrenaline": 0, "Oxytocin": 0, "Dopamine": 0, "Serotonin": 0}

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

spark_library = {
    "Oxytocin-Lover": [
        "💞 Do a slow dance with your partner or by yourself in candlelight.",
        "📝 Write a love note and hide it for someone to find.",
        "📞 Call someone you miss and say something vulnerable.",
        "💖 Create a mini altar with objects that remind you of love."
    ],
    "Dopamine-Creator": [
        "🎨 Make a mini collage that captures your current mood.",
        "🎧 Create a playlist called 'Spark Me' with music that makes you feel alive.",
        "🕯️ Light a candle and free-write your dreams for 10 minutes.",
        "🧠 Try writing a one-paragraph fantasy story — no rules."
    ],
    "Adrenaline-Explorer": [
        "🌃 Go somewhere you’ve never been — even a different street corner.",
        "⚡ Take 10 bold selfies that show different moods.",
        "🎢 Try something physically thrilling — dancing, sprinting, or a cold shower.",
        "📸 Take one object and photograph it in 5 wild angles."
    ],
    "Serotonin-Queen": [
        "📚 Organize a calming nighttime routine with lavender tea.",
        "🧘‍♀️ Do 3 grounding breaths and a posture check.",
        "🪴 Water your plants and whisper intentions while doing it.",
        "📅 Write down 3 things you did well this week."
    ]
}

if st.button("Reveal My Spark"):
    top_driver = max(driver_scores, key=driver_scores.get)
    top_hormone = max(hormone_scores, key=hormone_scores.get)
    st.markdown("## 🔍 Your Results")
    st.markdown(f"**Excitement Driver:** {top_driver}")
    st.markdown(f"**Primary Hormone:** {top_hormone}")
    key = f"{top_hormone}-{top_driver}"
    sparks = spark_library.get(key, ["✨ Your Spark: Do something today that brings you gentle joy and bold energy."])
    chosen_spark = random.choice(sparks)
    st.markdown("## ✨ Your Personalized Spark")
    st.success(chosen_spark)
    st.markdown("_There are 60+ Sparks in the full version. This is just your beginning._")

with st.expander("🔍 Preview Other Sparks Like These"):
    st.markdown("Here are more Sparks your future self might love:")
    preview = random.sample(sum(spark_library.values(), []), 5)
    for spark in preview:
        st.markdown(f"- {spark}")
