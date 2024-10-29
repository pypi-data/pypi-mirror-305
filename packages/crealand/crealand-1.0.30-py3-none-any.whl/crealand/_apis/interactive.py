from crealand._core.bridge import _interface
from crealand._apis.constants import OptionName, ResultType, ToastPosition, ToastState, Volume

class Dialogue:
    # 立绘对话 获取选项
    option_value = ''
    # @classmethod
    def get_option_value(self):
        return self.option_value

    # 立绘对话 初始化
    @staticmethod
    def init():
        _interface.call_api('web-ide', "api.prepareDialogBoard", [{}])
        

    # 立绘对话 显示
    @staticmethod
    def set_dialogue(
        obj_name: str,
        content: str,
        res_id: str,
        volume: str = Volume.MEDIUM,
    ):
        _interface.call_api(
            'web-ide',
            "api.showDialog",
            [
                {
                    "speaker": obj_name,
                    "type": volume,
                    "txt": content,
                    "voiceId": '',
                    "imgId":res_id,
                }
            ],
        )
    @staticmethod
    def set_dialogue_tone(
        obj_name: str,
        content: str,
        res_id: str,
        tone: str,
        volume: str = Volume.MEDIUM,
    ):
        _interface.call_api(
            'web-ide',
            "api.showDialog",
            [
                {
                    "speaker": obj_name,
                    "type": volume,
                    "txt": content,
                    "voiceId": tone,
                    "imgId":res_id,
                }
            ],
        )

    # 立绘对话 设置选项
    @staticmethod
    def set_option( content: str, opt_name: str = OptionName.OPTION01):
        options = {}
        options[opt_name] = content
        _interface.call_api(
            'web-ide',
            "api.setDialogOptions",
            [{"options": options}],
        )

    # 立绘对话选项 显示
    @classmethod
    def set_option_show(self,is_show: bool = True):
        self.option_value = _interface.call_api('web-ide', "api.toggleDialogOptions", [{"show": is_show}])
    #  立绘对话 显示
    @classmethod
    def show(self,is_show: bool = True):
        if is_show == False:
            self.option_value = ''
            
        _interface.call_api('web-ide', "api.toggleDialogBoard", [{"show": is_show}])


class HelpPanel:
    # 帮助面板 初始化
    @staticmethod
    def init():
        _interface.call_api('web-ide', "api.prepareHelpboard", [{}])

    # 帮助面板 设置标题
    @staticmethod
    def set_tips(title: str, res_id: str):
        _interface.call_api(
            'web-ide',
            "api.addHelpItem",
            [
                {
                    "title": title,
                    "imgId": res_id,
                }
            ],
        )

    # 帮助面板 显示
    @staticmethod
    def show(is_show: bool = True):
        _interface.call_api(
            'web-ide',
            "api.toggleHelpboard",
            [
                {
                    "show": is_show,
                }
            ],
        )


class TaskPanel:

    # 任务面板 设置标题
    @staticmethod
    def set_task(title: str, nickname: str):
        _interface.call_api(
            'web-ide',
            "api.createTaskboard",
            [
                {
                    "title": title,
                    "alias": nickname,
                }
            ],
        )

    # 任务面板 设置任务项
    @staticmethod
    def set_task_progress(
        task_name: str, subtasks_content: str, completed_tasks: int, total_tasks: int
    ):
        _interface.call_api(
            'web-ide',
            "api.setTaskboard",
            [
                {
                    "alias": task_name,
                    "taskName": subtasks_content,
                    "process": [max(0, completed_tasks), max(1, total_tasks)],
                }
            ],
        )

    # 任务面板 显示
    @staticmethod
    def set_task_show(task_name: str, is_show: bool = True):
        _interface.call_api(
            'web-ide',
            "api.toggleTaskboard",
            [{"alias": task_name, "show": is_show}],
        )


class Speak:
    # 说
    @staticmethod
    def text( runtime_id: int, content: str, time: int = 2):
        _interface.call_api_async(
            'unity', "unity.actor.speak", [runtime_id, content, time]
        )

    # 说-img
    @staticmethod
    def image(runtime_id: int, res_id: str, time: int = 2):
        _interface.call_api_async(
           'unity', "unity.actor.speakImage", [runtime_id, res_id, time]
        )


class Interactive:
    # 提示面板显示
    @staticmethod
    def set_tip_show(option: str = ResultType.START):
        _interface.call_api(
            'web-ide',
            "api.showTipboardResult",
            [
                {
                    "result": option,
                }
            ],
        )

    # 提示面板显示
    @staticmethod
    def toast(
        content: str,
        position: str = ToastPosition.TOP,
        state: str = ToastState.DYNAMIC,
    ):
        _interface.call_api_async(
            'web-ide',
            "api.toast",
            [
                {
                    "position": position,
                    "mode": state,
                    "txt": content,
                }
            ],
            
        )
