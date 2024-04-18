"""Minimal reproducible example script.

This script is for you to use to reproduce a bug or demonstrate a feature.
"""

import asyncio
from os import getenv

from acapy_controller import Controller
from acapy_controller.logging import logging_to_stdout
from acapy_controller.protocols import didexchange

INVITER = getenv("INVITER", "http://alice:3001")
INVITEE = getenv("INVITEE", "http://bob:3001")


async def main():
    """Test Controller protocols."""
    async with Controller(base_url=INVITER) as alice, Controller(base_url=INVITEE) as bob:
        await didexchange(alice, bob)


if __name__ == "__main__":
    logging_to_stdout()
    asyncio.run(main())
