from crealand._core.bridge import _interface
from crealand._apis import _subscribe_event
from typing import Callable,Any
from crealand._utils import _utils, _logger_setup

_logger = _logger_setup.setup_logger()

# 超声波传感器

class Ultrasonic:
    _sensors = {}

    # 前端处理传感器信息绑定
    @staticmethod
    def add_sensor(sensor: str, runtime_id: int, attachment_id: tuple) ->None:
        if not isinstance(sensor, str) or not isinstance(runtime_id, int) :
            raise ValueError("Invalid arguments: sensor must be a string, runtime_id must be integers.")
        attach=_utils.Handle_point(attachment_id)
        Ultrasonic._sensors[sensor] = (runtime_id, attach)

    @staticmethod
    def get_sensor(sensor: str) -> list:
        if sensor in Ultrasonic._sensors:
            return Ultrasonic._sensors[sensor]
        else:
            raise KeyError(f"Sensor '{sensor}' not found")

    @staticmethod
    def onSensorUltrasonicEvent(sensor: str, compare: str, distance: float,cb:Callable[...,Any]):
        sensor_info = Ultrasonic.get_sensor(sensor) 
        attachment_id = sensor_info[1]
        _subscribe_event.onSensorUltrasonicEvent(sensor_info[0],attachment_id,compare,distance,cb)

    @staticmethod
    def get_obstacle_distance(sensor: str)->float:
        sensor_info = Ultrasonic.get_sensor(sensor) 
        length = _interface.call_api('unity', 'unity.sensor.ultrasonicRanging', [sensor_info[0], sensor_info[1]])
        return length

class Auditory:

    _decibel_val=0

    # 获取声音强度
    @staticmethod
    def get_decibel_value():
        return Auditory._decibel_val

    @staticmethod
    def onSensorSoundEvent(compare,decibel_value,cb):
        def cb_wrapper(err,data):
            if err is None:
                Auditory._decibel_val = data['data']
                cb()
            else:
                _logger.error(f"Error occurred: {err},{data}")

        _subscribe_event.onSensorSoundEvent(compare,decibel_value,cb_wrapper)

    # 开始分贝识别
    @staticmethod
    def start_decibel_recognition():
        def cb_wrapper(err,data):
            if err is None:
                Auditory._decibel_val = data['data']
            else:
                _logger.error(f"Error occurred: {err},{data}")

        _subscribe_event.onSensorSoundEvent('==','',cb_wrapper)

    # 结束分贝识别
    @staticmethod
    def stop_decibel_recognition():
        _interface.call_api_async('web-ide', 'api.openDecibelDetectionPage', [{'type':'end'}])


class Visual:
    _sensors = {}

    # 将传感器绑定到对象的挂点
    @staticmethod
    def add_sensor( sensor: str, runtime_id: int, attachment_id: tuple):
        attach=_utils.Handle_point(attachment_id)
        Visual._sensors[sensor] = (runtime_id, attach)

    # 获取传感器信息
    @staticmethod
    def get_sensor( sensor: str):
        if sensor in Visual._sensors:
            return Visual._sensors[sensor]
        else:
            raise KeyError(f"Sensor '{sensor}' not found")

    # 打开或关闭传感器画面
    @staticmethod
    def open_visual_sensor( action_type: bool=True,sensor: str=''):
        sensor_info=Visual.get_sensor(sensor)
        if action_type:
            func_name = 'unity.sensor.openVision'
            _interface.call_api('unity',func_name,[sensor_info[0], sensor_info[1],sensor])
        else:
            func_name = 'unity.sensor.closeVision'
            _interface.call_api('unity',func_name,[sensor])

