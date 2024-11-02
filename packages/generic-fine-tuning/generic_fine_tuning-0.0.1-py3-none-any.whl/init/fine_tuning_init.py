from datasets import DatasetDict
from peft import LoraConfig
from transformers import TrainingArguments
from trl import SFTTrainer
import re


def get_layers(model):
    return model.modules


def get_linear_layers(model) -> list[str]:
    
    model_modules = str(model.modules)
    
    pattern = r'\((\w+)\): Linear'
    
    linear_layer_names = re.findall(pattern, model_modules)
    
    names = []
    # return the names of the Linear layers
    for name in linear_layer_names:
        names.append(name)
    target_modules = list(set(names))
    return target_modules


def pick_layers(model,indices: list[int]):
    # freeze --> requires_grad_(False)
    # pick ---> requires_grad_(True) default.
    
    # pattern = r"(model\.layers\.("
    pattern = r".+\.layers\.("
  
    for i in indices:
        pattern += str(i) + r'|'
    
    pattern = pattern[:-1]
    
    pattern += r')\..+'
    
    for name, module in model.named_parameters():
        res = re.findall(pattern, name)
        if len(res) != 1: # doesn't match the regex of picking
            # module.requires_grad = False
            module.requires_grad_(False)
                
                
    
    
def get_lora_config(target_modules: list[str], r: int=8,lora_alpha: int=16,
                    lora_dropout: float=0.05,
                    task_type: str='CAUSAL_LM') -> LoraConfig:
    
    return LoraConfig(
        r=r,
        lora_alpha=lora_alpha,
        lora_dropout=lora_dropout,
        # modules_to_save=["embed_tokens"],
        bias="none",
        # use_dora=True,
        # use_rslora=True,
        # layer_replication=[(0,10),(10,20),(10,20),(20,24)],
        target_modules = target_modules,# list of layers to be trained
        task_type=task_type)


def get_training_args(output_dir: str='./adapters_checkpoints',
                      num_train_epochs: int=100,
                      save_strategy: str='steps',
                      save_steps: int=100,
                      per_device_train_batch_size: int=4,
                      gradient_accumulation_steps: int=4,
                      optim: str='adamw_hf',
                      learning_rate: float=2e-4,
                      use_fp16: bool=True,
                      max_grad_norm: float=0.3,
                      warmup_ratio: float=0.03,
                      group_by_length: bool=True,
                      lr_scheduler_type: str='linear'
                      ) -> TrainingArguments:
    
    return TrainingArguments(
        output_dir=output_dir,
        num_train_epochs = num_train_epochs,
        save_strategy=save_strategy,
        save_steps=save_steps,
        # evaluation_strategy="steps",
        # eval_steps=500,
        # do_eval=True,
        per_device_train_batch_size=per_device_train_batch_size,
        gradient_accumulation_steps=gradient_accumulation_steps,
        optim=optim,
        learning_rate=learning_rate,
        fp16=use_fp16,
        max_grad_norm=max_grad_norm,
        warmup_ratio=warmup_ratio,
        group_by_length=group_by_length,
        lr_scheduler_type=lr_scheduler_type)


def get_sft(model,train_dataset: DatasetDict,dataset_text_field: str='prompt',
            max_seq_length: int=1024,
            args: TrainingArguments=get_training_args()) -> SFTTrainer:
    return SFTTrainer(
        model,
        train_dataset=train_dataset['train'],
        # eval_dataset = dataset['validation'],
        dataset_text_field=dataset_text_field,
        max_seq_length=max_seq_length,
        # save_embedding_layers=True,
        args=args, # the config of the training hyper-params
        )
 
    
def train(trainer,path: str='./adapters',last_checkpoint: str=None):
    if last_checkpoint:
        train_result = trainer.train(last_checkpoint)
    else:
        train_result = trainer.train()
    metrics = train_result.metrics
    trainer.log_metrics("train_metrics_log", metrics)
    trainer.save_metrics("train_metrics", metrics)
    trainer.save_model(path)
    return train_result