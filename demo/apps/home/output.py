import torch
from transformers import pipeline
from huggingface_hub import login
from demo.settings import HF_TOKEN

login(token=HF_TOKEN)


def sentiment_classifier(prompt):

    model = "distilbert-base-uncased-finetuned-sst-2-english"
    pipe = pipeline(
        "sentiment-analysis",
        model=model,
    )
    response = pipe([prompt])[0]

    return (
        f"It's a {response['label'].lower()} proposition, rated {response['score']:.2%}"
    )


def text_gen(prompt):

    model = "meta-llama/Llama-3.2-1B-Instruct"
    pipe = pipeline(
        "text-generation",
        model=model,
        torch_dtype=torch.bfloat16,
        device=-1,  # run only cpu
    )
    messages = [
        {"role": "system", "content": prompt},
    ]
    response = pipe(
        messages,
        max_new_tokens=256,
    )[0]

    return response["generated_text"][1]["content"]
