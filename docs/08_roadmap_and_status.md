# 08 · Roadmap and Status

Last updated: **2026-11-25**

## Timeline (tentative)

| Period | Goals |
|---|---|
| **Oct – Nov 2026** | Literature review, workcell setup, calibration planning, first camera tests, baseline robot programs |
| **Dec 2026** | Choose the observable task. Camera acquisition and tracking. Dataset pilot. First baseline detection. |
| **Jan 2027** | 🎯 **Functional integrated monitoring / anomaly-detection prototype** (minimum scope) |
| **Feb – Jun 2027** | Controlled experiments, method comparison, edge benchmark, analysis, documentation, advisor review |
| **By Jul 1, 2027** | Final defense (tentative) |

The January target must be met with the **minimum scope** before any optional correction work starts.

## Status snapshot

### Confirmed / reported
- Project identity, team and advisor
- ABB IRB 1090 platform with RobotStudio / RAPID
- Cognex camera access and image acquisition over FTP (sample code in `vision/`)
- Preliminary focus and exposure adjustments (qualitative)
- Historical RAPID socket sample reviewed
- Calibration and experimental methodology discussed
- Wire-insertion workcell concept with two cameras discussed (see [meeting notes](meeting-notes/2026-11-25_whiteboard_session.md))

### Not yet confirmed
- Completed robot calibration and measured positioning errors
- Camera color capability and streaming compatibility
- Final camera mount and number of cameras
- Chosen task trajectory
- Synchronized acquisition between robot and camera
- Final gripper
- Labeled dataset, trained model, selected edge hardware
- Verified robot ↔ PC communication
- Completed prototype or automatic correction

## Immediate priorities

1. [ ] Agree on the **minimum monitoring experiment** with the advisor
2. [ ] Check the camera's streaming and hardware capabilities (model label, color/mono, FPS)
3. [ ] Select a **fixed viewpoint** and a **simple repeatable motion**
4. [ ] Establish robot references (TCP, workobject) and camera references
5. [ ] Define the shared **data schema** and cycle synchronization
6. [ ] Capture **pilot normal cycles**
7. [ ] Validate tracking
8. [ ] Introduce **safe controlled deviations**
9. [ ] Compare the baseline and ML detectors
10. [ ] Demonstrate the monitoring prototype

## Open questions

- Which visible rigid part should be tracked? Should a fiducial marker be added?
- Should cycle synchronization use controller signals (digital I/O or socket), or vision-only event detection?
- Can the Cognex camera deliver frames fast enough for per-frame tracking, or is a different RGB camera needed?
- Which edge hardware should be used?
- What is the cause of the intermittent images at exposures below 8 ms?
