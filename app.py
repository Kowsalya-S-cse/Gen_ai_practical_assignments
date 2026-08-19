"""Experiment 12: deploy a summarizer with Gradio and evaluate it with ROUGE."""

import os

import evaluate
import gradio as gr
from transformers import pipeline


SUMMARIZER = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize_text(input_text: str) -> str:
    result = SUMMARIZER(input_text, max_length=45, min_length=15, do_sample=False)
    return result[0]["summary_text"]


def evaluate_example() -> None:
    rouge = evaluate.load("rouge")
    scores = rouge.compute(
        predictions=["AI models generate new content such as text and images."],
        references=[
            "Generative AI models can produce new content including text and images."
        ],
    )
    print("ROUGE evaluation scores:", scores)


def main() -> None:
    evaluate_example()
    demo = gr.Interface(
        fn=summarize_text,
        inputs=gr.Textbox(lines=8, label="Enter text to summarize"),
        outputs=gr.Textbox(label="Generated summary"),
        title="GenAI Text Summarizer",
        description="A cloud-deployable Generative AI summarization app.",
    )
    share = os.getenv("GRADIO_SHARE", "false").lower() == "true"
    demo.launch(share=share)


if __name__ == "__main__":
    main()

