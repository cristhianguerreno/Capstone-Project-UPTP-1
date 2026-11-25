# Vision

Owner: **Esteban Gomez** · Documentation: [04 · Vision pipeline](../docs/04_vision_pipeline.md)

| Path | Content |
|---|---|
| `cognex/cognex_ftp_capture.py` | Command-line tool that downloads the current image from a Cognex In-Sight camera over FTP |
| `notebooks/cognex_ftp_capture.ipynb` | Original working sample notebook (same logic, interactive) |

## Cognex FTP capture

The camera exposes its current image as `image.bmp` on its FTP server (port 21). The script **downloads** that image. **It does not trigger a new acquisition.**

```bash
python vision/cognex/cognex_ftp_capture.py --show
```

| Option | Default | Description |
|---|---|---|
| `--ip` | `$COGNEX_IP` or prompt | Camera IP address |
| `--user` | `$COGNEX_USER` or prompt | Camera username |
| *(password)* | `$COGNEX_PASSWORD` or hidden prompt | Never passed on the command line |
| `--remote-file` | `image.bmp` | File to download from the camera |
| `--output-dir` | `data/raw/cognex_captures` | Where timestamped copies are saved (git-ignored) |
| `--count` | `1` | Number of downloads |
| `--interval` | `1.0` | Seconds between downloads |
| `--show` | off | Display the last image |

Each download prints the image shape and the **download + decode time** in ms. This is useful for checking whether FTP is fast enough for tracking.

### Security
- FTP sends credentials in plain text. Use it only on the isolated lab network.
- **Never commit** the camera IP address, username or password. Set them as environment variables in your own terminal session instead.

### Known limitations / to verify
- Repeated capture (`--count > 1`) has not been validated on the real camera.
- The image is decoded as grayscale. Check whether the sensor is color or monochrome.
- For video-rate tracking, investigate the camera's streaming or SDK options, or use another RGB camera.
