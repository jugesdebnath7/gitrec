# scaffold.py

import os
from pathlib import Path
import argparse

# ----------------------------
# CONFIG
# ----------------------------

PROJECT_NAME = "gitrec"

STRUCTURE = {
    "src": {
        PROJECT_NAME: {
            "ingestion": {
                "github": [
                    "client.py",
                    "loader.py",
                    "rate_limiter.py",
                ]
            },
            "mapper": {
                "schemas": [
                    "repo.py",
                    "user_event.py",
                ],
                "__files__": [
                    "repo_mapper.py",
                    "event_mapper.py",
                ]
            },
            "storage": {
                "__files__": ["db.py", "session.py"],
                "models": [
                    "repo_model.py",
                    "user_model.py",
                    "user_event_model.py",
                    "feature_model.py",
                ],
                "repositories": [
                    "repo_repository.py",
                    "user_repository.py",
                    "event_repository.py",
                    "feature_repository.py",
                ],
                "migrations": {}
            },
            "features": {
                "pipelines": [
                    "repo_features.py",
                    "user_features.py",
                ],
                "sql": [],
                "transformers": [
                    "feature_utils.py",
                ],
                "__files__": ["feature_store.py"],
            },
            "models": {
                "__files__": ["base.py"],
                "candidate_generation": [
                    "popularity.py",
                    "user_cf.py",
                    "item_cf.py",
                    "embedding_model.py",
                ],
                "ranking": [
                    "heuristic_ranker.py",
                    "lightgbm_ranker.py",
                    "nn_ranker.py",
                ],
                "hybrid": [
                    "hybrid_model.py",
                ],
            },
            "training": [
                "dataset.py",
                "trainer.py",
                "evaluator.py",
                "registry.py",
            ],
            "serving": [
                "api.py",
                "inference.py",
                "ranking.py",
                "cache.py",
            ],
            "monitoring": [
                "data_quality.py",
                "drift_detection.py",
                "metrics.py",
            ],
            "core": [
                "config.py",
                "logging.py",
                "constants.py",
                "exceptions.py",
            ],
            "utils": [
                "time_utils.py",
                "hashing.py",
            ],
        }
    },
    "scripts": [
        "ingest_github.py",
        "build_features.py",
        "train_model.py",
        "evaluate_model.py",
        "backfill.py",
    ],
    "tests": [
        "test_mapper.py",
        "test_features.py",
        "test_models.py",
    ],
    "configs": [
        "model_config.yaml",
        "feature_config.yaml",
    ],
    "artifacts": [],
}


# ----------------------------
# FILE TEMPLATES
# ----------------------------

TEMPLATES = {
    "__init__.py": "",
    "client.py": """class GitHubClient:
    def __init__(self):
        pass
""",
    "trainer.py": """def train():
    print("Training started...")
""",
    "api.py": """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
""",
}


# ----------------------------
# CORE FUNCTIONS
# ----------------------------

def create_file(path: Path, content: str = ""):
    if not path.exists():
        path.write_text(content)
        print(f"[FILE] {path}")


def ensure_init(path: Path):
    init_file = path / "__init__.py"
    if not init_file.exists():
        init_file.touch()


def build_structure(base_path: Path, structure):
    if isinstance(structure, dict):
        for name, content in structure.items():
            if name == "__files__":
                for file in content:
                    file_path = base_path / file
                    template = TEMPLATES.get(file, "")
                    create_file(file_path, template)
                continue

            new_dir = base_path / name
            new_dir.mkdir(parents=True, exist_ok=True)
            ensure_init(new_dir)

            build_structure(new_dir, content)

    elif isinstance(structure, list):
        for file in structure:
            file_path = base_path / file
            template = TEMPLATES.get(file, "")
            create_file(file_path, template)


# ----------------------------
# MAIN
# ----------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-name", default=PROJECT_NAME)
    args = parser.parse_args()

    root = Path.cwd()

    print(f"Scaffolding project: {args.project_name}")

    build_structure(root, STRUCTURE)

    # root files
    create_file(root / "README.md", f"# {args.project_name}\n")
    create_file(root / "requirements.txt")
    create_file(root / "Dockerfile")

    print("\nDone.")


if __name__ == "__main__":
    main()