from __future__ import annotations

import os
from enum import Enum
from typing import Optional

import pytest


class Status(Enum):
    PASSED = 0
    FAILED = 1
    NOT_STARTED = 2

    def __bool__(self) -> bool:
        if self is Status.NOT_STARTED:
            if "PYTEST_CURRENT_TEST" in os.environ:
                pytest.skip("Not started")
        return self is not Status.FAILED

    @staticmethod
    def from_bool(value: Optional[bool]) -> Status:
        if value is None:
            return Status.NOT_STARTED
        if value:
            return Status.PASSED
        return Status.FAILED

    def __str__(self) -> str:
        if self is Status.PASSED:
            return "✅ " + self.name
        if self is Status.FAILED:
            return "❌ " + self.name
        if self is Status.NOT_STARTED:
            return "⏳ " + self.name
        return self.name
