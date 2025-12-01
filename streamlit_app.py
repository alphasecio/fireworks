import os
import streamlit as st
import fireworks.client
from fireworks.client.image import ImageInference, Answer

st.set_page_config(
    page_title="Fireworks Playground",
    page_icon="🎆",
    layout="centered"
)

# Streamlit app
st.subheader("🎆 Fireworks Playground")
with st.sidebar:
  st.subheader("⚙️ Settings")
  fireworks_api_key = st.text_input("Fireworks API key", type="password", help="Get your key [here](https://fireworks.ai/settings/users/api-keys)")
  option = st.selectbox("Select serverless model", [
    "Text: Meta Llama 3.3 70B Instruct",
    "Text: Google Gemma 3 27B Instruct",
    "Text: OpenAI gpt-oss 20B",
    "Text: Mixtral MoE 8x22B Instruct",
    "Text: DeepSeek V3.1",
    "Text: Qwen3 30B-A3B",
    "Image: Stable Diffusion XL"]
    )

col1, col2 = st.columns([4, 1])
prompt = col1.text_input("Prompt", label_visibility="collapsed")
submit = col2.button("Submit")

# If Submit button is clicked
if submit:
  if not fireworks_api_key.strip():
    st.warning("⚠️ Please enter your Fireworks API key in the sidebar.")
  elif not prompt.strip():
    st.warning("⚠️ Please enter a prompt.")
  else:
    try:
      with st.spinner("Please wait..."):
        fireworks.client.api_key = fireworks_api_key
        os.environ["FIREWORKS_API_KEY"] = fireworks_api_key
        
        if option == "Text: Meta Llama 3.3 70B Instruct":
          # Run llama-v3p3-70b-instruct model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/llama-v3p3-70b-instruct",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "Text: Google Gemma 3 27B Instruct":
          # Run gemma-3-27b-it model on Fireworks AI
          #response = fireworks.client.ChatCompletion.create(
          #    model="accounts/fireworks/models/gemma-3-27b-it",
          #    messages=[{
          #        "role": "user",
          #        "content": prompt,
          #    }],
          #)
          #st.success(response.choices[0].message.content)
          st.error("This model is currently unavailable in serverless mode.")
        elif option == "Text: OpenAI gpt-oss 20B":
          # Run gpt-oss-20b model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/gpt-oss-20b",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "Text: Mixtral MoE 8x22B Instruct":
          # Run mixtral-8x22b-instruct model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/mixtral-8x22b-instruct",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "Text: DeepSeek V3.1":
          # Run deepseek-v3 model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/deepseek-v3p1",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "Text: Qwen3 30B-A3B":
          # Run qwen3-30b-a3b model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/qwen3-30b-a3b",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "Image: Stable Diffusion XL":
          # Run stable-diffusion-xl-1024-v1-0 model on Fireworks AI
          client = ImageInference(model="stable-diffusion-xl-1024-v1-0")
          answer : Answer = client.text_to_image(
              prompt=prompt,
              cfg_scale=7,
              height=1024,
              width=1024,
              sampler=None,
              steps=30,
              seed=0,
              safety_check=False,
              output_image_format="PNG"
          )
          st.image(answer.image)
    except Exception as e:
      st.exception(f"Exception: {e}")
