
import mlflow
import mlflow.artifacts
import shutil

mlflow.set_tracking_uri("https://dagshub.com/anaelleplrt/my-dvc-project.mlflow")

models = mlflow.search_logged_models(
    experiment_ids=["0"],
    output_format="list"
)

models = [m for m in models if m.status.value == "READY"]

latest = max(models, key=lambda m: m.creation_timestamp)

path = mlflow.artifacts.download_artifacts(
    artifact_uri=latest.model_uri
)

shutil.copytree(path, "model", dirs_exist_ok=True)

print("Downloaded model:", latest.model_uri)
