"""Download the current image from a Cognex In-Sight camera over FTP.

This script retrieves the image currently held by the camera (``image.bmp``).
It does NOT trigger a new acquisition: trigger the camera first (In-Sight
Explorer, a hardware trigger or a robot signal) if a fresh image is needed.

Credentials are never stored in the repository. They are read, in order of
priority, from command-line arguments, environment variables
(``COGNEX_IP``, ``COGNEX_USER``, ``COGNEX_PASSWORD``) or an interactive prompt.

Usage examples
--------------
    python vision/cognex/cognex_ftp_capture.py
    python vision/cognex/cognex_ftp_capture.py --ip <camera-ip> --show
    python vision/cognex/cognex_ftp_capture.py --count 10 --interval 0.5

Status: adapted from the team's first working sample notebook
(``vision/notebooks/cognex_ftp_capture.ipynb``). Image acquisition with this
method was reported to work in the lab; repeated capture (``--count``) has not
yet been validated on the real camera.
"""

from __future__ import annotations

import argparse
import os
import time
from datetime import datetime
from ftplib import FTP
from getpass import getpass
from io import BytesIO
from pathlib import Path

import cv2
import numpy as np

DEFAULT_REMOTE_FILE = "image.bmp"
DEFAULT_OUTPUT_DIR = Path("data/raw/cognex_captures")


def download_image_bytes(
    ip: str,
    username: str,
    password: str,
    remote_file: str = DEFAULT_REMOTE_FILE,
    port: int = 21,
    timeout: float = 10.0,
) -> bytes:
    """Return the raw bytes of ``remote_file`` downloaded from the camera."""
    buffer = BytesIO()
    with FTP() as ftp:
        ftp.connect(ip, port=port, timeout=timeout)
        ftp.login(user=username, passwd=password)
        ftp.retrbinary(f"RETR {remote_file}", buffer.write)
    return buffer.getvalue()


def decode_image(image_bytes: bytes, grayscale: bool = True) -> np.ndarray:
    """Decode image bytes (BMP, PNG, ...) into an OpenCV array."""
    flag = cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_UNCHANGED
    image = cv2.imdecode(np.frombuffer(image_bytes, dtype=np.uint8), flag)
    if image is None:
        raise RuntimeError("The camera did not return a valid image.")
    return image


def save_image_bytes(image_bytes: bytes, output_dir: Path, suffix: str = ".bmp") -> Path:
    """Save the original bytes with a microsecond timestamp and return the path."""
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_path = output_dir / f"cognex_{timestamp}{suffix}"
    file_path.write_bytes(image_bytes)
    return file_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ip", default=os.getenv("COGNEX_IP"), help="Camera IP address")
    parser.add_argument("--user", default=os.getenv("COGNEX_USER"), help="Camera username")
    parser.add_argument("--remote-file", default=DEFAULT_REMOTE_FILE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--count", type=int, default=1, help="Number of downloads")
    parser.add_argument("--interval", type=float, default=1.0, help="Seconds between downloads")
    parser.add_argument("--show", action="store_true", help="Display the last image")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ip = args.ip or input("Cognex IP address: ").strip()
    username = args.user or input("Camera username: ").strip()
    password = os.getenv("COGNEX_PASSWORD") or getpass("Camera password: ")

    image = None
    for i in range(args.count):
        start = time.perf_counter()
        image_bytes = download_image_bytes(ip, username, password, args.remote_file)
        image = decode_image(image_bytes)
        path = save_image_bytes(image_bytes, args.output_dir, Path(args.remote_file).suffix)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"[{i + 1}/{args.count}] shape={image.shape} download+decode={elapsed_ms:.1f} ms -> {path}")
        if i + 1 < args.count:
            time.sleep(args.interval)

    if args.show and image is not None:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(9, 6))
        plt.imshow(image, cmap="gray", vmin=0, vmax=255)
        plt.title("Image received from the Cognex camera")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    main()
