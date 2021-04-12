from argparse import ArgumentParser, Namespace

from openapi_parser import parse

from . import __title__
from .config import load_config
from .generator import generate, GenerationError
from .logger import logger


def get_arguments() -> Namespace:
    parser = ArgumentParser(__title__)

    parser.add_argument('--swagger', required=True, help='path to OpenAPI file', metavar='path')
    parser.add_argument('--config', required=True, help='path to generator config (*.yml)', metavar='path')

    return parser.parse_args()


def run() -> None:
    args = get_arguments()

    try:
        config = load_config(args.config)
        specification = parse(args.swagger)

        generate(specification, config)
    except FileNotFoundError as error:
        logger.error(f"{error.strerror}: {error.filename}")
    except LookupError as error:
        logger.error(error.args[2])
    except GenerationError as error:
        logger.error(f"Generation error: {error}")


if __name__ == '__main__':
    # python -m codegen --config tests/data/config.yml --swagger tests/data/swagger.yml
    run()
