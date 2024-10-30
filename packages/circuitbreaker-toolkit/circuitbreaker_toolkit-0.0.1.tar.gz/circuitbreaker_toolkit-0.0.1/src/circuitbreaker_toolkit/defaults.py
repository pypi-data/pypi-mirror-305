# SPDX-FileCopyrightText: © 2024 David E. James
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

import time


class Defaults:
    TIME_FUNC              = time.time
    BREAKER_FACTORY        = None
    BREAKER_OPEN_TIME      = 30.0
    BREAKER_OPEN_THRESHOLD = 5.0
    FORGIVENESS            = 1.0


