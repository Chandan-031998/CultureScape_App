import streamlit as st
import random

def render():
    st.title("🌱 Sustainable Travel Tips")
    st.markdown("Small steps lead to big change. Travel responsibly and protect our culture and planet.")

    st.markdown("---")

    st.markdown("### 🧭 General Travel Tips")

    travel_tips = [
        "💧 Carry a refillable water bottle to avoid buying plastic bottles.",
        "🚮 Always dispose of waste in designated bins and avoid littering cultural sites.",
        "🚌 Use public transport, walk, or rent bicycles when exploring cities.",
        "📵 Avoid playing loud music or using phones near temples or sacred spots.",
        "📸 Ask permission before photographing people or restricted areas."
    ]

    for tip in travel_tips:
        st.info(tip)

    st.markdown("### 🛏️ Eco-Friendly Stays")

    with st.expander("🏨 Choose certified eco-stays"):
        st.write("Look for accommodations with green certifications like LEED, EarthCheck, or local eco-labels.")

    with st.expander("💡 Conserve electricity and water"):
        st.write("Turn off lights, ACs, and taps when not in use. Avoid daily towel/laundry services.")

    with st.expander("🍴 Eat local and seasonal food"):
        st.write("Reduce carbon footprint by supporting local farmers and traditional cooking.")

    st.markdown("### 🙏 Respect Culture and Community")

    with st.expander("🧵 Wear culturally appropriate attire"):
        st.write("When visiting temples or tribal areas, cover shoulders and legs as a sign of respect.")

    with st.expander("🎁 Buy authentic handicrafts"):
        st.write("Support artisans by purchasing locally made items instead of mass-produced souvenirs.")

    with st.expander("🗣️ Learn a few local words"):
        st.write("Using greetings or thanks in the local language builds connection and respect.")

    st.markdown("---")

    # 🌿 Random Daily Tip
    st.markdown("### 🌿 Today's Sustainability Tip")
    st.success(random.choice(travel_tips))

    st.caption("📌 Sustainable travel is not just a choice — it's a responsibility.")
