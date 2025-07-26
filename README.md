# 🔄 Content Multiplier Agent — Repurpose with Local Ollama

*Turn one piece of content into five formats using a locally running Ollama LLM.*

---

## 🌍 Project Description

The Content Multiplier Agent allows creators to quickly transform any long-form content (blog, article, or transcript) into:

* A short summary
* A tweet thread
* A LinkedIn post
* An Instagram caption
* An email newsletter draft

It uses **Gradio** for UI and **Ollama** to run models like `llama3` locally — no internet or API key required.

---

## 📁 Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [License](#license)

---

## ✨ Features

| Feature                | Details                                         |
| ---------------------- | ----------------------------------------------- |
| 🔄 Multi-Format Output | Summary, Tweets, LinkedIn, Instagram, Email     |
| 🧠 Local LLM Powered   | Uses Ollama with `llama3` — no API key required |
| 📦 Lightweight         | Only requires Gradio for UI                     |
| 💻 PyCharm Ready       | Compatible with Python 3.13                     |
| 🖼️ Gradio Interface   | Easy-to-use textbox-based UI                    |

---

## 🚀 Installation

### 1. Install Ollama (if not installed)

Follow the guide at [https://ollama.com/download](https://ollama.com/download) to install and run Ollama on your machine.

### 2. Clone the repository

```bash
git clone https://github.com/yourname/content-multiplier-agent.git
cd content-multiplier-agent
```

### 3. Create a virtual environment

```bash
python3.13 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 4. Install required packages

```bash
pip install gradio
```

---

## 💻 Usage

Make sure Ollama is running and the `llama3` model is available.

```bash
ollama run llama3
```

Then run the script:

```bash
python app.py
```

You will see a Gradio interface where you can:

* Paste long-form content
* Click "Repurpose Content"
* See outputs formatted into five use cases

---

## 🧠 Prompt Logic

The prompt instructs the model to create multiple content formats from a single source. You can modify the template in the `repurpose_content()` function.

---

## 📂 Project Structure

```
content-multiplier-agent/
├── app.py               # Main script
├── requirements.txt     # packages
└── README.md            # This file
```

---

## 📝 Notes

* Make sure Ollama and the `llama3` model are installed and working
* Tested on Python 3.13 and PyCharm
* All content generation is local (no cloud)

---

## 📜 License

MIT License — Free to use, adapt, and share. No warranties.

---

## 🙌 Acknowledgements

* [Ollama](https://ollama.com/)
* [Gradio](https://gradio.app/)
* [Meta Llama 3](https://ai.meta.com/llama/)