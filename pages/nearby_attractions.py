import streamlit as st
import pandas as pd
import requests
import pydeck as pdk

# 🔐 Google Maps API Key – store securely
GOOGLE_API_KEY = "AIzaSyA-6Ht_I7ufmiR6U5vPslMTxsTKuRo5DEE"  # Replace with your key

# 🌐 Static cultural site list (replace with dynamic from DB if needed)
cultural_sites = {
    "Taj Mahal": {"state": "Uttar Pradesh", "lat": 27.1751, "lon": 78.0421},
    "Konark Sun Temple": {"state": "Odisha", "lat": 19.8876, "lon": 86.0945},
    "Kathakali Center": {"state": "Kerala", "lat": 9.9312, "lon": 76.2673}
}

# Map friendly names to Google Places API types
type_map = {
    "Temple": "hindu_temple",
    "Museum": "museum",
    "Food": "restaurant",
    "Garden": "park",
    "Fort": "tourist_attraction",
    "Nature": "natural_feature",
    "Art Gallery": "art_gallery"
}

def fetch_nearby_places(lat, lon, radius, types):
    results = []
    for place_type in types:
        url = (
            f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
            f"location={lat},{lon}&radius={radius}&type={place_type}&key={GOOGLE_API_KEY}"
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for place in data.get("results", []):
                results.append({
                    "name": place.get("name"),
                    "lat": place["geometry"]["location"]["lat"],
                    "lon": place["geometry"]["location"]["lng"],
                    "type": place_type.replace("_", " ").title(),
                    "address": place.get("vicinity", "")
                })
    return results

def render():
    st.title("🗺️ Nearby Attractions")
    st.markdown("Find nearby places around popular cultural sites using real-time Google Maps data.")

    selected_site = st.selectbox("🛕 Select a Cultural Site", list(cultural_sites.keys()))
    site_info = cultural_sites[selected_site]

    selected_types = st.multiselect(
        "Filter by Attraction Type",
        options=list(type_map.keys()),
        default=["Food", "Temple", "Museum"]
    )

    radius = st.slider("📏 Radius (in meters)", min_value=500, max_value=5000, step=500, value=3000)

    st.markdown("---")

    if selected_types:
        st.info(f"📍 Exploring around {selected_site} in {site_info['state']}")

        with st.spinner("🔎 Searching nearby attractions..."):
            places = fetch_nearby_places(
                site_info["lat"], site_info["lon"], radius, [type_map[t] for t in selected_types]
            )

        if places:
            st.success(f"✅ Found {len(places)} nearby places!")

            # List of places
            for p in places[:10]:  # limit to 10 for performance
                with st.expander(f"📍 {p['name']}"):
                    st.write(f"📂 Type: {p['type']}")
                    st.write(f"📌 Address: {p['address']}")
                    st.markdown(f"[🗺️ View on Google Maps](https://www.google.com/maps/search/?api=1&query={p['lat']},{p['lon']})")

            # Interactive Map
            st.markdown("### 🗺️ Map View")
            map_df = pd.DataFrame(places)
            map_df = pd.concat([
                pd.DataFrame([{"name": selected_site, "lat": site_info["lat"], "lon": site_info["lon"]}]),
                map_df
            ])

            layer = pdk.Layer(
                "ScatterplotLayer",
                data=map_df,
                get_position='[lon, lat]',
                get_radius=80,
                get_fill_color='[0, 128, 255, 160]',
                pickable=True
            )

            view_state = pdk.ViewState(
                latitude=site_info["lat"],
                longitude=site_info["lon"],
                zoom=13,
                pitch=40
            )

            st.pydeck_chart(pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state=view_state,
                layers=[layer],
                tooltip={"text": "{name}"}
            ))

        else:
            st.warning("No places found for selected filters.")
    else:
        st.info("🎯 Select at least one category to begin.")
