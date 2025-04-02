from datetime import datetime, timezone
from random import choice

DEFAULT_CHARACTERS = 'acdefghijkmnpqrtuvwxyzACEFGHJKLMNPQRTUVWXYZ2346789-_'

def ruid(length=10, fully_random=False) -> str:
    if length < 8 or fully_random:
        return ''.join(choice(DEFAULT_CHARACTERS) for _ in range(length))

    prefix_len = length - 6
    set_len = len(DEFAULT_CHARACTERS)

    token = ''.join(choice(DEFAULT_CHARACTERS) for _ in range(prefix_len))
    now = datetime.now(timezone.utc)

    token += DEFAULT_CHARACTERS[now.day]
    token += DEFAULT_CHARACTERS[now.month]
    token += DEFAULT_CHARACTERS[now.year % set_len]
    token += DEFAULT_CHARACTERS[now.hour]
    token += DEFAULT_CHARACTERS[now.minute % set_len]
    token += DEFAULT_CHARACTERS[now.second % set_len]

    return token
