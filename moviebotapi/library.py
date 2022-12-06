from typing import List, Optional, Dict

from moviebotapi import Session
from moviebotapi.core import utils
from moviebotapi.core.models import MediaType


class MediaLibraryPath:
    path: str
    auto_scan: bool = False

    def __init__(self, data: Dict = None):
        if not data:
            utils.copy_value(data, self)


class LibraryApi:
    def __init__(self, session: Session):
        self._session: Session = session

    def start_scanner(self, library_id: int):
        self._session.get('library.start_scanner', {
            'library_id': library_id
        })

    def stop_scanner(self, library_id: int):
        self._session.get('library.stop_scanner', {
            'library_id': library_id
        })

    def add_library(self, media_type: MediaType, library_name: str, library_paths: List[MediaLibraryPath]) -> Optional[
        int]:
        return self._session.post('library.add_library', {
            'library_name': library_name,
            'media_type': media_type.value,
            'library_paths': [utils.to_dict(x) for x in library_paths]
        })
