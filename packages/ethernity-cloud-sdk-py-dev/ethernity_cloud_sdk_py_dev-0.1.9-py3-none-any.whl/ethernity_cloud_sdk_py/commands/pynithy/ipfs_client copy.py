# ipfs_client.py

import argparse
import os
import sys
import time
import math
import ipfshttpclient
import asyncio
from pathlib import Path
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# Set default max retries from environment or default to 5
DEFAULT_MAX_RETRIES = int(os.getenv("REACT_APP_IPFS_RETRIES", "5"))

# Global variable for IPFS client
ipfs = None


def initialize(host, protocol="http", port=5001, token=""):
    """
    Initialize the IPFS client.
    """
    global ipfs
    try:
        if "http" in host:
            address = host
        else:
            address = f"/dns/{host}/tcp/{port}/{protocol}"
        if token:
            ipfs = ipfshttpclient.connect(address, session=True, auth=(token, ""))
        else:
            ipfs = ipfshttpclient.connect(address, session=True)
    except Exception as e:
        print(f"Failed to connect to IPFS host {host}: {e}")
        sys.exit(1)


def upload_file_to_ipfs(file_path):
    """
    Upload a single file to IPFS.
    """
    try:
        res = ipfs.add(file_path)
        cid = res["Hash"]
        with open("./IPFS_DOCKER_COMPOSE_HASH.ipfs", "w") as f:
            f.write(cid)
        return cid
    except Exception as e:
        print(f"Failed to upload file to IPFS: {e}")
        return "Failed to upload file to IPFS, please try again."


def upload_folder_to_ipfs(folder_path):
    """
    Upload a folder to IPFS.
    """
    try:
        print(f"Uploading folder to IPFS: {folder_path}")
        # TQDM progress bar setup
        total_size = sum(
            f.stat().st_size for f in Path(folder_path).rglob("*") if f.is_file()
        )
        progress_bar = tqdm(
            total=total_size, unit="B", unit_scale=True, desc="Uploading"
        )

        def progress_callback(total_transferred, total_size):
            progress_bar.update(total_transferred - progress_bar.n)

        # Unfortunately, ipfshttpclient doesn't support progress callbacks directly,
        # so we've to manage without accurate progress updates.

        res = ipfs.add(folder_path, recursive=True, pin=True, wrap_with_directory=True)
        dir_cid = res[-1]["Hash"]
        progress_bar.close()

        with open("./IPFS_HASH.ipfs", "w") as f:
            f.write(dir_cid)
        return dir_cid
    except Exception as e:
        print(f"Upload failed: {e}")
        return "Upload failed."


def get_retry_delay(retry_count, base_delay=1):
    """
    Calculate exponential backoff delay.
    """
    return base_delay * (2**retry_count)


def get_from_ipfs(hhash, file_path, max_retries=DEFAULT_MAX_RETRIES):
    """
    Download a file from IPFS.
    """
    retry_count = 0
    while retry_count < max_retries:
        try:
            res = ipfs.cat(hhash)
            with open(file_path, "wb") as f:
                f.write(res)
            return
        except Exception as e:
            print(f"Error: {e}")
            retry_count += 1
            if retry_count < max_retries:
                delay = get_retry_delay(retry_count)
                print(f"Retrying... ({retry_count}/{max_retries}) in {delay} seconds")
                time.sleep(delay)
            else:
                raise Exception("ECError.IPFS_DOWNLOAD_ERROR")


def download_folder_from_ipfs(cid, output_path):
    """
    Download a folder from IPFS.
    """
    try:
        print(f"Downloading folder from IPFS: {cid}")
        # TQDM progress bar setup
        # Note: ipfshttpclient doesn't provide progress for get operations
        ipfs.get(cid, target=output_path)
        print(f"Download complete. Files saved to {output_path}")
    except Exception as e:
        print(f"Error downloading folder: {e}")
        return "err"


def main(
    host="localhost",
    protocol="http",
    port=5001,
    token="",
    hhash="",
    filePath="",
    folderPath="",
    action="",
    output="",
):
    # parser = argparse.ArgumentParser(description="IPFS Client")
    # parser.add_argument("--host", help="IPFS host", default="localhost")
    # parser.add_argument("--protocol", help="Protocol (http or https)", default="http")
    # parser.add_argument("--port", help="IPFS port", type=int, default=5001)
    # parser.add_argument("--token", help="Authorization token", default="")
    # parser.add_argument("--hhash", help="IPFS hash")
    # parser.add_argument("--filePath", help="Path to the file")
    # parser.add_argument("--folderPath", help="Path to the folder")
    # parser.add_argument(
    #     "--action", help="Action to perform (upload, download)", required=True
    # )
    # parser.add_argument("--output", help="Output path for download")

    # args = parser.parse_args()

    initialize(host, protocol, port, token)

    if action == "upload":
        if filePath:
            hhash = upload_file_to_ipfs(filePath)
            print(f"{hhash}")
        elif folderPath:
            retry_count = 0
            hhash = None
            while (not hhash or hhash == "Upload failed.") and retry_count < 3:
                try:
                    hhash = upload_folder_to_ipfs(folderPath)
                    print(f"{hhash}")
                except Exception as e:
                    print(f"Error uploading folder: {e}")
                if not hhash or hhash == "Upload failed.":
                    retry_count += 1
                    print(f"Retrying... ({retry_count}/3)")
            if not hhash or hhash == "Upload failed.":
                print("Failed to upload folder to IPFS, please try again.")
            sys.exit(0)
        else:
            print("Please provide a filePath or folderPath for upload.")
    elif action == "download":
        if filePath:
            print(f"Downloading file from IPFS: {hhash}")
            get_from_ipfs(hhash, filePath)
            print(f"File downloaded. {hhash}")
        elif folderPath:
            print(f"Downloading folder from IPFS: {hhash}")
            download_folder_from_ipfs(hhash, folderPath)
            print(f"Folder downloaded. {hhash}")
        else:
            print("Please provide a filePath or folderPath for download.")
    else:
        print("Please provide a valid action (upload, download).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IPFS Client")
    parser.add_argument("--host", help="IPFS host", default="localhost")
    parser.add_argument("--protocol", help="Protocol (http or https)", default="http")
    parser.add_argument("--port", help="IPFS port", type=int, default=5001)
    parser.add_argument("--token", help="Authorization token", default="")
    parser.add_argument("--hhash", help="IPFS hash")
    parser.add_argument("--filePath", help="Path to the file")
    parser.add_argument("--folderPath", help="Path to the folder")
    parser.add_argument(
        "--action", help="Action to perform (upload, download)", required=True
    )
    parser.add_argument("--output", help="Output path for download")

    args = parser.parse_args()

    main(
        host=args.host,
        protocol=args.protocol,
        port=args.port,
        token=args.token,
        hhash=args.hhash,
        filePath=args.filePath,
        folderPath=args.folderPath,
        action=args.action,
        output=args.output,
    )
