# import streamlit as st
# import openai
# import matplotlib.pyplot as plt
# import datetime

# # App title
# st.title("📊 Emotional Analyzer & Trend Visualizer")

# # Sidebar for API key input (won’t store it)
# api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

# if api_key:
#     openai.api_key = api_key

#     history = []

#     def analyze(input_text, model="gpt-4-turbo"):
#         prompt = f"""
#         You are a highly insightful, friendly assistant. Analyze the text below and respond with:
#         1. A brief summary.
#         2. Tone (friendly, formal, angry, hopeful, etc.)
#         3. Sentiment (positive, neutral, negative)
#         4. Emotional intensity (scale 1-10)
#         5. Detect any rhetorical devices (metaphor, irony, hyperbole, etc.)
#         6. Is there humor? (Yes/No, and describe if yes)
#         7. Any kind, constructive suggestions.

#         Text:
#         \"\"\"{input_text}\"\"\"
#         """

#         from openai import OpenAI
#         client = OpenAI(api_key=api_key)

#         response = client.chat.completions.create(
#             model=model,
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7
#         )

#         result = response['choices'][0]['message']['content']

#         # Extract emotional intensity
#         intensity_line = [line for line in result.split("\n") if "Emotional intensity" in line]
#         intensity = int(intensity_line[0].split(":")[1].strip()) if intensity_line else 5

#         history.append({
#             "time": datetime.datetime.now(),
#             "text": input_text,
#             "intensity": intensity
#         })

#         return result

#     def plot_emotional_trends():
#         if not history:
#             st.write("No data yet!")
#             return

#         times = [entry["time"] for entry in history]
#         intensities = [entry["intensity"] for entry in history]

#         fig, ax = plt.subplots(figsize=(8, 4))
#         ax.plot(times, intensities, marker='o', linestyle='-', color='mediumslateblue')
#         ax.set_title("Emotional Intensity Over Time")
#         ax.set_xlabel("Time")
#         ax.set_ylabel("Emotional Intensity (1-10)")
#         ax.set_ylim(0, 10)
#         ax.grid(True)

#         st.pyplot(fig)

#     # Input text box
#     input_text = st.text_area("Enter text to analyze:", height=150)

#     if st.button("Analyze"):
#         if input_text.strip() == "":
#             st.warning("Please enter some text!")
#         else:
#             with st.spinner("Analyzing..."):
#                 result = analyze(input_text)
#                 st.subheader("🔍 Analysis Result")
#                 st.text(result)

#     if st.button("Show Emotional Trend"):
#         plot_emotional_trends()

# else:
#     st.info("Please enter your OpenAI API key in the sidebar to get started.")











import streamlit as st
import requests
import matplotlib.pyplot as plt
import datetime

# App title
st.title("📊 Emotional Analyzer & Trend Visualizer")

history = []

def analyze(input_text, model="text-davinci-002-render-sha"):
    prompt = f"""
    You are a highly insightful, friendly assistant. Analyze the text below and respond with:
    1. A brief summary.
    2. Tone (friendly, formal, angry, hopeful, etc.)
    3. Sentiment (positive, neutral, negative)
    4. Emotional intensity (scale 1-10)
    5. Detect any rhetorical devices (metaphor, irony, hyperbole, etc.)
    6. Is there humor? (Yes/No, and describe if yes)
    7. Any kind, constructive suggestions.

    Text:
    \"\"\"{input_text}\"\"\"
    """
    
    try:
        # Using a free API proxy
        response = requests.post(
            "https://api.pawan.krd/v1/chat/completions",
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            },
            headers={"Authorization": "Bearer pk-this-is-a-real-free-api-key-pk-for-everyone"}
        )
        
        result = response.json()['choices'][0]['message']['content']

        # Extract emotional intensity
        intensity_line = [line for line in result.split("\n") if "Emotional intensity" in line]
        intensity = int(intensity_line[0].split(":")[1].strip()) if intensity_line else 5

        history.append({
            "time": datetime.datetime.now(),
            "text": input_text,
            "intensity": intensity
        })

        return result
        
    except Exception as e:
        return f"Error analyzing text: {str(e)}"

# Rest of your existing code (plot_emotional_trends, input_text, buttons, etc.)
def plot_emotional_trends():
    if not history:
        st.write("No data yet!")
        return

    times = [entry["time"] for entry in history]
    intensities = [entry["intensity"] for entry in history]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(times, intensities, marker='o', linestyle='-', color='mediumslateblue')
    ax.set_title("Emotional Intensity Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Emotional Intensity (1-10)")
    ax.set_ylim(0, 10)
    ax.grid(True)

    st.pyplot(fig)

# Input text box
input_text = st.text_area("Enter text to analyze:", height=150)
    
    if st.button("Analyze"):
        if input_text.strip() == "":
            st.warning("Please enter some text!")
        else:
            with st.spinner("Analyzing..."):
                result = analyze(input_text)
                st.subheader("🔍 Analysis Result")
                st.text(result)

    if st.button("Show Emotional Trend"):
        plot_emotional_trends()

    else:
        st.info("Please enter your OpenAI API key in the sidebar to get started.")
