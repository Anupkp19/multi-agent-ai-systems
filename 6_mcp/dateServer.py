# server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("date-server")

@mcp.tool()
def get_current_date() -> str:
    """Returns today's date"""
    from datetime import date
    return str(date.today())

if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8000) 