from checkio_referee import RefereeCodeGolf


import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    BASE_POINTS = 10
    DEFAULT_MAX_CODE_LENGTH = 350
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
