# Simple Python Web Server

This project is a simple web server implemented in Python using the `http.server` module. It serves static HTML files and supports custom HTML pages.

## Features

- Serves static HTML files
- Supports different MIME types
- Customizable HTML pages
- Error handling for missing files and internal server errors

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gauthamnair2005/Procyon-WebServer.git
    cd simple-python-web-server
    ```

2. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

### Usage

1. Place your HTML files (e.g., `index.html`, `about.html`) in the same directory as `server.py`.

2. Run the server:
    ```sh
    python server.py
    ```

3. Open your web browser and navigate to `http://localhost:8088` to view the home page. Navigate to `http://localhost:8088/about.html` to view the about page.