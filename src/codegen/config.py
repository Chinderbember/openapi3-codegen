import yaml


def _get_config_dict(file_path: str) -> dict:
    with open(file_path) as stream:
        return yaml.safe_load(stream)


def _validate_config(config: dict) -> bool:
    # TODO: validate configuration fields (required, data types, etc)
    
    return True


def load_config(file_path: str) -> dict:
    data = _get_config_dict(file_path)

    if not _validate_config(data):
        raise ValueError("Invalid generator configuration")

    return data
