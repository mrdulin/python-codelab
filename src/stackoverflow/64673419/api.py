import gcsfs

PROJECT = "teresa.teng"


def download_models(gcs_model_path, local_path):
    filesystem = gcsfs.GCSFileSystem(project=PROJECT)
    filesystem.get(gcs_model_path, local_path, recursive=True)
