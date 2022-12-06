def duplicate_count(text: str) -> int:
    repeating = 0
    new_text = text.lower()
    for i in text.lower():
        if new_text.count(i) > 1:
            repeating += 1
            new_text = new_text.replace(i, '')
    return repeating

