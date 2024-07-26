# GaLore

Messing around with Galore on Hugging Face.

## Installation and Setup

1. Clone this repository and install the dependencies in your favorite virtual environment.
    
    ```bash
    git clone https://github.com/gil2rok/structured-dl.git
    cd structured-dl
    pip install -r requirements.txt
    ```
2. Sign into Hugging Face Hub with your [User Access Token](https://huggingface.co/docs/hub/security-tokens) generated from your Hugging Face account settings [here](https://huggingface.co/settings).
        
    ```bash
    huggingface-cli login
    ```
        
3. Train Gemma 2B model with GaLore on your GPU(s).
        
    ```bash
    python main.py
    ```

    This may require you to (1) agree to Google's conditions for using Gemma 2B [here](https://huggingface.co/google/gemma-2b) and (2) sign into Weights and Biases.
