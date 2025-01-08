# PixelPerfect

PixelPerfect is a Python application designed to help you achieve optimal resolution and color accuracy on Windows devices. It adjusts the display settings to ensure your screen's resolution and color depth are configured for the best visual experience.

## Features

- Retrieves the current screen resolution and color depth.
- Sets the screen resolution to a common optimal setting (1920x1080).
- Adjusts the color depth to 32 bits per pixel for high color accuracy.

## Requirements

- Windows operating system.
- Python 3.x installed on your system.
- Administrator privileges may be required to change display settings.

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/PixelPerfect.git
   cd PixelPerfect
   ```

2. Ensure you have Python installed on your Windows device. You can download it from [python.org](https://www.python.org/downloads/).

3. (Optional) Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

## Usage

To run the application, navigate to the directory containing `pixel_perfect.py` and execute it with Python:

```bash
python pixel_perfect.py
```

The program will output the current display settings and adjust them to optimal values if necessary.

## Note

- This application uses Windows-specific APIs and PowerShell commands, so it will not work on non-Windows systems.
- Run the script with administrative privileges for best results.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements or enhancements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.