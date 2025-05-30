import streamlit as st
import os
import uuid
from datetime import date
from utils import execute_query

# Folder to store uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def render():
    st.title("📄 Upload Cultural Documents")
    st.markdown("Upload brochures, cultural policies, event posters, or any related material.")

    uploaded_file = st.file_uploader("📤 Upload a File (PDF, JPG, PNG)", type=["pdf", "jpg", "png"])

    doc_title = st.text_input("📝 Document Title")
    doc_description = st.text_area("💬 Document Description", max_chars=300)

    if uploaded_file and doc_title:
        # Generate unique filename
        filename = f"{uuid.uuid4()}_{uploaded_file.name}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # Save locally
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("✅ Save Document"):
            doc_id = str(uuid.uuid4())
            admin_id = st.session_state.user_id
            upload_date = date.today()

            insert_query = """
                INSERT INTO DOCUMENTS_UPLOAD (
                    document_id, admin_id, title, description, file_url, upload_date
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """
            params = (doc_id, admin_id, doc_title, doc_description, file_path, upload_date)
            execute_query(insert_query, params)
            st.success("🎉 Document uploaded successfully!")

    elif not uploaded_file and st.button("✅ Save Document"):
        st.warning("⚠️ Please select a file to upload.")

    st.markdown("---")
    st.markdown("### 📚 Recently Uploaded Documents")

    fetch_query = """
        SELECT title, description, file_url, upload_date
        FROM DOCUMENTS_UPLOAD
        ORDER BY upload_date DESC
        LIMIT 10
    """
    docs = execute_query(fetch_query, fetch_all=True)

    if docs:
        for doc in docs:
            with st.expander(f"📄 {doc[0]} — {doc[3]}"):
                st.write(f"📝 {doc[1]}")
                if os.path.exists(doc[2]):
                    st.markdown(f"[🔗 Open Document]({doc[2]})")
                else:
                    st.warning("⚠️ File not found on disk.")
    else:
        st.info("📭 No documents uploaded yet.")
