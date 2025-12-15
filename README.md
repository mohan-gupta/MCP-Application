# MCP-Application
A simple MCP server and an MCP client

To run this agent in your local machine, follow these steps:
1. <b>Set-up the .env file</b>
   ```bash
    GOOGLE_API_KEY=<your google gemini api key>

    WEATHER_API_KEY=<your open weather map api key>
   ```
2. <b>Set-up the environment,</b> for environment setup I have used [uv](https://docs.astral.sh/uv/guides/install-python/)
   ```bash
    # MCP supports python>=3.10
    uv venv --python 3.12

    # for windows:
    .venv\Scripts\activate

    # for mac:
    source .venv/bin/activate

    # install dependencies
    uv pip install -r requirements.txt
3. <b>To run the Server</b>
   ```bash
    # To test server
    mcp dev server/server.py
    ```
