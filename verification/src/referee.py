from checkio_referee import RefereeCodeGolf

import settings
import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    BASE_POINTS = 25
    DEFAULT_MAX_CODE_LENGTH = 250
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "golf"
