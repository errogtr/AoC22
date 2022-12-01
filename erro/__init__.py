from pathlib import Path


def get_data_path(fpath: str) -> str:
    return Path(fpath).stem + "_data"

