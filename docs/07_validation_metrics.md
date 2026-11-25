# 07 · Validation Metrics

No numeric results have been established yet. This file defines **how** results will be measured and reported.

## Motion and vision

| Metric | Unit | Notes |
|---|---|---|
| Positioning error | mm | Only with a calibrated physical measurement |
| Image tracking error | px | Compared against manual annotation or a marker |
| Trajectory RMSE | px or mm | Against the reference trajectory |
| Repeatability / spread | px or mm | Over repeated cycles |
| Cycle duration variability | s | Std / IQR of cycle and phase durations |

## Anomaly detection

TP, FP, TN and FN are counted per cycle. Abnormal is the positive class.

| Metric | Formula |
|---|---|
| Precision | TP / (TP + FP) |
| Recall | TP / (TP + FN) |
| F1 | 2·P·R / (P + R) |
| False-positive rate | FP / (FP + TN) |
| Accuracy | (TP + TN) / N |

Also report the **confusion matrix**, and optionally **PR-AUC / ROC-AUC**.

## Timing and edge performance

- **Detection latency**: measured from the defined anomaly onset, or from the cycle start.
- Throughput / FPS.
- CPU, GPU and memory usage on the edge device.

## Reporting checklist

- [ ] Sample sizes (cycles and sessions) for each split
- [ ] How the threshold was selected, using validation data only
- [ ] Uncertainty / variation across sessions or repeated runs
- [ ] Per-cycle and (if used) per-frame results reported separately
- [ ] Failure examples, both false positives and false negatives
- [ ] Limits of generalization
