import streamlit as st
import openai
import os
from openai import OpenAI;

token = os.environ["GITHUB_TOKEN"];
endpoint = "https://models.github.ai/inference";
modelName = "openai/gpt-4o-mini";

client = OpenAI( base_url=endpoint, api_key=token );

# Title of the application
st.title("Joke Explainer")

# Text input for the user to enter a joke
joke_input = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke_input:
        # Call the OpenAI API to get the explanation
        try:
            # response = openai.ChatCompletion.create(
            #     model="gpt-4o-m-ni",
            #     messages=[
            #         {"role": "user", "content": f"Explain this joke: {joke_input}"}
            #     ]
            # )

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": f"Explain this joke: {joke_input}"}
                ],
            )


            explanation = response.choices[0].message.content
            # Display the explanation
            st.subheader("Explanation")
            st.write(explanation)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a joke before submitting.")
