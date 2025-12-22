# AI-voice-agent

```
voice_agent/
│
├── main.py                     # Entry point
├── config/
│   ├── settings.py             # API keys, paths
│   ├── permissions.json        # Security rules
│
├── core/
│   ├── listener.py             # Microphone input
│   ├── stt.py                  # Speech → Text
│   ├── tts.py                  # Text → Speech
│   ├── wake_word.py            # Wake word detection
│   ├── command_router.py       # Command classification
│
├── system_control/
│   ├── volume.py
│   ├── brightness.py
│   ├── power.py
│   ├── screenshot.py
│
├── file_manager/
│   ├── file_ops.py
│   ├── folder_ops.py
│
├── web_automation/
│   ├── browser.py
│   ├── youtube.py
│   ├── google.py
│   ├── email.py
│
├── coding_assistant/
│   ├── code_generator.py
│   ├── code_debugger.py
│   ├── code_explainer.py
│
├── productivity/
│   ├── reminder.py
│   ├── todo.py
│   ├── scheduler.py
│
├── ai_brain/
│   ├── llm_client.py
│   ├── intent_parser.py
│
├── security/
│   ├── auth.py
│   ├── confirmation.py
│
├── ui/
│   ├── gui.py                  # PyQt / Tkinter
│
├── utils/
│   ├── logger.py
│   ├── helpers.py
│
├── requirements.txt
└── README.md
```