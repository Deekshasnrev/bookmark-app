# Social Media Bookmark App

Social Media Bookmark App is a simple Python application that uses the Tkinter library to create a graphical user interface (GUI). The app provides buttons to quickly open your LinkedIn and GitHub profiles in your default web browser.

## Features

- **Quick Access**: Easily open your LinkedIn and GitHub profiles with a single click.
- **Simple GUI**: The app has a minimalistic design, making it easy to use.
- **Error Handling**: Includes basic error handling to manage incorrect URLs.
- **Extensible**: You can easily add more buttons for other social media platforms.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/social-media-bookmark-app.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd social-media-bookmark-app
    ```
3. **Install required dependencies:**
    This app only requires Python's standard library, so no additional installations are necessary.

4. **Run the application:**
    ```bash
    python app.py
    ```

## Usage

- Run the application, and a window will appear with buttons labeled "LinkedIn" and "GitHub".
- Click on any button to open the respective social media profile in your default web browser.

## Extending the App

To add more social media platforms:

1. Create a new function similar to `open_linkedin` or `open_github` for the desired platform.
2. Add a new button in the `create_window()` function and bind it to the new function.
3. Update the interface layout if needed.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you find a bug or have a feature request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Deeksha S N** - [LinkedIn](https://www.linkedin.com/in/deeksha-s-n) | [GitHub](https://github.com/Deekshasnrev)
