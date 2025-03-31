# Procyon WebServer 2025

Procyon WebServer (PWS) is a fast and efficient web server with support for **SLS/LSP (Server Logic Script/Linea Server Pages)** and **PHP**. It is designed for small to medium websites and provides a modern GUI for easy management.

## Features

- **SLS/LSP Support**: Dynamic server-side scripting with Linea Server Pages. (requires `lsp.py` and `liblinea.py` in the server folder).
- **PHP Support**: Execute PHP scripts seamlessly (requires PHP binaries in the server folder).
- **Static File Serving**: Serves static HTML, CSS, JavaScript, and other files.
- **Directory Listing**: Automatically lists directory contents when no index file is found.
- **Error Handling**: Displays detailed error messages for missing files and internal server errors.
- **Modern GUI**: A PyQt6-based GUI for starting, stopping, and monitoring the server with real-time logs.
- **Customizable Logs**: Displays server start/stop messages, mid-error logs, and runtime errors in the GUI.
- **Auto-Resize Support**: GUI components adjust dynamically to window size.
- **Dark Theme**: A sleek, modern dark theme for the GUI.

## Getting Started

### Prerequisites

- Python 3.x
- PyQt6 (for the GUI)
- PHP (optional, for PHP script execution)
- LSP (optional, for SLS/LSP support)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/gauthamnair2005/Procyon-WebServer.git
    cd Procyon-WebServer
    ```

2. Install the required Python dependencies:

    ```sh
    pip install pyqt6
    ```

3. Ensure you have PHP installed (if you plan to use PHP scripts). Add the PHP executable to your system's PATH.

### Usage

#### Running the Server (Command-Line Interface)

1. Place your HTML, LSP, or PHP files in the same directory as `server.py`.
2. Run the server:

    ```sh
    python server.py
    ```

3. Open your web browser and navigate to:
    - `http://localhost:<port>` (default port is `8086`).

#### Running the Server (Graphical User Interface)

1. Run the GUI:

    ```sh
    python server_gui.py
    ```

2. Enter the desired port number in the GUI and click "Start Server".
3. Monitor real-time logs and errors in the GUI.