from .utilities.datasets import DATASETS
from .setup import setup

setup.setup = setup # for backward compatibility  # type: ignore

__all__ = ["DATASETS", "setup"]
