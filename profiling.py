import time


class ProfilingContext:
    data = {}
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        duration = end_time - self.start_time
        ProfilingContext.data.setdefault(self.name, []).append(duration)

    @classmethod
    def print_summary(cls):
        for name, data in cls.data.items():
            print('{}: {}s avg for {} calls'.format(name, sum(data)/len(data), len(data)))


with ProfilingContext('test'):
    time.sleep(1)

ProfilingContext.print_summary()
