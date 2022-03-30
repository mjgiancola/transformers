# This script loads our fine-tuned model, evaluates it on our held-out test
# set, and generates pretty-printed output including the input proof, the
# ground truth explanation, and the transformer's output

from transformers import PegasusTokenizer, PegasusForConditionalGeneration
import json

if __name__ == '__main__':
    model = PegasusForConditionalGeneration.from_pretrained('./out')
    tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-xsum')

    texts = [] # Input
    summs = [] # Output

    # Parse jsonlines into lists
    with open('test.json') as fp:
        for line in fp:
            texts.append(json.loads(line)['text'])
            summs.append(json.loads(line)['summary'])

    inputs = tokenizer(texts, return_tensors='pt', padding=True)

    # Generate Summaries
    summary_ids = model.generate(inputs['input_ids'])
    generated = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]


    for i in range(len(generated)):
        print("Input:\n" + texts[i] + "\n")
        print("Human-Generated Output:\n" + summs[i] + "\n")
        print("Machine-Generated Output:\n" + generated[i] + "\n\n")

