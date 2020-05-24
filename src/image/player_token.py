from typing import Tuple
from src.image.play_token_image_processor import TokenImageProcessor, DEFAULT_TOKEN_FRAME_FILE


class Token(TokenImageProcessor):
    def __init__(self, name: str, position: Tuple[int, int], image_url: str, square_size: int, server_id: str,
                 frame_url: str = DEFAULT_TOKEN_FRAME_FILE):
        super().__init__(name, position, image_url, square_size, server_id, frame_url)

    @property
    def name(self) -> str:
        return self._name

    @property
    def url(self) -> str:
        return self._url

    @property
    def position(self) -> Tuple[int, int]:
        return self._position

    @position.setter
    def position(self, value: Tuple[int, int]):
        self._position = value

    @property
    def frame_url(self) -> str:
        return self._frame_url

    @frame_url.setter
    def frame_url(self, value):
        self._frame_url = value

    def increment_position(self, x: int = 0, y: int = 0):
        self._position = (self._position[0] + x, self.position[1] + y)