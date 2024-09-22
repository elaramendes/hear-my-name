# Hear-My-Name

This project also has a [Portuguese version](README.pt.md).


**Hear-My-Name** is an application that captures sounds and emits a notification when it detects a person's name. The project uses voice recognition with the **Vosk** library to listen to sounds in real-time and alerts the user when their name is mentioned.

## Features

- Real-time sound capture.
- Voice recognition using **Vosk** to identify the person's name.
- Notification emission when the name is detected.
- Intuitive interface for displaying spoken text.

## Requirements

- **Python 3.9**

## Technologies Used

- **Python**: The main programming language of the project.
- **Libraries**:
  - `Vosk`: For offline speech recognition.
  - `Flet`: For the graphical user interface.
  - `PyAudio`: For real-time audio capture.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/elaramendes/hear-my-name.git
   ```

2. Navigate to the project directory:
   ```bash
   cd hear-my-name
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the language model for Vosk:
   - Visit the official [Vosk Models](https://alphacephei.com/vosk/models) page and download the appropriate model for the desired language.
   - Extract the model into the project directory.


5. Setup Instructions:
   - Create a directory named `model` in the project root to store the Vosk model.
   - In the project root directory, create a file named `text.txt` to receive real-time transcribed text.

## How to Use

1. Run the application:
   ```bash
   python gui.py
   ```

   **Note**: You may need to select the correct microphone in the `cli.py` file. To do this, adjust the `device_index` parameter:

   ```python
   device_index = 3
   stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024, input_device_index=device_index)
   ```

2. Enter the name you want to monitor in the specified field.

3. The application will capture sounds and notify you when the name is mentioned.

## Contributions

Contributions are welcome! Feel free to open issues or make pull requests with improvements.

## License

This project is licensed under the [MIT License](LICENSE.txt).
