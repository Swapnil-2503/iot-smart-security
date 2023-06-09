# Smart Home Security IoT Project

This project implements a smart home security system using IoT technologies. It includes a motion detection module, a backend server, and a web-based frontend interface to display notifications.

## Project Components

The project consists of the following components:

- `index.html`: HTML file containing the frontend interface code for displaying notifications.
- `server.py`: Python file implementing the backend server to handle notification requests.
- `motion/motion_detection.py`: Python file that detects motion using a PIR sensor and sends notifications to the server.

## Prerequisites

Before running the project, ensure the following prerequisites are met:

- Raspberry Pi or similar device with GPIO support.
- PIR sensor connected to the appropriate GPIO pin.
- Python 3.x installed on the device.
- Required Python libraries installed (`RPi.GPIO`, `requests`, `flask`).

## Setup

Follow these steps to set up and run the project:

1. Clone or download the project repository.

2. Install the required Python libraries using the command: `pip install RPi.GPIO requests flask`.

3. Update the `SERVER_URL` variable in `motion_detection.py` and `server.py` to the appropriate address of your server.

4. Open a terminal and navigate to the project directory.

5. Start the backend server by running the command: `python server.py`.

6. In a separate terminal, navigate to the `motion` directory using the command: `cd motion`.

7. Run the motion detection module by executing the command: `python motion_detection.py`.

8. Open a web browser and go to `http://localhost:3000` to access the frontend interface.

## Usage

- The motion detection module will monitor the PIR sensor for any motion. When motion is detected, it will send a notification to the backend server.

- The backend server receives the notification and stores it. The frontend interface fetches notifications from the server and displays them.

- You can customize the frontend interface, add additional features, or integrate with other services as needed.

## Contributing

Contributions are welcome! If you have any suggestions or improvements for the project, feel free to open an issue or submit a pull request.

## Acknowledgments

Special thanks to the open-source community for providing helpful libraries and resources used in this project.

