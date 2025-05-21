# ShobdoPath Language Helper

**ShobdoPath** is an AI-powered language learning and vocabulary assistant designed to make English word exploration, reading assistance, and language games more interactive and personalized — especially for Bengali learners.

Built with **Streamlit** and powered by **Gemini Pro** (via LangChain), this app can explain English words, simplify text, generate vocabulary games, and much more.

🎬 **Demo:**  
![demo.mp4](https://github.com/debjotyms/shobdopath-language-helper/blob/main/demo.mp4)

## 🚀 Features

### Word Explorer
Explore words in detail:
- Synonyms & Antonyms
- Bangla translation
- IPA pronunciation
- Definitions, Examples, Etymology, Part of Speech

### Language Games
Make learning fun with:
- Word Association
- Vocabulary Builder (with difficulty levels)
- Anagram Solver

### Reading Assistant
Paste any English paragraph and:
- Simplify the language
- Highlight key vocabulary
- Generate summaries

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

3. **Setup API keys**
   * Create a `.env` file with your [Google Gemini API Key](https://ai.google.dev/).
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
PRs and issues are welcome! If you have a feature idea or want to translate the app fully into Bangla, feel free to open a pull request.

## License
This project is licensed under the MIT License.

## Author
Made with ❤️ by [Debjoty M S](https://debjotyms.com)
