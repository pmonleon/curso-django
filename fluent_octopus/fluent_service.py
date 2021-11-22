import os.path
from threading import Lock, Thread
from fluent.runtime import FluentLocalization, FluentResource, FluentResourceLoader
import os
from pathlib import Path
from django.utils.translation import get_language


class FluentMeta(type):
    """
    This is a thread-safe implementation of FluentService Singleton.
    """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class FluentService(metaclass=FluentMeta):
    """
    Fluent service
    """

    def __init__(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent

        print("base path", BASE_DIR)
        self._fluent_resource_loader = FluentResourceLoader(os.path.join(BASE_DIR, "fluent_octopus/l10n/{locale}"))
        self._localization = {
            "es": FluentLocalization(['es', 'en'], ["main.ftl"], self._fluent_resource_loader),
            "en": FluentLocalization(["en"], ["main.ftl"], self._fluent_resource_loader)
        }

    def get_l10n(self, locale) -> FluentLocalization:
        return self._localization[locale]


def test_singleton() -> None:
    singleton = FluentService()
    l10n = singleton.get_l10n("es")
    print("formatted welcome value", l10n.format_value("welcome"))


def translation(arg, arg1, arg2):
    print("calling translation with a ", arg, arg1, arg2, get_language())
    trans_service = FluentService()
    val = trans_service.get_l10n(get_language()).format_value(arg, {arg1 : arg2})
    return val

if __name__ == "__main__":
    process1 = Thread(target=test_singleton)

    # process2 = Thread(target=test_singleton)
    process1.start()
    # process2.start()
