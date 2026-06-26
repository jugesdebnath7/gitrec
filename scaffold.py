import logging
from pathlib import Path

PROJECT_ROOT = Path(".")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

project_tree = {
    "configs": ["config.yaml", "model_config.yaml"],
    "data/raw": [],
    "data/processed": [],
    "data/artifacts": [],
    "models/saved": ["__init__.py"],
    "models": ["__init__.py", "registry.json"],
    "src": ["__init__.py"],
    "src/simulation": ["__init__.py"],
    "src/db": ["__init__.py", "connection.py", "schema.sql", "repository.py"],
    "src/features": ["__init__.py", "feature_pipeline.sql", "feature_store.py"],
    "src/training": ["__init__.py", "dataset.py", "train_embedding.py", "train_ranker.py", "trainer.py"],
    "src/inference": ["__init__.py", "candidate_generator.py", "ranker.py", "service.py"],
    "src/api": ["__init__.py", "app.py"],
    "src/pipelines": ["__init__.py", "batch_pipeline.py", "training_pipeline.py"],
    "src/utils": ["__init__.py", "logger.py", "config_loader.py", "env_loader.py"],
    ".": [".env", "pyproject.toml", "docker-compose.yml", "requirements.txt", "README.md"]
}

for dir_path, files in project_tree.items():
    full_dir_path = PROJECT_ROOT / dir_path

    # Create directories
    if not full_dir_path.exists():
        logging.info(f"Creating directory: {full_dir_path}")
        full_dir_path.mkdir(parents=True, exist_ok=True)

    # Create files
    for file in files:
        file_path = full_dir_path / file
        if not file_path.exists():
            file_path.touch()    