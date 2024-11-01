from crealand._core.bridge import _interface
from crealand._apis import _subscribe_event, _constants
from crealand._utils import _utils
import time

#收到广播事件
def onBroadcastEvent(info,cb):
    _subscribe_event.onBroadcastEvent(info,cb)

#发送广播事件
def send_broadcast(info):
    _subscribe_event.sendBroadcast(info)

#对象进入/离开判定区域事件
def onAreaObjectEvent(runtime_id,action,area_id,cb):
    def cb_wrapper(err,data):
        if err is None:
            cb()
        else:
            _utils.raise_error('onAreaObjectEvent',err,data)
    _subscribe_event.onAreaObjectEvent(runtime_id,action,area_id,cb_wrapper)

#分类进入/离开判定区域事件
def onAreaClassEvent(config_id,action,area_id,cb):
    def cb_wrapper(err,data):
        if err is None:
            cb()
        else:
            _utils.raise_error('onAreaClassEvent',err,data)
    _subscribe_event.onAreaClassEvent(config_id,action,area_id,cb_wrapper)

# 验证按键是否按下
def keydown_state(button):
    time.sleep(_constants.SLEEP_TIME)
    result = _interface.call_api('unity',"unity.input.verifyKeyCodeState",[button, _constants.KeyActiveType.KEY_DOWN])
    return result

# 鼠标键盘事件
def onKeyEvent(click,button,cb):
    def cb_wrapper(err,data):
        if err is None:
            cb()
        else:
            _utils.raise_error('onKeyEvent',err,data)
    _subscribe_event.onKeyEvent(click,button,cb_wrapper)
