# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2024 Scipp contributors (https://github.com/scipp)
from collections.abc import Generator
from typing import Any, NewType, TypedDict

import numpy as np
from numpy.random import default_rng

# Configuration
EventRate = NewType("EventRate", int)  # [events/s]
FrameRate = NewType("FrameRate", int)  # [Hz]
NumFrames = NewType("NumFrames", int)  # [dimensionless]
DataFeedingSpeed = NewType("DataFeedingSpeed", float)  # [s/counts]

# Hard-coded Configuration
ReferenceTimeZero = NewType("ReferenceTimeZero", int)  # [ns]

# Arguments
DetectorName = NewType("DetectorName", str)
DetectorNumberCandidates = NewType("DetectorNumberCandidates", list[int])


class EV44(TypedDict):
    source_name: DetectorName
    reference_time: list[float] | np.ndarray
    reference_time_index: list[int] | np.ndarray
    time_of_flight: list[float] | np.ndarray
    pixel_id: list[int] | np.ndarray | None


RandomEV44Generator = Generator[EV44, Any, Any]


def random_ev44_generator(
    *,
    source_name: DetectorName,
    detector_numbers: DetectorNumberCandidates | None = None,
    event_rate: EventRate,
    frame_rate: FrameRate,
) -> Generator[EV44, Any, Any]:
    """Randomly select detector numbers (pixel ids) and generate events per frame."""
    rng = default_rng(123)
    ef_rate = int(event_rate / frame_rate)

    et_zero = ReferenceTimeZero(13620492 * 10**11)  # No reason
    while True:
        cur_event_number = int(
            ef_rate * (rng.integers(99, 101) / 100)
        )  # 1% of fluctuation
        yield EV44(
            source_name=source_name,
            reference_time=np.asarray([et_zero]),
            reference_time_index=np.asarray([0]),
            time_of_flight=(
                rng.random((cur_event_number,)) * 48_000_000 + 4_000_000
            ).astype("int32"),  # No reason
            pixel_id=(
                None
                if detector_numbers is None
                else rng.choice(detector_numbers, cur_event_number)
            ),
        )
        et_zero += int(1e9 / frame_rate)  # Move to next frame


def nxevent_data_ev44_generator(
    *,
    source_name: DetectorName,
    event_id: np.ndarray | None,
    event_index: np.ndarray,
    event_time_offset: np.ndarray,
    event_time_zero: np.ndarray,
) -> Generator[EV44, Any, Any]:
    """Generate EV44 from datasets of a NXevent_data group."""
    from itertools import pairwise

    for i, (start, end) in enumerate(pairwise(event_index)):
        yield EV44(
            source_name=source_name,
            reference_time=np.asarray(event_time_zero[i : i + 1]),
            reference_time_index=np.asarray([0]),
            time_of_flight=np.asarray(event_time_offset[start:end]),
            pixel_id=None if event_id is None else np.asarray(event_id[start:end]),
        )
