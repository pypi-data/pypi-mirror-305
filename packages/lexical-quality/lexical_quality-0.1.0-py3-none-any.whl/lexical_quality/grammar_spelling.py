from spellchecker import SpellChecker
import language_tool_python

# Initialize tools
spell = SpellChecker()
tool = language_tool_python.LanguageTool('en-US')

def check_spelling_grammar(text):
    # Check for spelling errors
    words = text.split()
    misspelled = spell.unknown(words)
    spelling_score = 1 - (len(misspelled) / len(words)) if words else 1  # 1 means no spelling errors

    # Check for grammar issues
    grammar_matches = tool.check(text)
    grammar_score = 1 - (len(grammar_matches) / len(words)) if words else 1  # 1 means no grammar errors

    # Average score for grammar and spelling (higher is better)
    return (spelling_score + grammar_score) / 2

