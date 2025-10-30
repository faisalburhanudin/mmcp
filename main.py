#!/usr/bin/env python3
import asyncio
import json
import click
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


@click.group()
def cli():
    """Simple MCP client for testing tool calls."""
    pass


@cli.command()
@click.option("--host", default="127.0.0.1", help="MCP server host")
@click.option("--port", default=23456, help="MCP server port")
def list_tools(host, port):
    """List available tools from MCP server."""
    asyncio.run(fetch_tools(host, port))


@cli.command()
@click.option("--host", default="127.0.0.1", help="MCP server host")
@click.option("--port", default=23456, help="MCP server port")
@click.option("--tool", default="amazon_get_purchase_history", help="Tool name to call")
@click.option("--params", default="{}", help="JSON string of tool parameters")
def call(host, port, tool, params):
    """Call a tool on the MCP server."""
    asyncio.run(call_tool(host, port, tool, params))


async def fetch_tools(host, port):
    """Connect to MCP server and fetch available tools."""
    try:
        # Construct server URL
        url = f"http://{host}:{port}/mcp-shopping/"

        # Connect to MCP server
        async with streamablehttp_client(url) as (read, write, _):
            async with ClientSession(read, write) as session:
                # Initialize connection
                await session.initialize()

                # List available tools
                tools = await session.list_tools()

                # Display tool names only
                for tool in tools.tools:
                    click.echo(tool.name)

    except Exception as e:
        import traceback

        click.echo(f"Error: {e}", err=True)
        click.echo(traceback.format_exc(), err=True)


async def call_tool(host, port, tool, params_str):
    """Connect to MCP server and call a tool."""
    try:
        # Parse parameters
        params = json.loads(params_str)

        # Construct server URL
        url = f"http://{host}:{port}/mcp-shopping"

        # Connect to MCP server
        async with streamablehttp_client(url) as (read, write, _):
            async with ClientSession(read, write) as session:
                # Initialize connection
                await session.initialize()

                # Call the tool
                result = await session.call_tool(tool, params)

                # Display result
                click.echo(json.dumps(result.model_dump(), indent=2))

    except json.JSONDecodeError as e:
        click.echo(f"Error: Invalid JSON in params: {e}", err=True)
    except Exception as e:
        import traceback

        click.echo(f"Error: {e}", err=True)
        click.echo(traceback.format_exc(), err=True)


if __name__ == "__main__":
    cli()
