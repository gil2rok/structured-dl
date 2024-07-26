import torch
import datasets
import trl

from transformers import TrainingArguments, AutoConfig, AutoTokenizer, AutoModelForCausalLM

train_dataset = datasets.load_dataset('imdb', split='train')

args = TrainingArguments(
    output_dir="./test-galore",
    max_steps=100,
    per_device_train_batch_size=256,
    optim="adamw_8bit",
    optim_target_modules=[r".*.attn.*", r".*.mlp.*"],
    fp16=True,
)

model_id = "google/gemma-2b"

config = AutoConfig.from_pretrained(model_id)
config.hidden_activation = "gelu_pytorch_tanh"  # See https://github.com/huggingface/transformers/pull/29402

tokenizer = AutoTokenizer.from_pretrained(model_id, config=config)
model = AutoModelForCausalLM.from_config(config).to(0)
    
trainer = trl.SFTTrainer(
    model=model, 
    args=args,
    train_dataset=train_dataset,
    dataset_text_field='text',
    max_seq_length=2048,
)

trainer.train()