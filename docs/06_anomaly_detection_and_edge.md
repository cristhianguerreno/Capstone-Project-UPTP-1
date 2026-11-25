# 06 · Anomaly Detection and Edge Deployment

Owner: **Ian Ruiz Diaz**

Status: **proposed**. No algorithm has been selected and no model has been trained.

## Methods to compare

All methods are compared fairly on the **same features** and the **same held-out cycles**.

| Level | Method | Why |
|---|---|---|
| Baseline 1 | Reference trajectory with mean ± k·std, or robust median / MAD thresholds | Simple and interpretable |
| Baseline 2 | Multivariate distance (e.g. Mahalanobis) or trajectory residual | Uses correlations between features |
| ML | Isolation Forest, One-Class SVM | Learn from normal data only |
| Optional | Autoencoder or temporal model | Only if the dataset size and timeline justify it |

Rules:
- Define the anomaly score and the threshold **before** evaluating on the test set.
- **Detection** (normal vs. abnormal) is the core task. **Classification** of anomaly types is optional and needs enough labeled data.
- Prefer interpretable baselines.

## Edge deployment plan

1. Build and validate the full pipeline on a PC first.
2. Export a lightweight model if needed.
3. Benchmark on the selected edge device with the **real camera stream and preprocessing**.
4. Measure:
   - end-to-end latency,
   - throughput / FPS,
   - CPU, GPU and memory load,
   - long-run stability.

> Real-time requirements must come from the **robot cycle time and the decision deadline**. FPS alone does not prove real-time performance.

## Output interface (proposed)

| Field | Description |
|---|---|
| `cycle_id` | Cycle being evaluated |
| `timestamp` | Decision time |
| `score` | Anomaly score |
| `status` | `normal` / `anomaly` / `tracking_failure` |
| `confidence` | Confidence of the decision |
| `heartbeat` | Liveness signal for the monitoring system |
