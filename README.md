# 📝 Text Summarization Using LLM

A lightweight, modular Python project that leverages a local Large Language Model (LLM) via **Ollama** to generate concise, accurate, and context-aware summaries of lengthy texts. Built with a clean system prompt architecture for maximum clarity, brevity, and intent preservation.

---

## 📁 Project Structure

```
text-summarization-using-llm/
├── summarizer.py
└── text_summarizer_model.py
```

- `summarizer.py` → Main execution script containing sample texts and the run loop.
- `text_summarizer_model.py` → Core `TextSummarizer` class that handles LLM communication and prompt engineering.

---

## 🛠️ Prerequisites

1. **Python 3.8+** installed on your system.
2. **Ollama** installed locally: [https://ollama.ai](https://ollama.ai)
3. Pull the default model (or any compatible LLM):
   ```bash
   ollama pull phi3:3.8b
   ```
4. Ensure the Ollama service is running locally (usually starts automatically when you run `ollama run` or `ollama serve`).

---

## ⚙️ Installation & Setup

Follow these steps to create a virtual environment and install dependencies:

```bash
# 1. clone the project
git clone https://github.com/sherrytelli/text-summarization-using-llm.git

# 2. Navigate to the project directory
cd text-summarization-using-llm

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 5. Install required dependencies
pip install ollama
```

> 💡 **Note:** The project only depends on the `ollama` Python client. No heavy ML frameworks (like PyTorch or TensorFlow) are required since inference is handled locally via Ollama.

---

## 🚀 Usage

Once dependencies are installed and Ollama is running, execute the main script:

```bash
python summarizer.py
```

The script will:
1. Load sample texts
2. Pass each through the `TextSummarizer` class
3. Print the original text and its generated summary side-by-side

---

## 📝 Example Input & Output

### 🔹 Input
```text
Education enables individuals to develop the knowledge, skills and confidence needed to participate fully in society. Through teaching and learning, societies pass on essential knowledge, values and competencies across generations. Education builds foundational literacy and numeracy strengthens social and emotional skills and equips people to make informed choices about their lives and their communities.

Education is one of the most powerful tools for lifting excluded children and adults out of poverty and is an enabler of other fundamental human rights. It is a cornerstone of peace, justice, and resilience in the face of today’s most pressing global challenges. It forms the foundation of democratic society, and the right to education is protected under international law. 

To achieve the right to education for all, education must be inclusive, equitable and free from discrimination. UNESCO works closely with Member States and partners to uphold these principles and strengthen education systems worldwide to make sure no learner is left behind. 
```

### 🔹 Output
```text
Education provides essential knowledge for societal participation, builds foundational skills like literacy and numeracy while also fortifying social competencies and informed decision-making abilities. It serves as a powerful instrument in alleviating poverty and promoting fundamental human rights such as freedom of expression or equality before the law. Education is integral to democratic society's foundation, peace, justice, resilience against global challenges like climate change, health crises etc., ensuring inclusivity and non-discrimination in learning environments while upholding international legal standards for education rights through initiatives by UNESCO.
```

---

## 📖 How It Works

1. `TextSummarizer` initializes with a default model (`phi3:3.8b`) and a strictly defined system prompt.
2. The system prompt enforces:
   - Core meaning extraction
   - Significant length reduction (15–25% of original)
   - Neutral tone & no hallucination
   - Clean, direct output without meta-commentary
3. `ollama.chat()` sends the system prompt + user text to the local LLM.
4. The model returns a structured, concise summary that is printed to the console.

---

## 🔧 Customization

- **Switch Models:** Pass your preferred model name directly to the constructor (e.g., `TextSummarizer(model_name="llama3.2:3b")`).
- **Use in Your Projects:** You can either import and use the `TextSummarizer` class in your own codebases, or simply append new texts to the `sample_texts` list in `summarizer.py` for quick local testing.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

✅ *Ready to summarize locally with AI. Happy coding!* 🚀