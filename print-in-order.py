from threading import Lock


class Foo:
    def __init__(self):

        self.locks = [Lock(), Lock()]
        self.locks[0].acquire()  # Lock for second()
        self.locks[1].acquire()  # Lock for third()
        pass

    def first(self, printFirst: "Callable[[], None]") -> None:
        printFirst()
        self.locks[0].release()  # Release lock for second()

    def second(self, printSecond: "Callable[[], None]") -> None:
        with self.locks[0]:
            printSecond()
            self.locks[1].release()  # Release lock for third()

    def third(self, printThird: "Callable[[], None]") -> None:
        with self.locks[1]:
            printThird()
