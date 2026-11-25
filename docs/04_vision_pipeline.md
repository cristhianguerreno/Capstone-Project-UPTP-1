# 04 · Vision Pipeline

Owner: **Esteban Gomez**

## Progress so far

- Introductory OpenCV learning. A beta object-tracking test was discussed; its code is not yet in the repository.
- **Cognex In-Sight camera discovered and images acquired** over FTP. The sample is in [`vision/`](../vision/README.md).
- Focus and exposure adjustments attempted. Focus looked better, but this was not measured.
- Working distance for the earlier close-up wire inspection: about **15 cm**.
- Exposure below about **8 ms** made the image appear intermittently. **The cause is unverified.** Candidates to investigate: illumination flicker, trigger settings, exposure and acquisition mode.

> No tracker accuracy or other measured performance has been established yet.

## Camera capabilities to verify

- [ ] Exact model and label. Is the sensor color or monochrome?
- [ ] Maximum frame rate at the required resolution
- [ ] Lens / optics and field of view at the chosen working distance
- [ ] Image export options: FTP, continuous streaming, SDK, triggering
- [ ] Licensing and controller options
- [ ] Latency of FTP download + decode, measured by `cognex_ftp_capture.py`

## Recommended sequence

1. **Acquisition.** Verify acquisition and save timestamped frames. ✅ First step done.
2. **Mount.** Choose a fixed camera mount with a clear field of view, controlled lighting and a repeatable setup.
3. **Intrinsic calibration.** Use a checkerboard or other suitable target. Record the intrinsic matrix, distortion coefficients, reprojection error and setup ID.
4. **ROI and references.** Define the region of interest and physical reference points.
5. **Tracking.** Start simple: a fiducial marker (e.g. ArUco) on a rigid visible part, segmentation, contours or optical flow. Use a detector such as YOLO only if simple tracking is not enough.
6. **Features.** Extract coordinates, orientation, area, confidence and timestamps.
7. **Synchronization.** Align the vision data with the robot cycle.
8. **Validation.** Check repeatability and tracking robustness.
9. **Dataset.** Generate the dataset (see [05](05_dataset_and_experiments.md)).
10. **Integration.** Connect to the anomaly model and run benchmarks (see [06](06_anomaly_detection_and_edge.md)).

## Geometric limitations

- A single fixed camera measures **image-plane motion** (pixels).
- A calibrated **planar homography** can recover physical coordinates (mm) on one plane.
- Arbitrary 3D pose or the absolute TCP position **cannot be observed** from pixels alone. That needs extra geometric assumptions, known markers or other sensors.
- Occlusion, perspective and depth changes must be reported as limitations.
- **Extrinsic calibration** is needed to relate image observations to robot coordinates. Recalibrate whenever the camera geometry changes.

## Candidate features

x/y trajectory, displacement, apparent speed, acceleration (after smoothing), orientation, cycle duration, phase duration, trajectory deviation, ROI area, detection confidence.

Always distinguish a **tracking failure**, where the vision system lost the target, from a **motion anomaly**, where the robot really behaved differently.
