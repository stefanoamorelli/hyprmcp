from mcp.server.fastmcp import FastMCP
import os
import subprocess

# Initialize the MCP server
mcp = FastMCP(
    "Hyprland MCP",
    dependencies=[
        "subprocess",
    ],
)


def run_hyprctl_command(command: list) -> str:
    """Runs a hyprctl command and returns its output."""
    try:
        env = os.environ.copy()

        # Check if HYPRLAND_INSTANCE_SIGNATURE is missing
        if "HYPRLAND_INSTANCE_SIGNATURE" not in env:
            # Optionally, you could try loading it from a file or something here
            return "Error: HYPRLAND_INSTANCE_SIGNATURE is not set."

        result = subprocess.run(
            ["hyprctl"] + command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return (
            f"Error running command: {' '.join(['hyprctl'] + command)}\n"
            f"Return code: {e.returncode}\n"
            f"STDOUT:\n{e.stdout.strip()}\n"
            f"STDERR:\n{e.stderr.strip()}"
        )
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_version() -> str:
    """Returns the Hyprland version and build information."""
    return run_hyprctl_command(["version"])


@mcp.tool()
def list_monitors() -> str:
    """Lists all outputs with their properties."""
    return run_hyprctl_command(["monitors", "-j"])


@mcp.tool()
def list_workspaces() -> str:
    """Lists all workspaces with their properties."""
    return run_hyprctl_command(["workspaces", "-j"])


@mcp.tool()
def list_clients() -> str:
    """Lists all windows with their properties."""
    return run_hyprctl_command(["clients", "-j"])


@mcp.tool()
def list_devices() -> str:
    """Lists all connected input devices."""
    return run_hyprctl_command(["devices", "-j"])


@mcp.tool()
def get_active_window() -> str:
    """Returns the active window name."""
    return run_hyprctl_command(["activewindow", "-j"])


@mcp.tool()
def list_layers() -> str:
    """Lists all the layers."""
    return run_hyprctl_command(["layers", "-j"])


@mcp.tool()
def get_splash() -> str:
    """Returns the current random splash."""
    return run_hyprctl_command(["splash"])


@mcp.tool()
def dispatch_command(dispatch: str, argument: str) -> str:
    """Calls a dispatcher with an argument."""
    return run_hyprctl_command(["dispatch", dispatch, argument])


@mcp.tool()
def set_keyword(keyword: str, value: str) -> str:
    """Sets a config keyword dynamically."""
    return run_hyprctl_command(["keyword", keyword, value])


@mcp.tool()
def reload_config() -> str:
    """Forces a reload of the config file."""
    return run_hyprctl_command(["reload"])


@mcp.tool()
def enter_kill_mode() -> str:
    """Enters kill mode to terminate an app by clicking on it."""
    return run_hyprctl_command(["kill"])


# Run the MCP server
if __name__ == "__main__":
    mcp.run()
