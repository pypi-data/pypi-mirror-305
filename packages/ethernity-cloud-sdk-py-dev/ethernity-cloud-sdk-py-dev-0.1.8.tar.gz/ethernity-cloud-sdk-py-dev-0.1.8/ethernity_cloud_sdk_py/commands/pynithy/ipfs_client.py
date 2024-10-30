import requests  # type: ignore
import argparse
import os, sys, time


class IPFSClient:
    def __init__(
        self, api_url: str = "http://ipfs.ethernity.cloud:5001/api/v0", token: str = ""
    ) -> None:
        self.api_url = api_url
        self.headers = {}
        if token:
            self.headers = {"authorization": token}

    def upload_file(self, file_path: str) -> None:
        add_url = f"{self.api_url}/add"

        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(add_url, files=files, headers=self.headers)

        if response.status_code == 200:
            try:
                response_data = response.json()
                ipfs_hash = response_data["Hash"]
                print(f"Successfully uploaded to IPFS. Hash: {ipfs_hash}")
                return ipfs_hash
            except Exception as e:
                print(f"Failed to upload to IPFS. Error: {e}")
                return None
        else:
            print(f"Failed to upload to IPFS. Status code: {response.status_code}")
            print(response.text)
            return None

    def upload_to_ipfs(self, data: str) -> None:
        add_url = f"{self.api_url}/add"
        files = {"file": data}
        response = requests.post(add_url, files=files, headers=self.headers)

        if response.status_code == 200:
            try:
                response_data = response.json()
                ipfs_hash = response_data["Hash"]
                print(f"Successfully uploaded to IPFS. Hash: {ipfs_hash}")
                return ipfs_hash
            except Exception as e:
                print(f"Failed to upload to IPFS. Error: {e}")
                return None
        else:
            print(f"Failed to upload to IPFS. Status code: {response.status_code}")
            print(response.text)
            return None

    def upload_folder_to_ipfs(self, folder_path: str) -> None:
        add_url = f"{self.api_url}/add?recursive=true&wrap-with-directory=true&pin=true&progress=true"
        files = {"file": open(folder_path, "rb")}
        response = requests.post(add_url, files=files, headers=self.headers)

        if response.status_code == 200:
            try:
                response_data = response.json()
                ipfs_hash = response_data["Hash"]
                print(f"Successfully uploaded to IPFS. Hash: {ipfs_hash}")
                return ipfs_hash
            except Exception as e:
                print(f"Failed to upload to IPFS. Error: {e}")
                return None
        else:
            print(f"Failed to upload to IPFS. Status code: {response.status_code}")
            print(response.text)

    def download_file(
        self, ipfs_hash: str, download_path: str, attempt: int = 0
    ) -> None:
        gateway_url = f"https://ipfs.io/ipfs/{ipfs_hash}"
        response = requests.get(url=gateway_url, timeout=60, headers=self.headers)

        if response.status_code == 200:
            with open(download_path, "wb") as file:
                file.write(response.content)
            print(f"File downloaded successfully to {download_path}")
        else:
            print(
                f"Failed to download from IPFS. Attempt {attempt}. Status code: {response.status_code}. Response text: {response.text}.\n{'Trying again...' if attempt < 6 else ''}"
            )
            if attempt < 6:
                self.download_file(ipfs_hash, download_path, attempt + 1)

    def get_file_content(self, ipfs_hash: str, attempt: int = 0) -> None:
        url = self.api_url
        gateway_url = f"{url}/cat?arg={ipfs_hash}"
        response = requests.post(url=gateway_url, timeout=60, headers=self.headers)

        if response.status_code == 200:
            # TODO: use a get encoding function to determine the encoding
            return response.content.decode("utf-8")
        else:
            print(
                f"Failed to get content from IPFS. Attempt {attempt}. Status code: {response.status_code}. Response text: {response.text}.\n{'Trying again...' if attempt < 6 else ''}"
            )
            if attempt < 6:
                self.get_file_content(ipfs_hash, attempt + 1)

        return None


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
    global ipfs_client
    ipfs_client = IPFSClient(host, token)

    if action == "upload":
        if filePath:
            hhash = ipfs_client.upload_file(filePath)
            print(f"{hhash}")
            with open("IPFS_DOCKER_COMPOSE_HASH.ipfs", "w") as f:
                f.write(hhash)

        elif folderPath:
            retry_count = 0
            hhash = None
            while (not hhash or hhash == "Upload failed.") and retry_count < 3:
                try:
                    hhash = ipfs_client.upload_folder_to_ipfs(folderPath)
                    with open("./IPFS_HASH.ipfs", "w") as f:
                        f.write(hhash)
                    print(f"{hhash}")
                except Exception as e:
                    print(f"Error uploading folder: {e}")
                if not hhash or hhash == "Upload failed.":
                    retry_count += 1
                    print(f"Retrying... ({retry_count}/3)")
                    # add a delay here
                    time.sleep(5)
            if not hhash or hhash == "Upload failed.":
                print("Failed to upload folder to IPFS, please try again.")
            sys.exit(0)
        else:
            print("Please provide a filePath or folderPath for upload.")
    # elif action == "download":
    #     if filePath:
    #         print(f"Downloading file from IPFS: {hhash}")
    #         get_from_ipfs(hhash, filePath)
    #         print(f"File downloaded. {hhash}")
    #     elif folderPath:
    #         print(f"Downloading folder from IPFS: {hhash}")
    #         download_folder_from_ipfs(hhash, folderPath)
    #         print(f"Folder downloaded. {hhash}")
    #     else:
    #         print("Please provide a filePath or folderPath for download.")
    else:
        print("Please provide a valid action (upload, download).")


# Example usage
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
