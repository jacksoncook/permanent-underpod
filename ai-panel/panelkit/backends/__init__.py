from .base import BackendError, TalkingHeadBackend
from .liveportrait import LivePortraitBackend
from .musetalk import MuseTalkBackend
from .sadtalker import SadTalkerBackend
from .static import StaticBackend

BACKENDS = {cls.name: cls for cls in
            (MuseTalkBackend, SadTalkerBackend, LivePortraitBackend,
             StaticBackend)}


def get_backend(name: str) -> TalkingHeadBackend:
    try:
        cls = BACKENDS[name]
    except KeyError:
        raise BackendError(
            f"unknown backend {name!r}; available: {', '.join(sorted(BACKENDS))}"
        )
    return cls()
