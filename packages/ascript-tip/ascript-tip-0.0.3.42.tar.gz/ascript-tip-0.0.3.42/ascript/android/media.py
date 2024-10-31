from airscript.system import Media as asMedia
from airscript.system import TTSAliHelper
from airscript.system import AliTTsParam
import threading


def volume(percent: int, type: int = 3):
    asMedia.volume(percent, type)


def get_volume(type: int = 3):
    return asMedia.getVolume(type)


def talk(msg: str):
    asMedia.talk(msg)


def play(path: str, callback=None):
    if callback:
        asMedia.play(path, callback)
    else:
        asMedia.play(path)


def recode(path: str, time=None):
    if time:
        return asMedia.recode(path, time)
    else:
        return asMedia.recode(path)


def vibrate(time: int = 200):
    asMedia.vibrate(time)


ali_tts_lock = threading.Lock()


def ali_tts(config: dict, tts_msg: str, autp_play: bool = True, save_file=None):
    with ali_tts_lock:
        tts = TTSAliHelper.getInstance()
        tts.init(config['app_key'], config['ak_id'], config['ak_secret'], config['font_name'])
        tts.setPlay(autp_play)
        if save_file:
            tts.saveFile(save_file)

        return tts.change(tts_msg)


class AliTts:
    def __init__(self, app_key: str, ak_id: str, ak_secret: str, font_name: str = "siqi", speed_level: str = "1",
                 pitch_level: str = "0", volume: str = "1.0"):
        self.tts_core = TTSAliHelper()
        self.param = AliTTsParam()
        self.param.setApp_key(app_key)
        self.param.setAk_id(ak_id)
        self.param.setAk_secret(ak_secret)
        self.param.setFont_name(font_name)
        self.param.setSpeed_level(speed_level)
        self.param.setPitch_level(pitch_level)
        self.param.setVolume(volume)
        self.tts_core.init_params(self.param)

    def start(self, tts_msg: str, auto_play: bool = True, save_file=None, font_name: str = None, speed_level: str = None,
                 pitch_level: str = None, volume: str = None):
        self.tts_core.setPlay(auto_play)
        self.tts_core.saveFile(save_file)
        if font_name:
            self.param.setFont_name(font_name)
        if speed_level:
            self.param.setSpeed_level(speed_level)
        if pitch_level:
            self.param.setPitch_level(pitch_level)
        if volume:
            self.param.setVolume(volume)
        self.tts_core.init_params(self.param)
        return self.tts_core.change(tts_msg)

    def start_asy(self, tts_msg: str, auto_play: bool = True, save_file=None,call_back=None, font_name: str = "siqi", speed_level: str = "1",
                 pitch_level: str = "0", volume: str = "1.0"):
        self.tts_core.setPlay(auto_play)
        self.tts_core.saveFile(save_file)
        if font_name:
            self.param.setFont_name(font_name)
        if speed_level:
            self.param.setSpeed_level(speed_level)
        if pitch_level:
            self.param.setPitch_level(pitch_level)
        if volume:
            self.param.setVolume(volume)
        self.tts_core.init_params(self.param)
        if call_back:
            self.tts_core.callBack(call_back)
        return self.tts_core.change_asy(tts_msg)

    def close(self):
        return self.tts_core.close()


def image_to_gallery(file_path: str):
    asMedia.file_to_gallery(file_path)
