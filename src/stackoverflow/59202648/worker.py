from typing import Any

Processor = Any


class Worker:
    _processor: Processor

    def set_processor(self, processor: Processor):
        self._processor = processor

    def start_work(self, data: bytes):
        self._processor.parse(data)
