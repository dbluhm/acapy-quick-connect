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
    async with Controller(base_url=INVITER) as one, Controller(base_url=INVITEE) as two:
        conn_1, conn_2 = await didexchange(one, two)
        await one.post(
            f"/transactions/{conn_1.connection_id}/set-endorser-role",
            params={"transaction_my_job": "TRANSACTION_ENDORSER"}
        )
        await two.post(
            f"/transactions/{conn_2.connection_id}/set-endorser-role",
            params={"transactions_my_job": "TRANSACTION_AUTHOR"}
        )


if __name__ == "__main__":
    logging_to_stdout()
    asyncio.run(main())
