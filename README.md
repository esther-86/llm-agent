# Getting Started

Follow these steps to set up the `browser-use` project:

## 1. Install `uv` (a fast Python package manager)
```sh
brew install uv
```

## 2. Create a virtual environment with Python 3.11
```sh
uv venv --python 3.11
```

## 3. Activate the virtual environment
```sh
source .venv/bin/activate
```

## 4. Install `browser-use` in your virtual environment
```sh
uv pip install browser-use
```

## 5. Install the required browser (Chromium) for Playwright
```sh
uv run playwright install
```

You are now set up to use the `browser-use` package as shown in the [official quickstart](https://github.com/browser-use/browser-use#quick-start).

https://github.com/microsoft/vscode-python/wiki/Activate-Environments-in-Terminal-Using-Environment-Variables

```sh
pip3 install -r requirements.txt
```

---

Add your API keys to a `.env` file if you plan to use LLMs (OpenAI, DeepSeek, etc.).

---

