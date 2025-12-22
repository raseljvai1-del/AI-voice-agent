from core.listener import listen
from core.stt import speech_to_text
from core.tts import speak
from core.command_router import route_command
from core.wake_word import wait_for_wake_word
from utils.logger import log_info
from utils.error_handler import handle_error


def main():
    speak("Voice assistant is starting.")

    while True:
        try:
            # 1️⃣ Wake word
            wait_for_wake_word()

            speak("Yes?")

            # 2️⃣ Listen from mic
            audio_path = listen()

            # 3️⃣ Speech → Text
            command = speech_to_text(audio_path)
            log_info(f"User said: {command}")

            if not command:
                speak("I did not hear anything.")
                continue

            # 4️⃣ Exit command
            if "exit" in command.lower() or "stop" in command.lower():
                speak("Goodbye!")
                break

            # 5️⃣ Route command
            response = route_command(command)

            # 6️⃣ Speak response
            speak(response)

        except KeyboardInterrupt:
            speak("Assistant stopped.")
            break

        except Exception as e:
            handle_error(e)
            speak("Something went wrong.")


if __name__ == "__main__":
    main()

