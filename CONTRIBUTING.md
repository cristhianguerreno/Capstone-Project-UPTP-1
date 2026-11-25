# Contributing · Team conventions

## Git workflow
1. Pull the latest `main` before starting: `git pull origin main`.
2. Create a branch per task: `feature/<area>-<short-name>` (e.g. `feature/vision-aruco-tracking`).
3. Make small commits with clear messages in English. Example: `vision: add ArUco tracker for gripper marker`.
4. Open a Pull Request to `main`. At least one teammate reviews it.
5. Never commit credentials, lab network details or large raw data.

## Where things go
| Area | Folder | Owner |
|---|---|---|
| Robot programs | `robot/rapid/` | Cristhian |
| Vision code | `vision/` | Esteban |
| AI models | `ai/` | Ian |
| Edge deployment | `edge/` | Ian |
| Experiment protocols and logs | `experiments/` | All |
| Meeting notes | `docs/meeting-notes/YYYY-MM-DD_topic.md` | All |

## Writing rules
- All repository content is written in **English**.
- Separate **facts / measured results** from **plans / assumptions**. Never report a number that was not measured.
- Record units (mm, degrees, seconds, px) everywhere.
- Update `docs/08_roadmap_and_status.md` when a milestone changes.
