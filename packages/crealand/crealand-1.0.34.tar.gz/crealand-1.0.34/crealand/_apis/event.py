from crealand._core.bridge import _interface
from crealand._apis import _subscribe_event
from crealand._utils import _utils

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

# 获取鼠标按键值
def get_mouse_value():
    result = _interface.call_api('web-ide',"api.getMouseValue",[{'code':0}])
    return result
# 获取键盘code值
def get_keyboard_value():
    result = _interface.call_api('web-ide',"api.getKeyboardValue",[{}])
    return result

#鼠标按下事件
def onInputsMouseEvent(click,button,cb):
    def cb_wrapper(err,data):
        if err is None:
            cb()
        else:
            _utils.raise_error('onInputsMouseEvent',err,data)
    _subscribe_event.onEventKeyCode(click,button,cb_wrapper)

#键盘按下事件
def onInputsKeyboardEvent(click,button,cb):
    def cb_wrapper(err,data):
        if err is None:
            cb()
        else:
            _utils.raise_error('onInputsKeyboardEvent',err,data)
    _subscribe_event.onEventKeyCode(click,button,cb_wrapper)