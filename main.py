import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import random

# Load environment variables and setup model
load_dotenv()
gemini_chat_model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0)

# App configuration and styling
st.set_page_config(page_title="Shobdopath AI", page_icon="📚")

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
    }
    .subheader {
        font-size: 1.2rem;
        color: #424242;
        margin-bottom: 2rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# App header with creative name
# st.markdown('<p class="main-header">📚 Wordsmith AI</p>', unsafe_allow_html=True)
# st.markdown('<p class="subheader">Your personal linguistic companion</p>', unsafe_allow_html=True)

# Create tabs for different functionalities
tab1, tab2, tab3 = st.tabs(["Word Explorer", "Language Games", "Reading Assistant"])


with tab1:
    st.header('Word Explorer')
    
    col1, col2 = st.columns([3, 1])
    with col1:
        user_input_word = st.text_input("Enter a word to explore:")
    # with col2:
        if st.button("Random Word"):
            common_words = ["serendipity", "eloquent", "ephemeral", "mellifluous", "petrichor", 
                           "luminous", "resilience", "ubiquitous", "sublime", "ethereal"]
            user_input_word = random.choice(common_words)
            st.session_state.random_word = user_input_word
    
    # Show the random word in the text input
    if 'random_word' in st.session_state:
        user_input_word = st.session_state.random_word
    
    selection_option = st.selectbox(
        "What would you like to know?",
        ('Synonym', 'Antonym', 'Bangla Translation', 'IPA Pronunciation', 
         'English Definition', 'Example Sentences', 'Etymology', 'Part of Speech')
    )


    template = load_prompt('word_explorer_prompt.json')

    if user_input_word:
        with st.spinner(f'Retrieving {selection_option.lower()} for "{user_input_word}"...'):
            fullTemplate = template.format(
                input_word=user_input_word,
                input_option=selection_option
            )
            result = gemini_chat_model.invoke(fullTemplate)
            
            # Display result in a styled container
            st.success(result.content)
            
            # Quick access buttons for other options
            st.write("Quick Explore:")
            col1, col2, col3, col4 = st.columns(4)
            quick_options = {
                "Definition": "English Definition",
                "Synonyms": "Synonym", 
                "Examples": "Example Sentences",
                "Etymology": "Etymology"
            }
            
            for col, (label, option) in zip([col1, col2, col3, col4], quick_options.items()):
                if col.button(label) and option != selection_option:
                    with st.spinner(f'Retrieving {option.lower()} for "{user_input_word}"...'):
                        quick_template = template.format(
                            input_word=user_input_word,
                            input_option=option
                        )
                        quick_result = gemini_chat_model.invoke(quick_template)
                        st.info(f"**{option}**: {quick_result.content}")

with tab2:
    st.header("Language Games")
    
    game_options = st.selectbox(
        "Select a game:",
        ["Word Association", "Vocabulary Builder", "Anagram Solver"]
    )
    
    if game_options == "Word Association":
        st.subheader("Word Association Game")
        st.write("Enter a word and see what it makes the AI think of!")
        
        assoc_word = st.text_input("Enter a word for association:")
        if assoc_word:
            prompt = f"""Generate a mind map of 5 words that are strongly associated with '{assoc_word}'. 
            For each associated word, provide a brief explanation of the connection.
            Format: Associated word: explanation"""
            
            with st.spinner("Generating associations..."):
                result = gemini_chat_model.invoke(prompt)
                st.write(result.content)
    
    elif game_options == "Vocabulary Builder":
        st.subheader("Vocabulary Builder")
        difficulty = st.select_slider(
            "Select difficulty level:",
            options=["Easy", "Medium", "Hard", "Advanced"]
        )
        
        if st.button("Generate New Word"):
            prompt = f"""Generate an interesting {difficulty.lower()} level English word that would help expand someone's vocabulary.
            Provide the word, its pronunciation, definition, and one example sentence.
            Format your response in these sections clearly labeled."""
            
            with st.spinner("Finding an interesting word..."):
                result = gemini_chat_model.invoke(prompt)
                st.write(result.content)
    
    elif game_options == "Anagram Solver":
        st.subheader("Anagram Solver")
        letters = st.text_input("Enter letters to rearrange:")
        if letters:
            prompt = f"""Find up to 10 meaningful English words that can be created using some or all of these letters: {letters}
            Sort them from longest to shortest. Only include valid English words."""
            
            with st.spinner("Finding anagrams..."):
                result = gemini_chat_model.invoke(prompt)
                st.write(result.content)

with tab3:
    st.header("Reading Assistant")
    
    text_to_analyze = st.text_area("Paste text to analyze:", height=150)
    
    if text_to_analyze:
        analysis_type = st.radio(
            "What would you like to do with this text?",
            ["Simplify Language", "Identify Key Vocabulary", "Summarize"]
        )
        
        if st.button("Process Text"):
            if analysis_type == "Simplify Language":
                prompt = f"""Rewrite the following text using simpler language while preserving the meaning:
                
                {text_to_analyze}
                
                Make it accessible to someone with basic English proficiency."""
                
            elif analysis_type == "Identify Key Vocabulary":
                prompt = f"""Identify the 5-8 most important vocabulary words from the following text:
                
                {text_to_analyze}
                
                For each word, provide:
                1. The word itself
                2. Its definition as used in this context
                3. A simpler synonym"""
                
            else:  # Summarize
                prompt = f"""Summarize the following text in 2-3 sentences:
                
                {text_to_analyze}"""
            
            with st.spinner("Processing text..."):
                result = gemini_chat_model.invoke(prompt)
                st.write(result.content)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center">
    <p>Made with ❤️ by debjotyms.com</p>
</div>
""", unsafe_allow_html=True)