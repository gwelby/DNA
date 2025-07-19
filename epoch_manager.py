#!/usr/bin/env python3
"""Epoch Manager – 𝛷^𝛷 Cycle Automation

Usage:
  python epoch_manager.py new           # create new epoch folder based on template
  python epoch_manager.py retro         # generate Retro.md in current epoch
  python epoch_manager.py status        # print today’s frequency reminder

An epoch folder is named EPOCH_<YYYY-MM-DD> in the project root.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import os
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = PROJECT_ROOT / "EPOCH_TEMPLATE"
DATE_FMT = "%Y-%m-%d"

# Simple 7-day frequency ladder map (Mon-Sun)
_FREQ_ORDER = [
    ("OBSERVE", 432),     # Monday
    ("CREATE", 528),      # Tuesday
    ("INTEGRATE", 594),   # Wednesday
    ("HARMONIZE", 672),   # Thursday
    ("TRANSCEND", 720),   # Friday
    ("CASCADE", 768),     # Saturday
    ("INFINITE", 963),    # Sunday
]


def today_frequency() -> tuple[str, float]:
    weekday = _dt.datetime.now().weekday()  # 0=Mon
    return _FREQ_ORDER[weekday]


def copy_template(epoch_dir: Path) -> None:
    """Copy template tree to destination."""
    if epoch_dir.exists():
        print(f"⚠️  Epoch directory {epoch_dir} already exists.")
        return
    shutil.copytree(TEMPLATE_DIR, epoch_dir)
    print(f"✅ Copied template to {epoch_dir}")

    # Stamp dates in Goals.md & Retro.md placeholders
    goals = epoch_dir / "Goals.md"
    retro = epoch_dir / "Retro.md"
    date_str = _dt.datetime.now().strftime(DATE_FMT)
    _replace_in_file(goals, "<start>", date_str)
    _replace_in_file(retro, "<start>", date_str)
    _replace_in_file(retro, "<end>", "<pending>")

    # Add first logbook row
    state, _freq = today_frequency()
    logbook = epoch_dir / "Logbook.csv"
    with logbook.open("a", encoding="utf-8") as f:
        f.write(f"{date_str},{state},,,,")
    print("📝 Initialized Logbook first row")


def _replace_in_file(path: Path, needle: str, replacement: str):
    txt = path.read_text(encoding="utf-8")
    path.write_text(txt.replace(needle, replacement), encoding="utf-8")


def create_retro(epoch_dir: Path):
    retro = epoch_dir / "Retro.md"
    if retro.exists():
        print("Retro.md already exists – nothing to do.")
    else:
        shutil.copy(TEMPLATE_DIR / "Retro.md", retro)
        _replace_in_file(retro, "<start>", epoch_dir.name.replace("EPOCH_", ""))
        _replace_in_file(retro, "<end>", _dt.datetime.now().strftime(DATE_FMT))
        print("✅ Retro.md created.")


def print_status():
    state, freq = today_frequency()
    print(f"📅 Today’s Frequency → {state} {freq:.0f} Hz")


def main(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(description="Epoch manager for φ-cycles")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("new", help="Create new epoch from template")
    sub.add_parser("retro", help="Generate retro in current epoch")
    sub.add_parser("status", help="Show today’s frequency state")

    args = parser.parse_args(argv)

    if args.cmd == "status":
        print_status()
        return

    # determine latest/target epoch dir
    today = _dt.datetime.now().strftime(DATE_FMT)
    epoch_dir = PROJECT_ROOT / f"EPOCH_{today}"

    if args.cmd == "new":
        copy_template(epoch_dir)
        print_status()
    elif args.cmd == "retro":
        # Assume retro for most recent epoch (latest dir)
        epochs = sorted(PROJECT_ROOT.glob("EPOCH_*"))
        if not epochs:
            print("No epoch directories found.")
            return
        create_retro(epochs[-1])
    else:
        parser.error("Unhandled command")


if __name__ == "__main__":
    main()
