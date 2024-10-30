# 🚀 Blexus

Welcome to **Blexus**, an AI innovation lab committed to crafting **small, specialized AI models**. Our mission is to unlock the full potential of AI through **task-specific models** that are fast, efficient, and highly customizable—ideal for developers, businesses, and everyday use cases.
[READ MORE](https://huggingface.co/Blexus)

---

## 🛠️ **Installation**

You can install the Blexus package using pip. Run the following command:

```bash
pip install blexus
```

## Use Quble models
```py
from blexus import TextGenerator

# Define the chat template  IMPORTANT: fill in the fields!
chat_template = {
    "before_system": "",
    "after_system": "",
    "before_user": "",
    "after_user": "",
    "before_assistant": ""
}

# Load Quble model
text_generator_quble = TextGenerator()
text_generator_quble.loadQuble()

# Generate text using Quble model
user_input = "Hello, how are you?"
system_input = "You are a helpful assistant."
generated_texts_quble = text_generator_quble.useQuble(user_input, system_input, chat_template, max_length=100, temperature=0.7, num_return_sequences=1)
print("Quble generated texts:", generated_texts_quble)

# Eject Quble model when done
text_generator_quble.eject_model()


# Load FCP model from a Hugging Face path
huggingface_path = "huggingface/fcp-model-name"  # Replace with actual Hugging Face model path
text_generator_fcp = TextGenerator()
text_generator_fcp.loadFCP(huggingface_path)

# Generate text using FCP model
generated_texts_fcp = text_generator_fcp.useFCP(user_input, system_input, chat_template, max_length=100, temperature=0.7, num_return_sequences=1)
print("FCP generated texts:", generated_texts_fcp)

# Eject FCP model when done
text_generator_fcp.eject_model()
```

# More coming soon!