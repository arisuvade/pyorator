# PyOrator
Pyorator is a speech generator app in development for Linux. With Pyorator, you can generate speech from any text input, making it a useful tool for anyone who needs to create audio content.

## Installation
To use the PyOrator app, you'll need to install the tk, customtkinter, and gtts packages. Also, you need to clone this repository. Here's how you can do that:

1. Install the tk package: 
    - Arch: `sudo pacman -S tk`
    - Debian: `sudo apt-get install python-tk`
    - Fedora: `sudo dnf install tkinter`

2. Install the customtkinter package:
    - Install the package using pip:
    ```bash
    $ pip install customtkinter
    ```

3. Install the gtts package:
    - Install the package using pip:
    ```bash
    $ pip install gtts
    ```

4. Clone this repository:
    ```bash
    $ git clone https://github.com/arisuvade/pyorator.git
    ```

## Usage
To use the PyOrator app, follow these steps:

1. Open a terminal window and navigate to the directory where you cloned the repository.

2. Run the script:
    ```bash
    $ cd pyorator
    $ cd [VERSION]
    $ ./main.py
    ```

3. Follow the prompts to customize the text contents and file name.

4. Press "Generate Speech" to generate the speech and "Play" to play it.

5. Save it using the save button or delete it.

## License
This project is licensed under the [MIT License](https://github.com/arisuvade/pyorator/blob/main/LICENSE).

## Acknowledgements
This app was inspired by the need to create an easy-to-use speech generator for Linux users. Thanks to the open-source community for providing the tools and resources needed to create this app.

## Contribution
If you find any bugs or issues, feel free to open an issue or submit a pull request to contribute to the project.
