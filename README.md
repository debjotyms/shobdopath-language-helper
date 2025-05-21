# ShobdoPath Language Helper

**ShobdoPath** is a simple tool I built for my personal use to help with learning English words and reading. It is made for Bengali speakers, but anyone can use it. You can also fork this project and change it however you like.

This app uses **Streamlit** for the interface and the **Gemini API** (via LangChain) for AI features.

🎬 **Demo:**  
<img src="demo.gif" alt="ShobdoPath Demo" width="600"/>

## 🚀 Features

### Word Explorer

- Find synonyms and antonyms
- Bangla translation
- IPA pronunciation
- Definitions, examples, etymology, part of speech

### Language Games

- Word Association
- Vocabulary Builder (choose difficulty)
- Anagram Solver

### Reading Assistant

- Paste any English paragraph
- Simplifies the language
- Highlights important words
- Makes summaries

## Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/debjotyms/shobdopath-language-helper.git
   cd shobdopath-language-helper
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**

   - Make a `.env` file with your [Google Gemini API Key](https://ai.google.dev/).
     ```
     GOOGLE_API_KEY=your_google_gemini_api_key
     ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## 📂 File Structure

```
.
├── app.py                    # Main Streamlit app
├── word_explorer_prompt.json # Prompt template for word exploration
├── demo.mp4                  # Demo video
├── .env                      # Environment variables (user-generated)
├── requirements.txt          # Python dependencies
```

## Contributing

Feel free to fork and change this project for your own needs. PRs and issues are welcome!

## License

This project is licensed under the MIT License.

## Author

Made with ❤️ by [Debjoty Mitra](https://debjotyms.com)
