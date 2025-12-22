# core/command_router.py
def route_command(text):
    text = text.lower()

    if "youtube" in text:
        from web_automation.youtube import open_youtube
        return open_youtube(text)

    elif "volume" in text:
        from system_control.volume import change_volume
        return change_volume(text)

    else:
        return "Sorry, I didn't understand."


