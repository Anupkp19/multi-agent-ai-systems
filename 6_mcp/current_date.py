import datetime
import re
from mcp.server.fastmcp import FastMCP;

mcp = FastMCP("current_date")

@mcp.tool()
async def print_current_date()->str:
    "It prints the current date in the string format"
    return datetime.datetime.now().isoformat()

if __name__ == "__main__":
    mcp.run(transport='stdio')


