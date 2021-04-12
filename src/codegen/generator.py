from openapi_parser.specification import Specification

from .logger import logger


class GenerationError(Exception):
    pass


def generate(specification: Specification, config: dict) -> None:
    logger.info(f"OpenAPI: {specification.version}")
    logger.info(f"Config: {config}")
    """
    Processing:
    - generate necessary directories
    - generate necessary files
    - copy simple files w/o template replacements
    - copy files with replacements
    - custom generators for application (aiohttp example)
    """
