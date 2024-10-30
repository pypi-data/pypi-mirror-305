# Nitrado API

Python module for easily interacting with the Nitrado API, allowing game server management and common operations like whitelist management, event configuration, file validation, and more.

## Features

- Retrieve server details
- Restart and stop the server
- Manage player lists (whitelist, banlist, priority list)
- Handle configuration files (upload, download, validate)
- Schedule automatic restarts
- Easy and extensible setup

## Requirements

This module requires Python 3.6 or higher and the `aiohttp` library to handle asynchronous HTTP requests.

## Installation

To install directly from GitHub:

```bash
pip install git+https://github.com/yourusername/nitrado_api.git
```

## Basic Usage

Here's an example to get started with the module:

```python
import asyncio
from nitrado_api import NitradoAPI

async def main():
    nitrado_api = NitradoAPI("YOUR_NITRADO_TOKEN")

    # Retrieve server details
    server_details = await nitrado_api.get_server_details(nitrado_id="123456")
    print("Server details:", server_details)

    # Restart the server
    await nitrado_api.restart_server(nitrado_id="123456")

    # Add users to the whitelist
    await nitrado_api.manage_list("123456", action="add", list_type="whitelist", members=["User1", "User2"])

# Run the main function
asyncio.run(main())
```
## Function Documentation

NitradoAPI(nitrado_token)

- Initializes the module with the Nitrado API token.

Main Methods

- get_server_details(nitrado_id): Retrieves details for the specified server.
- restart_server(nitrado_id): Restarts the server.
- stop_server(nitrado_id): Stops the server.
- manage_list(nitrado_id, action, list_type, members): Manages the whitelist, banlist, or priority list to add or remove players.

## Contributions

Contributions are welcome. If you find an issue or have a suggestion, please open an issue or make a pull request on the GitHub repository.

