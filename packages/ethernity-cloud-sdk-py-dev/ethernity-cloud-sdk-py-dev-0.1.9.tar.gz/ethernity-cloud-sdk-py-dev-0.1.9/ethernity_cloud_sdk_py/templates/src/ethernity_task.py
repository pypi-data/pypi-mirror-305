import os
import sys

from ethernity_cloud_runner_py.runner import EthernityCloudRunner  # type: ignore


def execute_task() -> None:
    ipfs_address = "http://ipfs.ethernity.cloud:5001/api/v0"
    # ipfs_address = "https://ipfs-sdk.ethernity.cloud:5001/api/v0"

    code = '___etny_result___(hello("Hello, Python World!"))'

    runner = EthernityCloudRunner()
    runner.initialize_storage(ipfs_address)

    resources = {
        "taskPrice": 8,
        "cpu": 1,
        "memory": 1,
        "storage": 1,
        "bandwidth": 1,
        "duration": 1,
        "validators": 1,
    }
    # this will execute a new task using Python template and will run the code provided above
    # the code will run on the TESTNET network
    runner.run(
        "etny-pynithy-testnet",
        code,
        "0xd58f5C1834279ABD601df85b3E4b2323aDD4E75e",
        resources,
    )


if __name__ == "__main__":
    execute_task()
