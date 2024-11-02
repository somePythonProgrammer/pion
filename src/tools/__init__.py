import importlib
import logging
import os
import sys

from logger import logger

sys.path.append(os.path.dirname(__file__))

tools = [
    {
        "type": "function",
        "function": {
            "name": "idle",
            "description": "Call this function if no task is left to be done.",
        },
    },
]

function_map = {"idle": None}

BLACKLIST = ["__init__"]

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and file.strip(".py") not in BLACKLIST:
        module = importlib.import_module(file.strip(".py"))
        tools.append(module.tool_export)
        function_map[module.tool_export["function"]["name"]] = module.function
        logger.log(
            logging.DEBUG,
            f"DEBUG [toolchain]  Registered tool `{module.tool_export["function"]["name"]}`",
        )