class Temperature:

    _sensors = {}

    @staticmethod
    def add_sensor(sensor: str, runtime_id: int) ->None:
        if not isinstance(sensor, str) or not isinstance(runtime_id, int):
            raise ValueError("Invalid arguments: sensor must be a string, runtime_id and attachment_id must be integers.")
        Temperature._sensors[sensor] = runtime_id
        _interface.call_api('unity','unity.sensor.attachTemperature',[runtime_id])

    @staticmethod
    def get_sensor(sensor: str) -> int:
        if sensor in Temperature._sensors:
            return Temperature._sensors[sensor]
        else:
            raise KeyError(f"Sensor '{sensor}' not found")

    @staticmethod
    def onSensorTemperatureEvent(sensor, compare, temperature,cb):
        runtime_id = Temperature.get_sensor(sensor)
        def cb_wrapper(err,data):
            if err is None:
                cb()
            else:
                _logger.error(f"Error occurred: {err},{data}")
        _subscribe_event.onSensorTemperatureEvent(runtime_id,compare,temperature,cb_wrapper)
    
    # 设置判定区域温度

    @staticmethod
    def set_temperature( area_id: int, temp_val: float):
        temp_val = max(-40, min(temp_val, 120))
        _interface.call_api('unity','unity.sensor.setTemperature',[area_id,temp_val])

    # 持续检测判定区域温度

    @staticmethod
    def startTemperatureDetection( area_id):
        _subscribe_event.startTemperatureDetection(area_id)

    # 获取温度值
    @staticmethod
    def get_temperature_value( sensor: str):
        runtime_id=Temperature.get_sensor(sensor)
        temperature_value=_interface.call_api('unity','unity.sensor.getTemperature',[runtime_id])
        return temperature_value



class Humidity:

    _sensors = {}

    @staticmethod
    def add_sensor(sensor: str, runtime_id: int) ->None:
        if not isinstance(sensor, str) or not isinstance(runtime_id, int):
            raise ValueError("Invalid arguments: sensor must be a string, runtime_id and attachment_id must be integers.")
        Humidity._sensors[sensor] = runtime_id
        _interface.call_api('unity','unity.sensor.attachHumidity',[runtime_id])

    @staticmethod
    def get_sensor(sensor: str) -> int:
        if sensor in Humidity._sensors:
            return Humidity._sensors[sensor]
        else:
            raise KeyError(f"Sensor '{sensor}' not found")

    @staticmethod
    def onSensorHumidityEvent(sensor, compare, humidity_value,cb):
        runtime_id = Humidity.get_sensor(sensor) 
        def cb_wrapper(err,data):
            if err is None:
                cb()
            else:
                _logger.error(f"Error occurred: {err},{data}")
        _subscribe_event.onSensorHumidityEvent(runtime_id,compare,humidity_value,cb_wrapper)

    # 设置判定区域湿度
    @staticmethod
    def set_humidity( area_id: int, humidity_value: int):
        humidity_value = int(humidity_value)
        humidity_value= max(0, min(humidity_value, 100))
        _interface.call_api('unity','unity.sensor.setHumidity',[area_id,humidity_value])


    @staticmethod
    def get_humidity_value(senser:str):
        runtime_id=Humidity.get_sensor(senser)
        result= _interface.call_api('unity','unity.sensor.getHumidity',[runtime_id])
        return result

    # 持续检测判定区域湿度

    @staticmethod
    def startHumidityDetection( area_id: int):
        _subscribe_event.startHumidityDetection(area_id)


class Gravity:

    _sensors = {}

    @staticmethod
    def add_sensor(sensor: str, area_id: int) ->None:
        if not isinstance(sensor, str) or not isinstance(area_id, int):
            raise ValueError("Invalid arguments: sensor must be a string, area_id and attachment_id must be integers.")
        Gravity._sensors[sensor] = area_id
        _interface.call_api('unity','unity.sensor.attachGravity',[area_id])

    @staticmethod
    def get_sensor(sensor: str) -> int:
        if sensor in Gravity._sensors:
            return Gravity._sensors[sensor]
        else:
            raise KeyError(f"Sensor '{sensor}' not found")

    @staticmethod
    def onSensorGravityEvent(sensor: str, compare: str, gravity_value: int,cb:Callable[...,Any]):
        runtime_id = Gravity.get_sensor(sensor)
        def cb_wrapper(err,data):
            if err is None:
                cb()
            else:
                _logger.error(f"Error occurred: {err},{data}")
        _subscribe_event.onSensorGravityEvent(runtime_id,compare,gravity_value,cb_wrapper)

    @staticmethod
    # 设置对象重力
    def set_gravity( runtime_id: str, gravity_value: int):
        gravity_value = int(gravity_value)
        gravity_value= max(0, min(gravity_value, 10000))
        _interface.call_api('unity','unity.sensor.setGravity',[runtime_id,gravity_value])

    # 获取重力值
    @staticmethod
    def get_gravity_value( sensor: str):
        runtime_id = Gravity.get_sensor(sensor) 
        value= _interface.call_api('unity','unity.sensor.getGravity',[runtime_id])
        return value

