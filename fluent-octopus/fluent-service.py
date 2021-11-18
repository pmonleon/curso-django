from threading import Lock, Thread
from fluent.runtime import  FluentLocalization, FluentResource


class FluentMeta(type):
    """
    This is a thread-safe implementation of FluentService Singleton.
    """
    _fluent_resource_loader = FluentResource('l10n/{locale}')
    _localization = {
        "es": FluentLocalization(["es", "en"], ["main.flt"], _fluent_resource_loader),
        "en": FluentLocalization(["en", "es"], ["main.flt"], _fluent_resource_loader)
    }
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
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def get_text(self):
        """
        Here we'll get the messages
        """


def test_singleton(value: str) -> None:
    singleton = FluentService(value)
    print(singleton.value)


if __name__ == "__main__":
    # The client code.

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (bad!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
