# 05 · Dataset and Experimental Design

Status: **proposed**. No data has been collected yet.

## Unit of analysis

One **complete robot motion cycle**.

Start with:
- one simple, repeatable trajectory,
- a fixed payload,
- fixed illumination,
- a fixed camera mount.

Start and end events are defined with controller signals or timestamped events where possible.

## Conditions

### Normal cycles
Repeated across several sessions under documented nominal conditions. Natural variation is included so that false alarms can be measured.

### Abnormal cycles (safe, predefined)
| Anomaly type | Example |
|---|---|
| Position offset | Small programmed offset of a target, within verified safe bounds |
| Timing / speed | Altered speed or added dwell time |
| Workpiece | Controlled misalignment of the wire or part |

Rules:
- **Never** generate a collision.
- Vary **one factor at a time** at first.
- Justify severity levels by the measurement resolution and the task tolerances.
- Camera occlusion and lighting changes are **perception robustness tests**. They are not robot-motion anomalies and get their own labels.

### Pilot sample size (suggested, not final)
20–30 normal cycles, plus 10–20 cycles per safe anomaly condition. Refine these numbers after seeing the real variability.

## Data schema

One row per frame. Cycle-level features are derived from it.

| Field | Type | Description |
|---|---|---|
| `cycle_id` | str | Unique cycle identifier |
| `session_id` | str | Recording session (day / setup) |
| `timestamp` | float / ISO | Acquisition time |
| `frame_index` | int | Frame number within the cycle |
| `robot_program` | str | RAPID program / version |
| `phase` | str | Cycle phase (e.g. pick, transfer, place) |
| `condition_label` | str | `normal` or `abnormal`. This is the **applied** condition, never the model's output. |
| `anomaly_type` | str | e.g. `offset_x`, `speed`, `misalignment`, `none` |
| `severity` | str / float | Magnitude of the applied deviation |
| `camera_config_id` | str | Camera setup / calibration ID |
| `x_px`, `y_px` | float | Tracked image coordinates |
| `angle_deg` | float | Tracked orientation |
| `confidence` | float | Tracking confidence |
| `robot_pose` | optional | Robot-reported pose |
| `latency_ms` | float | Processing latency |
| `missing` | bool | Missing-data / tracking-failure flag |

## Avoiding data leakage

- Split by **complete cycle**, and preferably by **session**. Never split randomly by individual frames.
- Fit preprocessing, normalization, thresholds and models **only on training data**. Tune on validation data and keep an independent test set.
- Store raw data separately from processed features.
- Version the scripts, configuration, dataset schema and experiment logs.

## Time alignment

Options: phase normalization, interpolation or dynamic time warping. **Keep the duration features**, so that alignment does not erase timing anomalies.

## Where data lives

See [`data/README.md`](../data/README.md) and [`experiments/README.md`](../experiments/README.md).
