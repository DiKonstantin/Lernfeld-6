# language.py

def load_language(language):
    try:
        module = __import__("brain.languages."+language, globals(), locals(), [''])
        return module.messages
    except ImportError:
        print("Language module '{}' not found.".format(language))
        return {}


_current_language = "en"  # Default language


def switch_language(language):
    global _current_language
    _current_language = language


def get_message(message_id, language=None):
    global _current_language
    if language is None:
        language = _current_language
    messages = load_language(language)
    if message_id in messages:
        return messages[message_id]
    else:
        return f"Message ID '{message_id}' not found for language '{language}'"

def get_question(question_id, language=None):
    global _current_language
    if language is None:
        language = _current_language
        questions = load_language(language)
        if question_id in questions:
            return questions[question_id]
        else:
            return f"Question ID '{question_id}' not found for language '{language}'"
