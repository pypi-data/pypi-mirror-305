# TokenProbs

Extract token-level probability scores from generative language models (GLMs) without fine-tuning. Often times, it is relevent to request probability assessment to binary or multi-class outcomes. GLMs are not well-suited for this task. Instead, use `LogitExtractor` to obtain label probabilities without fine-tuning.


## Installation

Install with `pip`:

```bash
conda create -n TokenProbs python=3.11 # Note: not available for 3.13
conda activate TokenProbs
pip3 install TokenProbs 
```

Install via Github Repository:
```bash
conda create -n TokenProbs python=3.12 # Note: not available for 3.13
conda activate TokenProbs

git clone https://github.com/francescoafabozzi/TokenProbs.git
cd TokenProbs
pip3 install -e . # Install in editable mode 
```



## Usage

See `examples/FinancialPhrasebank.ipynb` for an example of using `LogitExtractor` to extract token-level probabilities for a sentiment classification task.

```python
from TokenProbs import LogitExtractor

extractor = LogitExtractor(
    model_name = 'mistralai/Mistral-7B-Instruct-v0.1',
    quantization="8bit" # None = Full precision, "4bit" also suported
)

# Test sentence
sentence = "AAPL shares were up in morning trading, but closed even on the day."

# Prompt sentence
prompt = \
"""Instructions: What is the sentiment of this news article? Select from {positive/neutral/negative}.
\nInput: %text_input
Answer:"""

prompted_sentence = prompt.replace("%text_input",sentence)

# Provide tokens to extract (can be TokenIDs or strings)
pred_tokens = ['positive','neutral','negative']


# Extract normalized token probabilities
probabilities = extractor.logit_extraction(
    input_data = prompted_sentence,
    tokens = pred_tokens,
    batch_size=1
)

print(f"Probabilities: {probabilities}")
Probabilities: {'positive': 0.7, 'neutral': 0.2, 'negative': 0.1}

# Compare to text output
text_output = extractor.text_generation(input_data,batch_size=1)
```

## Trouble Shooting Installation

__Import Errors due to `torch`__

If recieving import errors due to `torch`, specific torch version may be required. Follow the steps below:

__Step 1__:  Identify the CUDA versions (for GPU users):
```bash
nvcc --version
``` 

```bash
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Wed_Nov_22_10:17:15_PST_2023
Cuda compilation tools, release 12.3, V12.3.107
Build cuda_12.3.r12.3/compiler.33567101_0
```

In this case, the CUDA version is 12.3. 

__Step 2__: Navigate to the [Pytorch website](https://pytorch.org/get-started/locally/) and select the version that matches the CUDA version.

There is no cuda version for 12.3, so select torch CUDA download < 12.3 (i.e., 12.1)

__Step 3__: Pip uninstall torch and download with the correct version:
```bash
pip3 uninstall torch
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

__Issues with `bitsandbytes`__

If recieving CUDA Setup failed despite GPU being available. error, identify the location of the cuda driver, typically found under /usr/local/ and input the following commands via the command line. The example below shows this for cuda-12.3.:

```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-12.3 # change 12.3 to appropriate location
export BNB_CUDA_VERSION=123 # 123 (i.e., 12.3) also needs to be changed
```


<!-- 
## Additional Features

`LogitExtractor` also provides functionality for applying Low-rank Adaptation (LoRA) fine-tuning tailored to extracting logit scores for next-token predictions.

Below is an example of fine-tuning Mistral on Financial Phrasebank, a financial sentiment classification dataset.

```python
from datasets import load_dataset
from TokenProbs import LogitExtractor

# Load dataset
dataset = load_dataset("financial_phrasebank",'sentences_50agree')['train']
# Apply training and test split
dataset = dataset.train_test_split(seed=42)
train = dataset['train']

# Convert class labels to text
labels = [{0:'negative',1:'neutral',2:'positive'}[i] for i in train['label']]
# Get sentences 
prompted_sentences = [prompt.replace("%text_input",sent) for sent in train['sentence']]

# Add labels to prompted sentences
training_texts = [prompted_sentences[i] + labels[i] for i in range(len(labels))]

# Load model
extractor = LogitExtractor(
    model_name = 'mistralai/Mistral-7B-Instruct-v0.1',
    quantization="8bit"
)

# Set up SFFTrainer
extractor.trainer_setup(
    train_ds = training_texts, #either a dataloader object or text list
    response_seq = "\nAnswer:", # Tells trainer to train only on text following "\nAnswer: "
    # Input can be text string or list of TokenIDs. Be careful, tokens can differ based on context.
    lora_alpha=16,
    lora_rank=32,
    lora_dropout=0.1
)
extractor.trainer.train()
# Push model to huggingface
extractor.trainer.model.push_to_hub('<HF_USERNAME>/<MODEL_NAME>')

# Load model later
trained_model = extractor(
    model_name = '<HF_USERNAME>/<MODEL_NAME>',
    quantization="8bit"
)
```
-->

<!-- ## Examples -->

<!-- Coming soon. -->



