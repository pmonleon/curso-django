from threading import Lock, Thread
from fluent.runtime import FluentLocalization, FluentResource


class FluentMeta(type):
    """
    This is a thread-safe implementation of FluentService Singleton.
    """

    _instances = {}
    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
                # todo: we'll need to create a Fluent class for each of the languages
        return cls._instances[cls]


class FluentService(metaclass=FluentMeta):

    def __init__(self) -> None:
        self._fluent_resource_loader = FluentResource('/l10n/{locale}')
        print("fluent resource loader", self._fluent_resource_loader)
        self._localization = {
            "es": FluentLocalization(["es", "en"], ["main.flt"], self._fluent_resource_loader),
            "en": FluentLocalization(["en"], ["main.flt"], self._fluent_resource_loader)
        }
        # print("localisation", self._localization)

    def get_l10n(self, locale) -> FluentLocalization:
        print("localization llamada", self._localization[locale])
        return self._localization[locale]


def test_singleton() -> None:
    singleton = FluentService()
    l10n = singleton.get_l10n("es")
    print("formatted welcome value", l10n.format_value("welcome"))


if __name__ == "__main__":
    process1 = Thread(target=test_singleton)
    process2 = Thread(target=test_singleton)
    process1.start()
    process2.start()
