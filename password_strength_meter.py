import streamlit as st
import re

st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔐")

st.markdown("""
   <style>
    .stApp {
        background: linear-gradient(135deg, #1a1f3c, #243b55);
        color: white;
    }
    .stTextInput input {
        border: 2px solid #00d4ff;
        background-color: #1e2a47;
        padding: 10px;
        color: white;
        font-size: 18px;
        border-radius: 8px;
    }
    
    .stButton button {
        width: 100%;
        background: linear-gradient(135deg, #00c6ff, #0072ff);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
        transition: 0.3s;
        border: none;
    }

    .stButton button:hover {
        background: linear-gradient(135deg, #0072ff, #00c6ff);
        box-shadow: 0px 0px 10px rgba(0, 198, 255, 0.8);
    }

    .alert {
        padding: 15px;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin: 10px 0px;
    }

    .success {
        background-color: #28a745;
        color: white;
    }

    .error {
        background-color: #dc3545;
        color: white;
    }

    .warning {
        background-color: #ffc107;
        color: black;
    }
   </style>       
""", unsafe_allow_html=True)

st.markdown("<h1>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#ffcc00; text-align: center;'>🔍 Enter Your Password Below To Check Its Security Level</h3>", unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ **Password Should Be At Least 8 Characters Long**")    
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔡 **Include Both Uppercase (A-Z) And Lowercase (a-z) Letters**")    
        
    if re.search(r"\d", password):
        score += 1
    else:    
        feedback.append("🔢 **Include At Least One Number (0-9)**")    
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔣 **Include At Least One Special Character (!@#$%^&*)**")

    if score == 4:
        st.markdown('<div class="alert success">✅ <b>Strong Password! 🔥</b> - Your Password Is Secure 🎉</div>', unsafe_allow_html=True)
    elif score == 3:
        st.markdown('<div class="alert warning">⚠️ <b>Moderate Password!</b> - Consider improving security by adding more features. 🔐</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="alert error">❌ <b>Weak Password! 🚨</b> - Follow The Suggestions Below To Strengthen It.</div>', unsafe_allow_html=True)

    if feedback:
        with st.expander("🔍 **Improve Your Password Here!** ⬇️"):
            for item in feedback:
                st.write(item)    

st.markdown("<h5>🔑 Enter Your Password:</h5>", unsafe_allow_html=True)
password = st.text_input("", type="password", help="💡 Ensure your password is strong.")    

if st.button("🔎 Check Strength"):
    if password:
        check_password_strength(password)        
    else:
        st.markdown('<div class="alert warning">⚠️ <b>Please Enter A Password First! ⌨️</b></div>', unsafe_allow_html=True)
