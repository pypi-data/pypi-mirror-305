import peft
from transformers import AutoTokenizer

def get_peft_model(model,lora):
    return peft.get_peft_model(model = model, peft_config = lora)


def get_peft_from_adapters(model,adapters_path :str):
    return peft.PeftModel.from_pretrained(model, adapters_path,
                                    #  torch_dtype=torch.float16,
                                    #  is_trainable=False
                                     )

def get_tokenizer(tokenizer_path: str):
    return AutoTokenizer.from_pretrained(tokenizer_path)


def print_trainable_parameters(peft_model):
    peft_model.print_trainable_parameters()
    
