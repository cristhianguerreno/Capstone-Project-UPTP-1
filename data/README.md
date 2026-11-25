# Data

**Raw images, videos and large datasets are NOT committed to Git.** Keep them on shared storage (e.g. a team drive). Document their location and version here.

## Layout (local, git-ignored)

```
data/
├── raw/          # original images / videos / robot logs, never modified
│   └── cognex_captures/
├── interim/      # intermediate outputs (tracking results)
└── processed/    # feature tables used for training / evaluation
```

## Schema

See the data schema in [05 · Dataset and experiments](../docs/05_dataset_and_experiments.md#data-schema).

## Dataset registry

| Dataset ID | Date | Sessions | Cycles (normal / abnormal) | Camera config | Location | Notes |
|---|---|---|---|---|---|---|
| *(none yet)* | | | | | | |
