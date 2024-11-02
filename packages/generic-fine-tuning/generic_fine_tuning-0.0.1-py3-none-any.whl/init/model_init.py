from transformers import AutoModelForCausalLM,AutoTokenizer,BitsAndBytesConfig
import torch


def get_quantization_config(type: int=8) -> BitsAndBytesConfig:
    if type == 8:
        return BitsAndBytesConfig(load_in_8bit=True)
    elif type == 4:
        return BitsAndBytesConfig(load_in_4bit=True,
                                  bnb_4bit_quant_type="nf4",
                                  bnb_4bit_use_double_quant=True,
                                  bnb_4bit_compute_dtype=torch.float16)
    else:
        raise Exception('Invalid Quantization type')


def load_model(hf_model_id: str, device_map: str='auto', quantization_config=None):
    if quantization_config:
        return AutoModelForCausalLM.from_pretrained(
            hf_model_id, device_map=device_map,quantization_config=quantization_config,
            trust_remote_code=True)
    else:
        return AutoModelForCausalLM.from_pretrained(
            hf_model_id, device_map=device_map,trust_remote_code=True)
        
def load_tokenizer(hf_model_id: str):
    return AutoTokenizer.from_pretrained(hf_model_id,trust_remote_code=True)