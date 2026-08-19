# GEN-AI & LLM Laboratory Experiments

This repository contains runnable Python implementations of all 12 experiments from the **CS4V48 GenAI & LLM Laboratory Manual**.

## Experiments

1. [Text Generation Using Pre-Trained Foundation Models](experiment_01_text_generation/app.py)
2. [Prompt Engineering for Content Generation, Reasoning and Task Automation](experiment_02_prompt_engineering/app.py)
3. [Conversational AI Chatbot Using Transformer-Based Language Models](experiment_03_conversational_chatbot/app.py)
4. [Text Summarization and Question Answering Using Large Language Models](experiment_04_summarization_qa/app.py)
5. [Sentiment Analysis and Document Classification Using Foundation Models](experiment_05_sentiment_classification/app.py)
6. [Retrieval-Augmented Generation Using a Vector Database](experiment_06_rag_vector_database/app.py)
7. [AI-Powered Code Generation and Debugging Assistant](experiment_07_code_assistant/app.py)
8. [Image Generation Using Diffusion Models](experiment_08_diffusion_image_generation/app.py)
9. [Multimodal AI Integrating Text and Image Inputs](experiment_09_multimodal_blip/app.py)
10. [Fine-Tuning a Pre-Trained Language Model for a Domain-Specific Application](experiment_10_fine_tuning/app.py)
11. [AI-Based Text, Image and Audio Content Generation](experiment_11_multimedia_generation/app.py)
12. [Deployment and Evaluation of a Generative AI Application](experiment_12_deployment_evaluation/app.py)

## Setup

Use Python 3.9 or newer:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Run an experiment from the repository root, for example:

```bash
python experiment_01_text_generation/app.py
```

## Runtime notes

- The first run downloads model weights from Hugging Face.
- Experiments 8, 10, and 11 are compute intensive; a CUDA GPU or Google Colab GPU runtime is recommended.
- Experiment 9 downloads its example image from the internet.
- Experiment 12 launches a local Gradio app. Set `GRADIO_SHARE=true` only when you intentionally want a temporary public link.

