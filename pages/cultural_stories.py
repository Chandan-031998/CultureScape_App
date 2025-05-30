import streamlit as st

def render():
    st.title("📚 Cultural Stories of India")
    st.markdown("Enrich your journey with timeless stories of India's art, traditions, and cultural legacy.")

    st.markdown("---")

    st.markdown("### 💃 Traditional Dance Forms")

    with st.expander("🕺 Kathak – Northern India"):
        st.image("https://www.hercircle.in/hcm/EngageImage/5F0D2024-9AB9-41B4-A03A-24D43C9A7E1A/D/CD3A279E-915B-4DBA-9FED-CAFA0DD4C469.jpg", use_column_width=True)
        st.write("""
        Kathak is a storytelling dance form that originated in the temples of North India.
        Dancers use intricate footwork, spins, and facial expressions to narrate mythological tales.
        """)

    with st.expander("💃 Bharatanatyam – Tamil Nadu"):
        st.image("https://shreesangamudhra.com/wp-content/uploads/2022/09/young-dancer-classical-indian-dance-dressed-traditional-suit-is-demonstrating-one-pose-copy-1024x685.jpg", use_column_width=True)
        st.write("""
        One of the oldest classical dance forms, Bharatanatyam is known for its precise movements,
        devotional themes, and expressive gestures based on Hindu spiritual ideas.
        """)

    st.markdown("### 🏛️ Architectural Marvels")

    with st.expander("🌞 Konark Sun Temple – Odisha"):
        st.image("https://www.savaari.com/blog/wp-content/uploads/2022/11/Konark-Sun-Temple-Ancient.webp", use_column_width=True)
        st.write("""
        Built in the 13th century, this chariot-shaped temple dedicated to the Sun God is known for its intricate carvings and astronomical alignment.
        """)

    with st.expander("🕌 Qutub Minar – Delhi"):
        st.image("https://cdn-ijnhp.nitrocdn.com/pywIAllcUPgoWDXtkiXtBgvTOSromKIg/assets/images/optimized/rev-5794eaa/www.jaypeehotels.com/blog/wp-content/uploads/2023/11/Blog-5.jpg", use_column_width=True)
        st.write("""
        This 73-meter tall minaret built in 1193 is a fine example of Indo-Islamic architecture and a UNESCO World Heritage Site.
        """)

    st.markdown("### 🍛 Culinary Heritage")

    with st.expander("🥘 Biryani – A Pan-Indian Delicacy"):
        st.image("https://bestdubaibrunch.com/wp-content/uploads/2023/11/1_New-Menu-grouped-dishes_1.jpg", use_column_width=True)
        st.write("""
        Biryani blends Persian spices and Mughal cooking methods with Indian ingredients. Variants like Hyderabadi, Lucknowi, and Kolkata biryani are culturally significant.
        """)

    with st.expander("🍲 Kerala Sadya – A Vegetarian Feast"):
        st.image("https://cas.indica.in/wp-content/uploads/2022/09/iStock-838927480-683x394.jpg", use_column_width=True)
        st.write("""
        Served on banana leaves, Sadya is a festive meal comprising over 20 dishes, served during Onam and temple festivals.
        """)

    st.markdown("### 🎉 Festivals and Celebrations")

    with st.expander("🪔 Diwali – Festival of Lights"):
        st.image("https://boutindia.s3.us-east-2.amazonaws.com/images/blog/images/2023-07-21-13-56-07-64ba411f1b660-Diwali--Festival-of-light-min.jpg", use_column_width=True)
        st.write("""
        Diwali marks the victory of light over darkness. Families light diyas, burst fireworks, and worship Goddess Lakshmi for prosperity.
        """)

    with st.expander("🎊 Durga Puja – West Bengal"):
        st.image("https://www.setmytrip.in/wp-content/uploads/2023/09/Beautiful-interior-of-decorated-Durga-Puja-pandal-at-Kolkata-West-Bengal-India.-Durga-Puja-is-biggest-religious-festival-of-Hinduism-scaled.jpg", use_column_width=True)
        st.write("""
        A vibrant celebration honoring Goddess Durga, known for massive artistic pandals and cultural performances across Kolkata and Bengal.
        """)

    st.markdown("---")
    st.markdown("📌 More stories coming soon — dive into India’s heritage with each click!")
