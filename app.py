"""Experiment 1: text generation using GPT-2."""

from transformers import pipeline, set_seed


def main() -> None:
    generator = pipeline("text-generation", model="gpt2")
    set_seed(42)
    prompt = "Artificial Intelligence will transform the future of"
    outputs = generator(
        prompt,
        max_length=60,
        num_return_sequences=2,
        temperature=0.8,
        top_k=50,
        top_p=0.95,
        do_sample=True,
        pad_token_id=generator.tokenizer.eos_token_id,
    )
    for index, output in enumerate(outputs, 1):
        print(f"--- Generated Text {index} ---")
        print(output["generated_text"], end="\n\n")


if __name__ == "__main__":
    main()

