import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    # Strength Rules
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one **uppercase letter (A-Z)**.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one **lowercase letter (a-z)**.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one **number (0-9)**.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("❌ Use at least one **special character (@, #, !, etc.)**.")

    # Strength Levels
    if strength == 1 or strength == 2:
        remarks = "Weak 😞"
        color = "red"
    elif strength == 3 or strength == 4:
        remarks = "Moderate 🙂"
        color = "orange"
    else:
        remarks = "Strong 💪"
        color = "green"

    return strength, remarks, color, feedback

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter by Bilal", page_icon="🔐")
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password",
                         placeholder="e.g., P@ssw0rd123",
                         help="🔹 Use at least 8 characters with uppercase, lowercase, numbers, and symbols."
                        )

if password:
    strength, remarks, color, feedback = check_password_strength(password)

    # Progress bar (out of 5)
    st.progress(strength / 5)

    # Strength remark with color
    st.markdown(f"**Password Strength: <span style='color:{color}; font-size:20px;'>{remarks}</span>**", unsafe_allow_html=True)

    # Show improvement suggestions
    if strength < 5:
        st.warning("⚠️ Improve your password:")
        for tip in feedback:
            st.markdown(f"- {tip}")

    # Password Tips
    st.subheader("✅ Best Practices for Strong Passwords:")
    st.markdown("""
    - **Use at least 12+ characters.**
    - **Include uppercase & lowercase letters.**
    - **Use numbers (0-9).**
    - **Add special symbols (@, #, !, etc.).**
    - **Avoid common words ('password123', 'qwerty', etc.).**
    """)

# Footer with Social Links and Name
st.markdown("""
    <hr>
    <div style="text-align: center;">
        <p><strong>Developed by: Muhammad Bilal Hussain</strong></p>
        <p>
            <a href="https://www.linkedin.com/in/bilalcode01/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30">
            </a>
            &nbsp;&nbsp;
            <a href="https://github.com/Bilal0335" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30">
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)
