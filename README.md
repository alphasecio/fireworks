# fireworks-ai
[Fireworks AI](https://fireworks.ai) is a platform for hosting and running machine learning (ML) models with a cloud API, without having to manage your own infrastructure. Sign up for an account at Fireworks and get an [API key](https://fireworks.ai/settings/users/api-keys), which you'll need for this project. 

This repository showcases a simple Streamlit app for running the following open-source text and image generation models on Fireworks AI:
* Text: Meta Llama 3.3 70B Instruct
* Text: Google Gemma 3 27B Instruct *(currently unavailable in serverless mode)*
* Text: OpenAI gpt-oss 20B
* Text: Mixtral MoE 8x7B Instruct
* Text: DeepSeek V3.1
* Text: Qwen3 30B-A3B
* Image: Stable Diffusion XL

![fireworks-sdxl](./fireworks-sdxl.png)

For a detailed guide, see [this](https://alphasec.io/running-open-source-generative-ai-models-on-fireworks-ai/) post. To deploy on [Railway](https://railway.app/?referralCode=alphasec) using a one-click template, click the button below.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/dYYPjx?referralCode=alphasec)
