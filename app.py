import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyBpR7OR9deTipX_eYteGqPcvjoPkG0KHJg")

sys_prompt = """ You are an AI Code Reviewer specializing in Python. Users will submit Python code, and you are expected to analyze it for potential bugs, errors, or areas of improvement. Provide detailed explanations of identified issues and suggest fixes with corrected code snippets. Ensure that your feedback is clear, accurate, and actionable.
If a user submits code in a language other than Python, politely inform them that the tool only supports Python code review.Always conclude with a helpful statement:
'If you need further clarification or have additional queries, feel free to drop an email at varshithm138@gmail.com """

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("An AI Code Reviewer")

user_input = st.text_area(label="Enter your pyhton code here...", placeholder="Explain the concept of for loops")

btn_click = st.button("Generate ")

if btn_click == True:
    response = gemini_model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)
