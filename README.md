<div align="center">

 ◈ ORBIT

 VOICE • AUTOMATION • PYTHON

*A lightweight voice-controlled personal assistant built with Python.*

<br>

<img src="https://img.shields.io/badge/PYTHON-0D0D0D?style=for-the-badge&logo=python&logoColor=9FE3C1" />
<img src="https://img.shields.io/badge/SPEECH%20RECOGNITION-0D0D0D?style=for-the-badge&logoColor=C77D8A" />
<img src="https://img.shields.io/badge/TEXT%20TO%20SPEECH-0D0D0D?style=for-the-badge&logoColor=9FE3C1" />

<br><br>

</div>

---

 ◈ OVERVIEW

**ORBIT** is a simple voice-controlled personal assistant written in Python.

It listens for spoken commands through a microphone, converts speech into text, performs predefined actions, and responds using text-to-speech.

The project combines several Python capabilities into one small interactive system:

`VOICE INPUT` → `COMMAND RECOGNITION` → `ACTION` → `VOICE RESPONSE`

---

 ◈ FEATURES

 🎙️ Voice Commands

ORBIT continuously listens through the system microphone and processes spoken commands using speech recognition.

 🔊 Voice Responses

Responses are spoken aloud using `pyttsx3`.

 🕒 Time & Date

Ask ORBIT for:

- Current time
- Current date

 🌐 Website Access

ORBIT can open:

- YouTube
- Google

directly through voice commands.

 🎵 Music Playback

ORBIT can search a configured folder for `.mp3` files and randomly select a song to play.

 🛑 Voice Shutdown

Say `stop` to end the assistant session.

 ❓ Unknown Command Handling

If ORBIT cannot match a spoken command, it provides a voice response instead of silently failing.

---

 ◈ COMMANDS

| Voice Command | Action |
|---|---|
| `hello` | ORBIT responds with a greeting |
| `time` | Announces the current time |
| `date` | Announces today's date |
| `open youtube` | Opens YouTube |
| `open google` | Opens Google |
| `play music` | Randomly plays an MP3 file |
| `stop` | Shuts down ORBIT |

---

 ◈ HOW IT WORKS

```text
             🎙️
        MICROPHONE INPUT
               │
               ▼
      SPEECH RECOGNITION
               │
               ▼
        COMMAND PARSING
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
      TIME   WEBSITE   MUSIC
       │       │        │
       └───────┼────────┘
               ▼
          ACTION RESULT
               │
               ▼
        TEXT-TO-SPEECH
               │
               ▼
              🔊
            RESPONSE
```

---

 ◈ TECHNOLOGY

 LANGUAGE

`Python`

### SPEECH RECOGNITION

`SpeechRecognition` · `Google Speech Recognition`

 TEXT TO SPEECH

`pyttsx3`

 SYSTEM / AUTOMATION

`webbrowser` · `os` · `datetime` · `random`

---

 ◈ PROJECT STRUCTURE

```text
ORBIT/
│
├── orbit.py
└── README.md
```

> If your main Python file has a different name, replace `orbit.py` with the actual filename.

---

# ◈ SETUP

 1. Clone the repository

```bash
git clone https://github.com/Harsh-Dev19/ORBIT.git
cd ORBIT
```

 2. Install dependencies

```bash
pip install pyttsx3 SpeechRecognition
```

For microphone input, install PyAudio if required by your system:

```bash
pip install PyAudio
```

 3. Configure your music folder

Open the Python file and find:

```python
music_folder = r"C:\Users\Admin\Downloads"
```

Change it to the folder containing your `.mp3` files.

For example:

```python
music_folder = r"C:\Users\YourName\Music"
```

 4. Run ORBIT

```bash
python orbit.py
```

ORBIT will announce:

```text
ORBIT is online. You can give commands.
```

and begin listening.

---

 ◈ EXAMPLE

```text
You: "Hello"

ORBIT: "Hello! How can I help you?"

You: "What is the time?"

ORBIT: "The time is 06:30 PM"

You: "Open YouTube"

ORBIT: "Opening YouTube"

You: "Play music"

ORBIT: "Playing music"

You: "Stop"

ORBIT: "Goodbye. ORBIT shutting down."
```

---

 ◈ PROJECT HIGHLIGHTS

- Microphone-based voice interaction
- Speech-to-text command processing
- Text-to-speech responses
- Browser automation
- Local music playback
- Continuous command loop
- Configurable music directory
- Lightweight Python implementation

---

 ◈ CURRENT SCOPE

ORBIT currently works through a predefined command system.

It does **not** use a large language model or generative AI for interpreting commands.

The project is intentionally lightweight and focuses on building a functional voice-assistant foundation using Python libraries and system-level capabilities.

---

 ◈ FUTURE DIRECTIONS

Possible extensions include:

- More voice commands
- Application launching
- Custom command handling
- Better error handling
- Configurable command modules
- More advanced natural-language understanding
- Additional system automation

---

<div align="center">

 ◈ ORBIT

**LISTEN → UNDERSTAND → ACT → RESPOND**

<br>

`PYTHON` · `VOICE` · `AUTOMATION`

<br><br>

*Harsh Dev*

</div>
