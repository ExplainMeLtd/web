"""Build-only: PYTHONPATH=<qrcode install> python3 scripts/generate-qr.py."""
from pathlib import Path
import qrcode

APP_STORE_URL = 'https://apps.apple.com/app/id6760954081'
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
qr.add_data(APP_STORE_URL)
qr.make(fit=True)
image = qr.make_image(fill_color='#244f4b', back_color='white')
image.save(Path(__file__).resolve().parents[1] / 'assets/app-store-qr.png')
