# 01 · Project Overview

## Title

**Industrial Robot Self-Awareness Enhancement with Edge AI**

National Taiwan University of Science and Technology (NTUST). Academic advisor: Prof. Shu-Hao Liang. Academic period: October 2026 to July 2027 (tentative).

## Research problem

Industrial robots execute programmed trajectories repeatedly, but they usually have **no independent visual check** that the real motion or the handled workpiece behaves as expected. In the earlier wire-handling workcell, the team saw a misalignment issue while transferring the wire from the infeed toward the alignment area/tray. **Its root cause has not been established.**

This project investigates whether an **external fixed RGB camera** combined with **Edge AI** can:

1. learn the normal operating pattern of a repetitive robot cycle, and
2. detect controlled abnormal cycles with acceptable accuracy, latency and false-alarm rate.

## Scope

| In scope (core) | Optional extensions | Out of scope |
|---|---|---|
| Vision-based motion monitoring with one fixed camera | Multi-camera fusion | Consciousness or full robot state estimation |
| Spatial and temporal feature extraction | Deep-learning models | Replacing safety-rated protection systems |
| Structured normal / abnormal dataset | Automatic correction of the robot | Generating collisions as tests |
| Statistical vs. ML anomaly detection | Task-specific wire inspection | |
| Edge deployment and benchmarking | Anomaly-type classification | |

**Core deliverable:** an anomaly-detection prototype that has been validated in experiments.

Wire insertion is the motivating application. The method should generalize to pick-and-place, assembly, inspection, condition monitoring and quality control.

## Objectives

1. Develop a vision-based robot motion monitoring system.
2. Extract spatial and temporal features from RGB images.
3. Collect a structured dataset of normal and abnormal cycles.
4. Compare statistical and machine-learning anomaly-detection methods.
5. Evaluate positioning and repeatability within the measurement limits.
6. Explore real-time deployment on edge hardware.
7. Investigate feedback to robot control as exploratory future work.

## Research questions

- **RQ1.** Which visual features distinguish normal and abnormal robot cycles?
- **RQ2.** How do simple statistical baselines compare with machine-learning methods on the same features?
- **RQ3.** Can detection run on edge hardware with acceptable latency and false-alarm rate?
- **RQ4.** How robust is the approach across repetitions, sessions and controlled changes?

## Team responsibilities

| Member | Main workstream | Responsibilities |
|---|---|---|
| Esteban Gomez | Vision | Camera acquisition, calibration, ROI and tracking, feature generation, vision validation |
| Cristhian Guerreño | Robot | ABB calibration, reproducible RAPID programs, safe anomaly conditions, robot logs and interface |
| Ian Ruiz Diaz | AI / Edge | Dataset and model pipeline, statistical vs. ML comparison, edge deployment and benchmarking |
| All | Shared | Experimental protocol, labels, synchronization, Git workflow, integration, final report |
