import os
import threading


class Register(object):
    @classmethod
    def add_process_async(cls, pid: int, name: str):
        with open('/tmp/worker', 'w') as f:
            f.write(str(pid) + '$$' + name)

    @classmethod
    def register_async(cls, pid: int, name: str):
        t = threading.Thread(target=cls.add_process_async, args=(pid, name))
        t.start()

    @classmethod
    def add_process(cls, pid: int, name: str):
        with open('/tmp/worker', 'w') as f:
            f.write(str(pid) + '$$' + name)

    @classmethod
    def unregister_process(cls, pid: int):
        with open('/tmp/worker', 'w') as f:
            f.write(str(-1*pid))

    @classmethod
    def auto_register(cls, name: str):
        pid = os.getpid()
        cls.add_process(pid, name)

    @classmethod
    def async_auto_register(cls, name: str):
        pid = os.getpid()
        cls.register_async(pid, name)

    @classmethod
    def auto_unregister(cls):
        pid = os.getpid()
        cls.unregister_process(pid)
