"""Offline tests for the Cognex capture helpers (no camera required)."""

import sys
from pathlib import Path

import cv2
import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "vision" / "cognex"))

from cognex_ftp_capture import decode_image, save_image_bytes  # noqa: E402


def _synthetic_bmp(height: int = 48, width: int = 64) -> bytes:
    image = np.tile(np.arange(width, dtype=np.uint8), (height, 1))
    ok, encoded = cv2.imencode(".bmp", image)
    assert ok
    return encoded.tobytes()


def test_decode_valid_bmp_returns_grayscale_array():
    image = decode_image(_synthetic_bmp())
    assert image.shape == (48, 64)
    assert image.dtype == np.uint8


def test_decode_invalid_bytes_raises():
    with pytest.raises(RuntimeError):
        decode_image(b"not an image")


def test_save_image_bytes_writes_timestamped_file(tmp_path):
    data = _synthetic_bmp()
    path = save_image_bytes(data, tmp_path / "captures")
    assert path.exists()
    assert path.name.startswith("cognex_") and path.suffix == ".bmp"
    assert path.read_bytes() == data
