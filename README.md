# FastAPI Project

This project is a FastAPI application that allows users to interact with an assistant through a web interface.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file from the `.env.sample` file:
    ```sh
    cp .env.sample .env
    ```

2. Open the `.env` file and replace the placeholder values with your actual API keys and other configuration values.

## Launching the App

1. Start the FastAPI application:
    ```sh
    uvicorn src.app:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## What the App Does

This FastAPI application allows users to:

- **Submit Profile**: Submit a profile once all questions have been answered.
- **View Profile**: View the user's profile.
- **Browse Market**: Browse available offers, listings, or products in the marketplace.

The application uses OpenAI and LangChain APIs to provide assistant functionalities.
