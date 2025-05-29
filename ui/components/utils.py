from wcwidth import wcswidth


UI_WIDTH = 40

def center_text(text):
    text_width = wcswidth(text)
    if text_width >= UI_WIDTH:
        return text
    padding = (UI_WIDTH - text_width) // 2
    return ' ' * padding + text

def get_divider(char='='):
    return char * UI_WIDTH


