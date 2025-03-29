
import streamlit as st
import random

st.set_page_config(page_title="The Spark List – Full 22-Question Test", layout="centered")
st.title("✨ The Spark List: Full Test Experience")
st.markdown("Answer honestly — this is your personalized emotional and hormonal Spark map.")

questions = [
    ("You feel most alive when you...", ["Try something new and exciting", "Connect deeply with someone", "Create something beautiful", "Lead or organize something"]),
    ("Your ideal self is...", ["Adventurous and bold", "Loving and kind", "Creative and visionary", "Wise and grounded"]),
    ("Your favorite way to recharge is...", ["Go somewhere spontaneous", "Cuddle or bond", "Do a passion project", "Have quiet, peaceful time"]),
    ("You feel drained when...", ["Life feels too predictable", "You feel emotionally distant", "You can't express yourself", "There's chaos or instability"]),
    ("In a perfect world, you’d spend more time...", ["Exploring the unknown", "Building deep relationships", "Pursuing artistic dreams", "Creating security and peace"]),
    ("When you're in a funk, you need...", ["Stimulation or risk", "A long hug or a good cry", "A creative outlet", "A peaceful plan"]),
    ("Which compliments feels best?", ["You're so brave", "You're so loving", "You're so original", "You're so centered"]),
    ("What type of book or movie draws you in?", ["Thriller or adventure", "Romance or drama", "Fantasy or creative stories", "Philosophy or documentaries"]),
    ("What would you do with 1 free hour?", ["Spontaneous adventure", "Talk with someone close", "Make something meaningful", "Reflect or organize"]),
    ("You’re most inspired by...", ["Overcoming fear", "Acts of love", "Vision and innovation", "Wisdom and legacy"]),
    ("When angry, you usually...", ["Explode or act out", "Withdraw emotionally", "Suppress and distract", "Shut down silently"]),
    ("What’s your greatest fear?", ["Being trapped or bored", "Being alone or unloved", "Being unoriginal", "Losing control or stability"]),
    ("You crave more...", ["Adventure", "Affection", "Expression", "Structure"]),
    ("Which scent draws you in?", ["Campfire or ocean", "Rose or vanilla", "Ink or citrus", "Sandalwood or pine"]),
    ("Your spark dims when...", ["Things feel repetitive", "You feel unloved", "You feel unseen", "You’re overwhelmed"]),
    ("Choose a word that excites you:", ["Wild", "Tender", "Vision", "Balance"]),
    ("Pick a visual scene:", ["Racing down a mountain", "A couple holding hands", "Someone painting alone", "A calm sunrise"]),
    ("Which hormone do you want more of?", ["Adrenaline", "Oxytocin", "Dopamine", "Serotonin"]),
    ("Pick the vibe:", ["Risk + Reward", "Connection + Safety", "Creative + Focused", "Calm + Power"]),
    ("Favorite energy:", ["Fire", "Water", "Air", "Earth"]),
    ("Favorite time of day:", ["Late night", "Twilight", "Sunrise", "Early morning"]),
    ("You light up when...", ["You face fear", "You feel loved", "You get inspired", "You feel grounded"])
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
