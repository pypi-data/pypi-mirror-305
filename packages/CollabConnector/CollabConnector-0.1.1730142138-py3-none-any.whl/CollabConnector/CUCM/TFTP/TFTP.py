import sys
import requests


class Connect:
    ip_address = ""

    def __init__(self, ip_address):
        self.ip_address = ip_address

    def download(self, filename: str, file_path: str = "") -> bytes:
        try:
            file = requests.get(f"http://{self.ip_address}:6970/{filename}").content
        except Exception as err:
            print(f"Error downloading TFTP {filename}: {err}", file=sys.stderr)
        else:
            if file_path:
                with open(file_path, "wb") as wav_file:
                    wav_file.write(file)
            return file