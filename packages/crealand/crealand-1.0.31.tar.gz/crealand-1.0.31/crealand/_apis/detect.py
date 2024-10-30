from crealand._core.bridge import _interface
from crealand._apis import _subscribe_event
from crealand._utils import _logger_setup

_logger = _logger_setup.setup_logger()

class Detect:
    _decibel_val=0
    # 分贝值
    @staticmethod
    def get_decibel_value():
        return Detect._decibel_val

    # 开始识别
    @staticmethod
    def start_decibel_recognition():

        def cb_wrapper(err,data):
            if err is None:
                Detect._decibel_val = data['data']
            else:
                _logger.error(f"Error occurred: {err},{data}")

        _subscribe_event.onSensorSoundEvent('==','',cb_wrapper)

    # 结束识别
    def stop_decibel_recognition():
        _interface.call_api_async('web-ide', 'api.openDecibelDetectionPage', [{'type':'end'}])

    @staticmethod
    def onEventDecibel(decibel_value,cb):
        def cb_wrapper(err,data):
            if err is None:
                Detect._decibel_val = data['data']
                cb(data['data'])
            else:
                _logger.error(f"Error occurred: {err},{data}")


        _subscribe_event.onSensorSoundEvent('>',decibel_value,cb_wrapper)


    # 获取虚拟相机
    @staticmethod
    def virtual_camera(runtime_id: int,status: bool, ):
        _interface.call_api('unity', 'unity.camera.openVirsual', [runtime_id,status])
