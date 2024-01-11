import requests
import os
from datetime import datetime
import gzip
import shutil


class BrdcController:
    def __init__(self, proxy_auth_token: str, urs_guid_ops: str):
        self.session = requests.Session()
        self.session.cookies.update(
            {"ProxyAuth": proxy_auth_token, "urs_guid_ops": urs_guid_ops}
        )

    def get_nasa_archive_link(self):
        current_date = datetime.now()

        return (
            f"https://cddis.nasa.gov/archive/gnss/data/daily/{current_date.year}/brdc/"
        )

    def get_current_filename(self):
        current_date = datetime.now()
        start_of_year = datetime(current_date.year, 1, 1)
        days_from_start = (current_date - start_of_year).days + 1
        formatted_days = f"{days_from_start * 10:04d}"

        return {
            "extracted": f"brdc{formatted_days}.{current_date.year % 100}n",
            "gzipped": f"brdc{formatted_days}.{current_date.year % 100}n.gz",
        }

    def is_file_exists(self, filename: str):
        directory_path = "./assets/brdc"
        file_path = os.path.join(directory_path, filename)

        if os.path.exists(file_path):
            return True
        else:
            return False

    def get_file(self):
        brdc_filename = self.get_current_filename()

        if self.is_file_exists(brdc_filename["gzipped"]):
            print(f"[!] {brdc_filename['gzipped']} already exists")
            return brdc_filename["extracted"]

        print(f"[!] Starting to download BRDC-file: {brdc_filename['gzipped']}")

        url = self.get_nasa_archive_link()
        response = self.session.get(f"{url}{brdc_filename['gzipped']}")

        if response.status_code != 200:
            return None

        os.makedirs("./assets/brdc", exist_ok=True)

        with open(f"./assets/brdc/{brdc_filename['gzipped']}", "wb") as file:
            file.write(response.content)

        with gzip.open(f"./assets/brdc/{brdc_filename['gzipped']}", "rb") as f_in:
            with open(f"./assets/brdc/{brdc_filename['extracted']}", "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

        print(f"[!] BRDC-file downloaded and extracted: {brdc_filename['gzipped']}")
        return brdc_filename["extracted"]
