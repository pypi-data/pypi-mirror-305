import asyncio
import logging
import re
import socket

# For WARP to apply network configurations, in seconds
CONFIG_DELAY: int = 2 * 60
LOGGER = logging.getLogger(__name__)


class WarpError(Exception):
    pass


async def _dns_test() -> bool:
    domain = "notify.bugsnag.com"  # Using a domain that used to fail

    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False


async def _dns_ready(*, attempts: int, seconds_per_attempt: int) -> bool:
    for attempt_number in range(1, attempts + 1):
        LOGGER.info(
            "Waiting for DNS resolution... Attempt %s/%s",
            attempt_number,
            attempts,
        )
        if await _dns_test():
            LOGGER.info(
                "DNS resolution successful after %s attempts",
                attempt_number,
            )
            return True
        LOGGER.info(
            "DNS resolution failed. Retrying in %s seconds",
            seconds_per_attempt,
        )
        await asyncio.sleep(seconds_per_attempt)
    LOGGER.error("DNS resolution failed after %s attempts", attempts)
    return False


async def warp_cli(*args: str) -> tuple[bytes, bytes]:
    proc = await asyncio.create_subprocess_exec(
        "warp-cli",
        "--accept-tos",
        *args,
        stderr=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.DEVNULL,
    )
    stdout, stderr = await asyncio.wait_for(proc.communicate(), 30)

    if proc.returncode != 0:
        raise WarpError(stderr.decode())

    if not await _dns_ready(attempts=40, seconds_per_attempt=3):
        raise WarpError("Failed to resolve DNS")

    return (stdout, stderr)


async def warp_cli_get_virtual_network_id(vnet_name: str) -> str:
    vnet_id_match = re.search(
        f"ID: (.*)\n  Name: {vnet_name}",
        (await warp_cli("vnet"))[0].decode(),
    )
    if not vnet_id_match:
        raise WarpError("Failed to find virtual network")

    return vnet_id_match.groups()[0]


async def warp_cli_connect_virtual_network(vnet_name: str) -> None:
    vnet_id = await warp_cli_get_virtual_network_id(vnet_name)
    LOGGER.info(
        "Connecting to virtual network",
        extra={
            "extra": {
                "name": vnet_name,
                "network_id": vnet_id,
            }
        },
    )
    await warp_cli("vnet", vnet_id)
    await asyncio.sleep(CONFIG_DELAY)
    LOGGER.info(
        "Connected to virtual network",
        extra={
            "extra": {
                "name": vnet_name,
                "network_id": vnet_id,
                "status": (await warp_cli("status"))[0].decode(),
            }
        },
    )
