
import streamlit as st
import random

# --- Setup ---
st.set_page_config(page_title="The Spark List – Free Trial", layout="centered")

# --- Welcome Screen ---
st.title("✨ Welcome to The Spark List ✨")
st.subheader("Your feel-good spark engine, based on your emotions and hormones.")
st.markdown("Let’s find out what lights you up. This free trial includes a short test and one personalized Spark just for you.")

# --- Test Questions ---
st.markdown("## Quick Test: What Excites You?")
driver_q = st.radio(
    "When you feel most alive, it’s usually because you’re…",
    [
        "Exploring something new (Explorer, Adrenaline)",
        "Feeling deeply connected to someone (Lover, Oxytocin)",
        "Creating something beautiful (Creator, Dopamine)",
        "Leading or organizing something meaningful (Queen, Serotonin)"
    ]
)

hormone_q = st.radio(
    "Under stress, you usually…",
    [
        "Crave connection and comfort (Oxytocin)",
        "Push through and act quickly (Adrenaline)",
        "Focus and complete a task (Dopamine)",
        "Withdraw to reflect (Serotonin)"
    ]
)

# --- Result Logic ---
if st.button("Reveal My Spark"):
    # Tag scoring
    hormone_map = {
        "Oxytocin": 0,
        "Dopamine": 0,
        "Serotonin": 0,
        "Adrenaline": 0
    }

    driver_map = {
        "Lover": 0,
        "Explorer": 0,
        "Creator": 0,
        "Queen": 0
    }

    # Score driver_q
    if "Lover" in driver_q:
        driver_map["Lover"] += 1
        hormone_map["Oxytocin"] += 1
    elif "Explorer" in driver_q:
        driver_map["Explorer"] += 1
        hormone_map["Adrenaline"] += 1
    elif "Creator" in driver_q:
        driver_map["Creator"] += 1
        hormone_map["Dopamine"] += 1
    elif "Queen" in driver_q:
        driver_map["Queen"] += 1
        hormone_map["Serotonin"] += 1

    # Score hormone_q
    if "Oxytocin" in hormone_q:
        hormone_map["Oxytocin"] += 1
    elif "Adrenaline" in hormone_q:
        hormone_map["Adrenaline"] += 1
    elif "Dopamine" in hormone_q:
        hormone_map["Dopamine"] += 1
    elif "Serotonin" in hormone_q:
        hormone_map["Serotonin"] += 1

    top_hormone = max(hormone_map, key=hormone_map.get)
    top_driver = max(driver_map, key=driver_map.get)

    st.markdown(f"### 🔬 Your Top Hormone: **{top_hormone}**")
    st.markdown(f"### 💖 Your Excitement Driver: **{top_driver}**")

    # Sample Sparks for demonstration
    spark_library = {
        "Oxytocin-Lover": "🌸 Cuddle up with a cozy playlist and text someone you adore.",
        "Dopamine-Creator": "🎨 Make a 5-minute mood collage using images or colors.",
        "Serotonin-Queen": "📋 Organize one small area of your home to feel in control.",
        "Adrenaline-Explorer": "🗺️ Take a spontaneous walk or try a new snack from a culture you’ve never explored."
    }

    key = f"{top_hormone}-{top_driver}"
    spark = spark_library.get(key, "✨ Do something spontaneous that blends comfort and adventure.")

    st.markdown("## Your Personalized Spark")
    st.success(spark)
    st.markdown("_There are 60+ Sparks in the full version. This is just the beginning._")
    st.markdown("❤️ Ready to feel like yourself again? Stay tuned for full access soon.")
