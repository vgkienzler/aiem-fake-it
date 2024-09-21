# Project

This project demonstrate how to easily use OpenAI Assistant API to test and 'fake' a chatbot with advanced function like updating a profile, viewing the profile and browsing a marketplace.

The assistant, its prompt and the tools it uses are all defined from the Openai Assistant dashboard.

The assistant created is called from within the app using its ID.

## Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:vgkienzler/aiem-fake-it.git 
    cd aiem-fake-it
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

## What the App Does (or pretend it does)

This application allows users to:

- **Submit Profile**: Submit a profile once all questions have been answered (it calls the submit_profile tool of the assistant).
- **View Profile**: View the user's profile (it calls the view_profile tool of the assistant).
- **Browse Market**: Browse available offers, listings, or products in the marketplace (it calls the browse_market tool of the assistant).

The application uses OpenAI Assistant and LangChain APIs to provide assistant functionalities.
