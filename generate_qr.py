from pathlib import Path

import segno


BASE_URL = "https://crbc-nigeria.github.io/crbc-contacts"
CONTACT_URL = f"{BASE_URL}/c/yi-wenwen/"

ROOT = Path(__file__).resolve().parent
QR_DIR = ROOT / "qr"
QR_DIR.mkdir(exist_ok=True)


def save_qr(name: str, url: str) -> None:
    qr = segno.make(url, error="h", micro=False)
    qr.save(QR_DIR / f"{name}.png", scale=16, border=4, dark="black", light="white")
    qr.save(QR_DIR / f"{name}.svg", scale=1, border=4, dark="black", light="white")


save_qr("yi-wenwen-page", CONTACT_URL)
print(CONTACT_URL)
