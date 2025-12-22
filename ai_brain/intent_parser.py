def detect_language(text):
    if any(ch in text for ch in "অআইউএ"):
        return "bn"
    return "en"
