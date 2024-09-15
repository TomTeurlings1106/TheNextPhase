import streamlit as st
import random

# List of funny jokes
jokes = [
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Did you hear about the mathematician who’s afraid of negative numbers? He will stop at nothing to avoid them.",
    "Why don’t scientists trust atoms? Because they make up everything!"
]

# Set the title of the landing page
st.title("Welcome to the World's Funniest Landing Page! 😂")

# Subheading
st.subheader("Where every click is a giggle and every scroll is a chuckle!")

# Display a random joke
st.write("Here's a joke to brighten your day:")
st.write(f"**{random.choice(jokes)}**")

# Add a funny image
st.image(
    "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif", 
    caption="When you realize how awesome this landing page is!",
    use_column_width=True
)

# Button to show another joke
if st.button("Need another laugh? Click me!"):
    st.write(f"**{random.choice(jokes)}**")

# Footer message
st.write("**P.S. If you laughed at least once, our mission is accomplished!** 🎉")
