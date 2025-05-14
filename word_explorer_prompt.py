from langchain_core.prompts import PromptTemplate

# Template with specific instructions
template = PromptTemplate(
    template="""
    You are a comprehensive dictionary assistant. I need information about the word: "{input_word}"
    
    Task: Provide the {input_option} for this word.
        
    If the task is "Synonym": Provide 5 synonyms separated by commas, from most common to most specialized.
    If the task is "Antonym": Provide 5 antonyms separated by commas.
    If the task is "Bangla Translation": Translate the word accurately to Bangla (Bengali).
    If the task is "IPA Pronunciation": Provide the IPA phonetic pronunciation.
    If the task is "English Definition": Provide a clear, concise definition of the word.
    If the task is "Example Sentences": Provide 3 example sentences using the word in different contexts.
    If the task is "Etymology": Provide a brief etymology of the word, explaining its origin.
    If the task is "Part of Speech": Identify the part(s) of speech this word can function as and explain briefly.
     
    Format your response without explanations or additional text - just provide the requested information directly.
    """,
    input_variables=['input_word', 'input_option']
)

template.save('word_explorer_prompt.json')