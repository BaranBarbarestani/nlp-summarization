from transformers import BartForConditionalGeneration, BartTokenizer

class TextSummarizer:
    def __init__(self):
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    def summarize(self, text):
        inputs = self.tokenizer([text], return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = self.model.generate(inputs['input_ids'], max_length=200, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

