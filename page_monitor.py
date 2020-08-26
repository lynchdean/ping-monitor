import hashlib
import time

import requests


class PageMonitor:
    def __init__(self, ref_url, wait_time=1.0):
        self.ref_url = ref_url
        self.wait_time = wait_time

    def wait_for_update(self):
        has_updated = False
        page = requests.get(self.ref_url)
        reference_hash = hashlib.md5(page.text.encode('utf-8'))
        reference_digest = reference_hash.hexdigest()

        while not has_updated:
            new_page = requests.get(self.ref_url)
            new_hash = hashlib.md5(new_page.text.encode('utf-8'))
            if new_hash.hexdigest() == reference_digest:
                print("No changes.")
                reference_digest = new_hash.hexdigest()
            else:
                print("Changes detected!")
                has_updated = True

            time.sleep(self.wait_time)
