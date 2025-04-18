from transformers import BartForConditionalGeneration, BartTokenizer

class TextSummarizer:
    def __init__(self):
        # Load pre-trained BART model and tokenizer from Hugging Face
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    def summarize(self, text):
        # Encode the text input into token IDs
        inputs = self.tokenizer([text], return_tensors="pt", max_length=1024, truncation=True)

        # Generate summary using the model
        summary_ids = self.model.generate(inputs['input_ids'], max_length=200, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode the summary tokens into readable text
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary
