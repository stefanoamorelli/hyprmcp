<div align="center">

# Hyprland MCP Server

</div>

---

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')

</div>

---

A lightweight, unofficial [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) server that exposes all the functionality of `hyprctl`—the command-line interface for the [Hyprland](https://wiki.hyprland.org/) Wayland compositor—to language models.

This server enables natural language interfaces to query and control Hyprland's window management, layouts, inputs, and more.

> **Note:** This project is experimental and in beta.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/stefanoamorelli/hyprmcp.git
cd hyprmcp
```

### 2. Grab your `HYPRLAND_INSTANCE_SIGNATURE`

```bash
echo $HYPRLAND_INSTANCE_SIGNATURE
```

### 3. Install the server in your MCP client

For example, in Claude Desktop, modify the `~/.config/Claude/claude_desktop_config.json` file as follows:

```json
"Hyperland MCP Server": {
  "command": "uv",
  "args": [
    "run",
    "--with",
    "mcp[cli]",
    "--with",
    "subprocess",
    "mcp",
    "run",
   "<global path of the repo>/hyprmcp/hyprmcp/server.py"
  ],
  "env": {
    "PYTHONPATH": "<global path of the repo>/hyprmcp",
    "HYPRLAND_INSTANCE_SIGNATURE": "<your-hyprland-instance-signature>"
  }
},
```

---

## 🧰 Available Tools

| Tool Name             | Description                                       |
|-----------------------|---------------------------------------------------|
| `run_hyprctl_command` | Executes arbitrary `hyprctl` commands.            |
| `get_version`         | Retrieves the Hyprland version and build info.    |
| `list_monitors`       | Lists all connected monitors and properties.      |
| `list_workspaces`     | Lists all active workspaces.                      |
| `list_clients`        | Lists all windows and their properties.           |
| `list_devices`        | Lists all connected input devices.                |
| `get_active_window`   | Shows the currently active window details.        |
| `list_layers`         | Displays all layers in the compositor.            |
| `get_splash`          | Retrieves the current random splash message.      |
| `dispatch_command`    | Dispatches a command to Hyprland.                 |
| `set_keyword`         | Dynamically sets a configuration keyword.         |
| `reload_config`       | Forces a reload of the Hyprland config file.       |
| `enter_kill_mode`     | Enables kill mode to terminate windows by click.  |

These tools allow language models to interact with Hyprland's features seamlessly.

---

## 💡 Example Usage

**User Prompt:** "Switch to workspace 2."

**MCP Server Action:** Executes `hyprctl dispatch workspace 2`.

**User Prompt:** "What is the current active window?"

**MCP Server Action:** Executes `hyprctl activewindow -j` and returns the details.

---

## 🛠️ Development

To run the server locally for development:

```bash
mcp dev server.py
```

Ensure that Hyprland is running and the necessary environment variables are set.

---

## 📚 References

- [Hyprland Documentation](https://wiki.hyprland.org/)
- [Model Context Protocol](https://github.com/modelcontextprotocol)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)

---

## 📜 License

[MIT License](LICENSE) © 2025 Stefano Amorelli

