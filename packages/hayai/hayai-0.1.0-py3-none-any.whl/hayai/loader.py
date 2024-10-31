from dataclasses import dataclass
import os
from queue import Queue
from typing import Callable
from multiprocess.pool import Pool


@dataclass
class Loader:
    func: Callable
    workers: int = 2 * os.cpu_count() or 8
    queue_size: int = 2 * os.cpu_count() or 8

    def __post_init__(self):
        self.__pool = Pool(self.workers)
        self.__queue = Queue(self.queue_size)

        for _ in range(self.queue_size):
            self.__queue.put(self.__pool.apply_async(self.func))

    def __call__(self):
        result = self.__queue.get().get()
        self.__queue.put(self.__pool.apply_async(self.func))
        return result
