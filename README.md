# MCP-Application
A simple implementation of MCP server and an MCP client integrated with FastAPI

To run this code in your local machine, follow these steps:
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
4. <b>To test the client</b>
   ```bash
   # just run the fastapi app
   uvicorn main:app
   ```

### References:
[MCP Server docs](https://modelcontextprotocol.io/docs/develop/build-server)<br>
[MCP Client docs](https://modelcontextprotocol.io/docs/develop/build-client)

<b>Note:</b> If you want to use any other LLM, or want to change the gemini api call from openai (as used in this repo) to google sdk, you will need to modify the ```client/client.py```. Make sure to check both the input and output format as well as tool data format.