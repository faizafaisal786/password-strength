import streamlit as st
import re
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Password length is good (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️ Password length is acceptable (8-11 characters)")
    else:
        feedback.append("❌ Password is too short (less than 8 characters)")
    
    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")
    
    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
    
    # Numbers check
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Missing numbers")
    
    # Special characters check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Missing special characters")
    
    # Common patterns check
    common_patterns = ['123', 'abc', 'password', 'qwerty']
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 1
        feedback.append("✅ No common patterns detected")
    else:
        feedback.append("❌ Contains common patterns")
    
    return score, feedback

def get_strength_level(score):
    if score >= 6:
        return "Very Strong", "🟢"
    elif score >= 4:
        return "Strong", "🟡"
    elif score >= 2:
        return "Medium", "🟠"
    else:
        return "Weak", "🔴"

def main():
    st.set_page_config(
        page_title="Password Strength Meter",
        page_icon="🔒",
        layout="centered"
    )
    
    st.title("🔒 Password Strength Meter")
    st.write("Check how strong your password is!")
    
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        score, feedback = check_password_strength(password)
        strength_level, color = get_strength_level(score)
        
        st.subheader(f"Password Strength: {color} {strength_level}")
        
        # Display progress bar
        progress = score / 7  # Maximum possible score is 7
        st.progress(progress)
        
        # Display feedback
        st.subheader("Detailed Analysis:")
        for item in feedback:
            st.write(item)
        
        # Additional tips
        st.subheader("Tips for a Strong Password:")
        st.write("1. Use at least 12 characters")
        st.write("2. Include a mix of uppercase and lowercase letters")
        st.write("3. Add numbers and special characters")
        st.write("4. Avoid common words and patterns")
        st.write("5. Don't use personal information")
    
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")

if __name__ == "__main__":
    main() 