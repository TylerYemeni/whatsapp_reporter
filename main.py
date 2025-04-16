from report_engine import send_report
from proxy_rotator import rotate_proxy
from number_generator import get_random_number
from config import TARGET_NUMBER, REPORT_COUNT

def main():
    for _ in range(REPORT_COUNT):
        proxy = rotate_proxy()
        fake_number = get_random_number()
        print(f"Using number {fake_number} with proxy {proxy}")
        try:
            send_report(TARGET_NUMBER, fake_number, proxy)
        except Exception as e:
            print(f"[!] Failed: {e}")

if __name__ == "__main__":
    main()
