from prometheus_client import Counter, Gauge
from enum import Enum

from .interface import Comm


class CounterComm(Comm):
    def __init__(self, counter: Counter):
        self._counter = counter

    def send(self, value: int = 1, **kwargs):
        self._counter.inc(value)


class GaugeComm(Comm):
    def __init__(self, counter: Counter):
        self._counter = counter

    def send(self, value: int = 1, **kwargs):
        self._counter.set(value)


def _wrap_metric(metric: Counter|Gauge) -> CounterComm|GaugeComm:
    if isinstance(metric, Counter):
        return CounterComm(metric)
    if isinstance(metric, Gauge):
        return GaugeComm(metric)
    raise ValueError(f"PrometheusComm expects either Counter or Gauge, not {metric.__class__.__name__}")


class PrometheusComm(Comm):
    def __init__(self, input: dict[Enum,Counter|Gauge], port: int = 8000):
        prometheus_client.start_http_server(port)
        self._metrics = {
            kind: _wrap_metric(metric)
            for kind, metric in input.items()
        }

    def send(self, *kinds: Enum, value: int = 1, **kwargs):
        for kind in kinds:
            self._metrics[kind].send(value, **kwargs)
