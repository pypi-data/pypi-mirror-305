# Streamlit IFrame Component

This component is an iframe wrapper that allows you to render an HTML iframe component and receive data posted using `window.parent.postMessage` in the `src` URL.

## Features

- Render an HTML iframe within a Streamlit app.
- Capture and return data posted from the iframe using `window.parent.postMessage`.

## Usage

Install streamlit-iframe with pip

```sh
pip install streamlit-iframe
```

Use the component in your Streamlit app:

```python
import streamlit as st
from streamlit_iframe import streamlit_iframe

event = streamlit_iframe({
    "src": "https://www.example.com",
    "height": "500px",
    "width": "600px",
})
```

## Development

To set up the development environment, follow these steps:

1. Create a virtual environment:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install the required dependencies:
    ```sh
    pip install streamlit
    ```

## Running the Example

To run the example Streamlit app, use the following command:
```sh
streamlit run ./example.py
```