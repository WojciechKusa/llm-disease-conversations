LLM disease conversations
==============================

This repository evaluates the consistency of large language models (LLMs) in delivering medical advice, emphasizing their sensitivity to diverse user inputs and beliefs. 
Our analysis uncovers inconsistencies in diagnoses, highlighting the models' variable responses to different symptom descriptions and pre-existing user assumptions.

## Installation

Create a virtual environment and install the requirements:

```zsh
$ conda create -n llm-disease-conversations python=3.8
$ conda activate llm-disease-conversations
(llm-disease-conversations)$ pip install -r requirements.txt
```

Set OpenAI API Key:
Ensure you have an OpenAI API Key. Add your organization and API key as environment variables:

```python
import os
import openai

openai.organization = os.environ['OPENAI_ORGANIZATION']
openai.api_key = os.environ['OPENAI_KEY']
```

## Running the experiment

The code is in the notebook: [`notebooks/NLPMC2023-Clinical-Conversation.ipynb`](notebooks%2FNLPMC2023-Clinical-Conversation.ipynb).

## Data

Generated data is stored in the `data/processed` directory.
Manual evaluations are in the `data/NLPMC-prompt-evaluation.csv` file.

