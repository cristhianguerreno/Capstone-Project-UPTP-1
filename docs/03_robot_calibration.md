# 03 · Robot Control and Calibration

Owner: **Cristhian Guerreño**

## Proposed calibration sequence

1. **Check mastering and calibration status** of the IRB 1090 (revolution counters, calibration data).
2. **Determine the TCP** accurately, using a multi-point TCP definition with a reference pin.
3. **Configure `tooldata` and `loaddata`** consistently with the real gripper and payload.
4. **Define a `wobjdata` (workobject)** on a physical reference fixture with accessible reference points. Do not try to locate the theoretical base origin, which cannot be reached.
5. **Evaluate repeatability and absolute positioning** (see the tests below).
6. **Investigate ABB Absolute Accuracy**: availability, license and calibration requirements. It is *not* a simple software toggle and *not* a substitute for TCP calibration.
7. **Then calibrate the camera** (see [04 · Vision pipeline](04_vision_pipeline.md)).

Use the manufacturer's procedures, qualified supervision and suitable measurement tools.

## Coordinate frames

| Frame | Defined by | Notes |
|---|---|---|
| World | Lab / cell | Optional common reference |
| Base | Robot base | Fixed by the robot installation |
| Workobject | Physical fixture reference points | Main frame for programmed targets |
| Tool (TCP) | Gripper tooldata | Must be recalibrated if the gripper changes |
| Camera | Camera extrinsics | Comes from camera calibration |
| Image | Pixels (u, v) | Comes from camera intrinsics |

**Units:** mm, degrees, seconds. Every transformation between frames must be documented in `configs/`.

> The pose reported by the robot is a useful **reference**. It is **not independent ground truth** for real positioning accuracy.

## Proposed robot tests

| Test | Purpose |
|---|---|
| Repeated returns to reference poses | Repeatability |
| Approach from different directions | Backlash and approach-direction effects |
| Positioning error measured independently (gauge, camera, pin) | Accuracy |
| Different loads and speeds | Consistency |
| Repeated execution of the same trajectory | Baseline for the anomaly dataset |

## Safety rules

- Use safe taught points, speed limits, clearance and collision checks, and work under lab supervision.
- **Never** cause collisions on purpose or override safety functions.
- Anomalies are created only as **small, predefined, safe deviations**. See [05 · Dataset and experiments](05_dataset_and_experiments.md).

## Historical RAPID code

See [`robot/rapid/README.md`](../robot/rapid/README.md). The earlier code fragments (a socket server and step-wise joint-6 motion) are **historical references, not validated programs**.
