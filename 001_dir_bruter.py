import requests
import argparse
from urllib.parse import urljoin

def brute_force_dirs(url, wordlist):
    try:
        with open(wordlist, 'r') as f:
            paths = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"[!] ไม่พบไฟล์: {wordlist}")
        return

    print(f"[+] เริ่มยิง request ไปยัง {url}")
    for path in paths:
        full_url = urljoin(url, path)
        try:
            r = requests.get(full_url, timeout=5)
            if r.status_code in [200, 301, 302, 403]:
                print(f"[+] พบ path: {full_url} ({r.status_code})")
        except requests.RequestException:
            continue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='🛠 Directory Bruteforcer Tool')
    parser.add_argument('url', help='URL เป้าหมาย (เช่น https://example.com/)')
    parser.add_argument('wordlist', help='Path ไปยังไฟล์ wordlist.txt')
    args = parser.parse_args()

    brute_force_dirs(args.url, args.wordlist)
