"""Minimal Prometheus exporter for epoch logbook metrics.
Run:  python coherence_exporter.py --port 8000
Then scrape http://localhost:8000/metrics
"""
from __future__ import annotations

import csv
import argparse
import pathlib
import time

from typing import Dict, Tuple

from prometheus_client import start_http_server, Gauge

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent
LOG_GAUGE: Dict[str, Gauge] = {}


def get_metric(epoch: str, metric: str) -> Gauge:
    key = f"{metric}_{epoch}"
    if key not in LOG_GAUGE:
        LOG_GAUGE[key] = Gauge(f"{metric}", f"{metric} score", ["epoch"])
    return LOG_GAUGE[key]


def tail_logbooks() -> None:
    for log in PROJECT_ROOT.glob("EPOCH_*/Logbook.csv"):
        epoch = log.parent.name.replace("EPOCH_", "")
        try:
            with log.open(newline="", encoding="utf-8") as fh:
                last: Tuple[str, ...] | None = None
                for row in csv.reader(fh):
                    if row and not row[0].startswith("#"):
                        last = tuple(row)
                if last and len(last) >= 5:
                    _, _state, coherence, creativity, insight, *_ = last + ("", "", "")  # pad
                    _update_gauge(epoch, "coherence_score", coherence)
                    _update_gauge(epoch, "creativity_score", creativity)
                    _update_gauge(epoch, "insight_score", insight)
        except FileNotFoundError:
            continue


def _update_gauge(epoch: str, name: str, val: str):
    try:
        v = float(val) if val else 0.0
    except ValueError:
        v = 0.0
    g = get_metric(epoch, name)
    g.labels(epoch=epoch).set(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8000, help="Port to expose metrics")
    args = ap.parse_args()

    start_http_server(args.port)
    print(f"🚀 Coherence exporter running on :{args.port}/metrics")

    try:
        while True:
            tail_logbooks()
            time.sleep(30)
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()
