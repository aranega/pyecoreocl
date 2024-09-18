from .main import preprocess as main_preprocess

__all__ = ["preprocess"]


def preprocess(data: str):
    return main_preprocess(data, "strict")