from crealand._core.bridge import _interface

class Sound:
    # 播放声音
    @staticmethod
    def play_sound(runtime_id: int, res_id: str,is_loop: bool=False):
        _interface.call_api_async(
            'unity',
            "unity.sound.playSound",
            [runtime_id, is_loop, res_id],
        )

    # 声音
    @staticmethod
    def adjust_volume(runtime_id: int, volume: int = 50):
        _interface.call_api_async(
            'unity',
            "unity.sound.adjustVolume",
            [runtime_id, max(0, min(volume, 100))],
        )

    # 停止播放
    @staticmethod
    def stop(runtime_id: int):
        _interface.call_api_async('unity', "unity.sound.stopSound", [runtime_id])

    # 设置背景音效
    @staticmethod
    def play_bgm(res_id: str):
        _interface.call_api_async('unity', "unity.sound.playBgSound", [res_id])

    # 背景音效音量
    @staticmethod
    def adjust_bgm_volume(volume: int = 50):
        _interface.call_api_async(
            'unity',
            "unity.sound.adjustBgVolume",
            [max(0, min(volume, 100))],
        )

    # 停止背景音效
    @staticmethod
    def stop_bgm():
        _interface.call_api_async(
            'unity',
            "unity.sound.stopBgSound",
            [],
        )


class Video:
    # 播放视频
    @staticmethod
    def play(res_id: str):
        _interface.call_api(
            'web-ide',
            "api.playVideo",
            [{res_id}],
        )


class Image:
    # 播放图片
    @staticmethod
    def show(res_id: str):
        _interface.call_api(
            'web-ide',
            "api.showImage",
            [{res_id}],
        )
