from transformers import pipeline


def model_output(prompt):

    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    generator = pipeline("sentiment-analysis", model=checkpoint)
    response = generator([prompt])[0]

    # return response
    return (
        f"It's a {response['label'].lower()} proposition, rated {response['score']:.2%}"
    )
