import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

class TextGenerator:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.device = None
        self.model_index = {
            "quble": None,
            "fcp": None
        }

    def loadQuble(self):
        """Load the Quble model and tokenizer."""
        self.model_index["quble"] = GPT2LMHeadModel.from_pretrained("quble-model-name")  # Replace with actual model name
        self.tokenizer = GPT2Tokenizer.from_pretrained("quble-model-name")  # Replace with actual model name
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_index["quble"].to(self.device)
        self.model_index["quble"].eval()
        print("Quble model and tokenizer loaded.")

    def loadFCP(self, huggingface_path: str):
        """Load the FCP model and tokenizer from the given Hugging Face path."""
        self.model_index["fcp"] = GPT2LMHeadModel.from_pretrained(huggingface_path)
        self.tokenizer = GPT2Tokenizer.from_pretrained(huggingface_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_index["fcp"].to(self.device)
        self.model_index["fcp"].eval()
        print(f"FCP model and tokenizer loaded from {huggingface_path}.")

    def useQuble(self, user: str, system: str, chat_template: dict, max_length: int = 50, temperature: float = 1.0, num_return_sequences: int = 1) -> str:
        if self.model_index["quble"] is None:
            raise ValueError("Quble model is not loaded. Call loadQuble() first.")

        # Construct the prompt using the provided chat template
        prompt = (
            f"{chat_template['before_system']} {system} {chat_template['after_system']} "
            f"{chat_template['before_user']} {user} {chat_template['after_user']} "
            f"{chat_template['before_assistant']} "
        )
        
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            generated_ids = self.model_index["quble"].generate(
                input_ids,
                max_length=max_length,
                num_return_sequences=num_return_sequences,
                temperature=temperature
            )

        generated_texts = [self.tokenizer.decode(generated_id, skip_special_tokens=True) for generated_id in generated_ids]
        return generated_texts

    def useFCP(self, user: str, system: str, chat_template: dict, max_length: int = 50, temperature: float = 1.0, num_return_sequences: int = 1) -> str:
        if self.model_index["fcp"] is None:
            raise ValueError("FCP model is not loaded. Call loadFCP() first.")

        # Construct the prompt using the provided chat template
        prompt = (
            f"{chat_template['before_system']} {system} {chat_template['after_system']} "
            f"{chat_template['before_user']} {user} {chat_template['after_user']} "
            f"{chat_template['before_assistant']} "
        )
        
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            generated_ids = self.model_index["fcp"].generate(
                input_ids,
                max_length=max_length,
                num_return_sequences=num_return_sequences,
                temperature=temperature
            )

        generated_texts = [self.tokenizer.decode(generated_id, skip_special_tokens=True) for generated_id in generated_ids]
        return generated_texts

    def eject_model(self):
        """Remove the model and clear resources."""
        self.model = None
        self.tokenizer = None
        self.model_index = {
            "quble": None,
            "fcp": None
        }
        torch.cuda.empty_cache()  # Clear the CUDA cache if using GPU
        print("Models ejected and resources cleared.")
