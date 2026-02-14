import os
import streamlit as st
import fireworks.client
from fireworks.client.image import ImageInference, Answer

# Streamlit app config
st.set_page_config(page_title="Fireworks Studio", page_icon="🔥", layout="centered")

with st.sidebar:
  st.title("🔥 Fireworks Studio")
  with st.expander("⚙️ Settings", expanded=True):
    fireworks_api_key = st.text_input("Fireworks API key", type="password", help="Get your key [here](https://fireworks.ai/settings/users/api-keys)")
    option = st.radio("Serverless model", [
      "📝 Kimi K2.5",
      "📝 MiniMax-M2.5",
      "📝 OpenAI gpt-oss 20B",
      "📝 Mixtral MoE 8x22B Instruct",
      "📝 Deepseek v3.2",
      "📝 GLM-5",
      "📷 Stable Diffusion XL"]
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
        
        if option == "📝 Kimi K2.5":
          # Run kimi-k2p5 model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/kimi-k2p5",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "📝 MiniMax-M2.5":
          # Run minimax-m2p5 model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/minimax-m2p5",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "📝 OpenAI gpt-oss 20B":
          # Run gpt-oss-20b model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/gpt-oss-20b",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "📝 Mixtral MoE 8x22B Instruct":
          # Run mixtral-8x22b-instruct model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/mixtral-8x22b-instruct",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "📝 Deepseek v3.2":
          # Run deepseek-v3p2 model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/deepseek-v3p2",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "📝 GLM-5":
          # Run glm-5 model on Fireworks AI
          response = fireworks.client.ChatCompletion.create(
              model="accounts/fireworks/models/glm-5",
              messages=[{
                  "role": "user",
                  "content": prompt,
              }],
          )
          st.success(response.choices[0].message.content)
        elif option == "📷 Stable Diffusion XL":
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
