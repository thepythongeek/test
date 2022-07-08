import os
from qfp import ReferenceFingerprint, QueryFingerprint
from qfp.db import QfpDB as DB

def find_audio(path):
    '''
    find if we have any record about this audio 
    (could be a song or audio clip).
    '''
    fingerprint = QueryFingerprint(path)
    fingerprint.create()
    db = DB()
    db.query(fingerprint)
    return fingerprint.matches

def create_audio_fingerprint(path):
    '''
    create an audio fingerprint for this audio and 
    store it.
    '''
    fingerprint = ReferenceFingerprint(path)
    fingerprint.create()
    return DB().store(fingerprint, os.path.splitext(os.path.basename(path))[0])


class AudioFingerPrintException (Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)