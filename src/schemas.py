class User:
    def __init__(self, id: int, state: ..., general_progress: int,
                 test_progress: list[int], settings: dict[str, bool | int]):
        self._id = id
        self._state = state
        self._general_progress = general_progress
        self._test_progress = test_progress
        self._settings = settings
