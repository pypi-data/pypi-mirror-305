from crealand._core.bridge import _interface
from crealand._apis.constants import Axis, AxisType, FilterStyle, HangPointType
from crealand._utils import _utils
from typing import List

# 信息
class Info:

    # 别名对象id
    @staticmethod
    def get_alias_id(
        nickname: str ,
    ):
        result = _interface.call_api(
            'unity', "unity.alias.getByAlias", [nickname]
        )
        return result

    # 获取configID的对象id
    @staticmethod
    def get_object_id(runtime_id) -> int:
        result = _interface.call_api(
            'unity',
            "unity.actor.getConfigID",
           [runtime_id] ,
        )
        return result

    # 获取对象的空间坐标
    @staticmethod
    def get_object_coordinates(runtime_id: int) :
        result = _interface.call_api(
            'unity', "unity.actor.getCoordinate", [runtime_id]
        )
        return result

    # 获取判定区域中的对象id
    @staticmethod
    def get_id_in_area(area_id: int, config_ids: List[str]) :
        result = _interface.call_api(
            'unity',
            "unity.editableTrigger.getContentRuntimeIds",
            [area_id, config_ids],
        )
        return result

    # 获取空间坐标某个轴的值
    @staticmethod
    def get_spatial_coordinates(coordinate: List[float], axis: str=Axis.X) :
        AXIS = {"X": 0, "Y": 1, "Z": 2}
        return coordinate[AXIS[axis]]

    # 获取对象的运动方向向量
    @staticmethod
    def get_motion_vector(runtime_id: int) :
        result = _interface.call_api(
            'unity', "unity.character.getMoveDirection", [runtime_id]
        )
        return result


class Camera:

    # 获取相机ID
    @classmethod
    def get_default_id(self):
        return _interface.call_api(
            'unity', "unity.camera.getDefaultID",[]
        )

    # 获取空间坐标
    @classmethod
    def get_object_coordinates(self, runtime_id: int) :
        result = _interface.call_api(
            'unity', "unity.actor.getCoordinate", [runtime_id]
        )
        return result

    # 相机移动
    @classmethod
    def move_to(self, time: float, coordinate: List[float], block: bool = False):
        new_time = max(0, time)
        _interface.call_api(
            'unity',
            "unity.camera.moveTo",
            [self.get_default_id(), new_time, coordinate, block ],
        )

    # 调整FOV
    @classmethod
    def adjust_FOV(self, time: float = 1, fov: float = 80):
        new_time = max(0, time)
        new_fov = max(60, min(fov, 120))
        _interface.call_api_async(
            'unity',
            "unity.camera.adjustFOV",
            [self.get_default_id(), new_time, new_fov],
        )

    # 相机锁定朝向并移动
    @classmethod
    def move_while_looking(
        self,
        coordinate_1: List[float],
        time: float = 1,
        coordinate_2: List[float] = [0, 0, 1],
        block: bool = False,
    ):
        new_time = max(0, time)
        _interface.call_api_async(
            'unity',
            "unity.camera.moveWhileLooking",
            [self.get_default_id(), new_time, coordinate_2, coordinate_1, block],
        )

    # 获取相机坐标
    @classmethod
    def get_camera_coordinate(self) -> List[float]:
        result = self.get_object_coordinates(self.get_default_id())
        return result

    # 相机朝向
    @classmethod
    def look_at(self, coordinate: List[float]):
        _interface.call_api_async(
            'unity',
            "unity.camera.lookAt",
            [self.get_default_id(), coordinate],
        )

    # 相机跟随
    @classmethod
    def follow_target(self, runtime_id: int, distance: float = 10, is_rotate: bool = True):
        _interface.call_api_async(
            'unity',
            "unity.camera.followTarget",
            [self.get_default_id(), runtime_id, distance, is_rotate],
        )

    # 相机结束跟随
    @classmethod
    def end_follow_target(self):
        _interface.call_api_async(
            'unity',
            "unity.camera.stopFollowing",
            [
                self.get_default_id(),
            ],
        )

    # 相机 滤镜
    @classmethod
    def filters(self, filter_name: str = FilterStyle.FOG, state: bool = True):
 
        _interface.call_api_async(
            'unity',
            "unity.camera.openEffect",
            [self.get_default_id(), filter_name, state],
        )


class Motion:
    # 创建对象
    @classmethod
    def create_object_coordinate(self, config_id: str, coordinate: List[float]):
        result = _interface.call_api(
            'unity',
            "unity.actor.createObject",
            [config_id, coordinate],
        )
        return result

    # 测距
    @staticmethod
    def ray_ranging(runtime_id: int, attachment_id: int = (HangPointType.LEFT_FRONT_WHEEL,)):
        
        result = _interface.call_api(
            'unity',
            "unity.actor.rayRanging",
            [runtime_id, _utils.Handle_point(attachment_id), 20],
        )
        return result

    # 移动
    @staticmethod
    def move_to(runtime_id: int, coordinate: List[float] = [0, 0, 1]):
        _interface.call_api(
            'unity',
            "unity.actor.setObjectPosition",
            [
                runtime_id,
                coordinate,
            ],
        )

    # 朝向
    @staticmethod
    def face_towards(runtime_id: int, coordinate: List[float] = [0, 0, 1]):
        _interface.call_api(
            'unity',
            "unity.actor.setObjectTowardPosition",
            [
                runtime_id,
                coordinate,
            ],
        )

    # 前进
    @staticmethod
    def move_forward(
        runtime_id: int, speed: float =1, distance: float =3, block: bool = False
    ):
        new_speed = max(1, min(speed, 5))
        _interface.call_api(
            'unity',
            "unity.actor.moveForwardByDistance",
            [
                runtime_id,
                distance,
                distance/new_speed,
            block ,
            ],
        )

    # 对象旋转
    @staticmethod
    def rotate(runtime_id: int, time: float=1, angle: float=90, block: bool = False):
        new_time = max(time, 0)
        _interface.call_api(
            'unity',
            "unity.character.rotateUpAxisByAngle",
            [
                runtime_id,
                angle,
                new_time,
                block 
            ],
        )

    # 云台旋转 & 机械臂旋转
    @staticmethod
    def ptz(runtime_id: int, angle: float=90, block: bool = False):
        print(block)
        _interface.call_api(
            'unity',
            "unity.actor.rotatePTZUpAxisByAngle",
            [runtime_id, angle, abs(angle) / 30, block],
        )

    # 播放动作
    @staticmethod
    def action(runtime_id: int, action: str, block: bool = False):
        _interface.call_api(
            'unity',
            "unity.actor.playAnimation",
            [runtime_id, action, block ],
        )

    # # 将对象吸附到挂点
    @staticmethod
    def attach_to(absorbed_runtime_id: int, absorb_runtime_id: int, attachment_id: tuple):
        print(_utils.Handle_point(attachment_id),'-----')
       
        _interface.call_api(
            'unity',
            "unity.actor.attach",
            [absorbed_runtime_id, absorb_runtime_id,  _utils.Handle_point(attachment_id)],
        )

    # 绑定挂点
    @staticmethod
    def bind_to_object_point(
        runtime_id_1: int,
        attachment_id_1: str,
        runtime_id_2: int,
        attachment_id_2: str,
    ):
        _interface.call_api(
            'unity',
            "unity.actor.bindAnchor",
            [runtime_id_1, _utils.Handle_point(attachment_id_1), runtime_id_2, _utils.Handle_point(attachment_id_2)],
        )

    # 解除绑定
    @staticmethod
    def detach(runtime_id: int):
        _interface.call_api(
            'unity',
            "unity.actor.detach",
            [
                runtime_id,
            ],
        )

    # 向画面空间前进
    @staticmethod
    def move_towards_screen_space(
        runtime_id: int, speed: float = 1, direction: List[float] = [0, 0, 1]
    ):
        new_speed = max(1, min(speed, 5))
        _interface.call_api(
            'unity',
            "unity.actor.moveByVelocity",
            [
                runtime_id,
                new_speed,
                2,
                direction,
            ],
        )

    # 旋转运动方向向量
    @staticmethod
    def rotate_to_direction(
        runtime_id: int, angle: float = 0, direction: List[float] = [0, 0, 1]
    ):
        _interface.call_api(
            'unity',
            "unity.character.rotateUpAxisByDirection",
            [runtime_id, angle, direction,0],
        )

    # 停止运动
    @staticmethod
    def stop(runtime_id: int):
        _interface.call_api_async(
            'unity',
            "unity.character.stop",
            [runtime_id],
        )

    # 设置别名
    @classmethod
    def create_object(
        self,
        config_id: int,
        nickname: str,
        coordinate: List[float] = [0, 0, 1],
    ):
        _interface.call_api_async(
            'unity',
            "unity.alias.setAlias",
            [
                nickname,
                self.create_object_coordinate(config_id, coordinate),
            ],
        )

    # 销毁对象
    @staticmethod
    def destroy(runtime_id: int):
        _interface.call_api(
            'unity',
            "unity.alias.destoryObject",
            [
                runtime_id,
            ],
        )

    # 上升
    @staticmethod
    def rise(
        runtime_id: int, speed: float = 3, height: float = 10, block: bool = False
    ):
        new_speed = max(1, min(speed, 5))
        _interface.call_api(
            'unity',
            "unity.character.moveUpByDistance",
            [runtime_id, height, height/new_speed, block],
        )
    # 降落
    @staticmethod
    def landing(
        runtime_id: int 
    ):
        _interface.call_api(
            'unity',
            "unity.character.land",
            [runtime_id, 3],
        )

    # 获取离自身距离的坐标
    @staticmethod
    def get_object_local_position(
        runtime_id: int, coordinate: List[float] = [0, 0, 1], distance: float = 0
    ):
        result = _interface.call_api_async(
            'unity',
            "unity.actor.getObjectLocalPosition",
            [runtime_id, coordinate, distance],
        )
        print(result,'=====')
        return result

    # 移动到指定坐标
    @staticmethod
    def move_by_point(
        runtime_id: int, time: float = 1, coordinate: List[float] = [0, 0, 1], block: bool = False
    ):
        new_time = max(time, 0)
        _interface.call_api(
            'unity',
            "unity.actor.moveByPoint",
            [runtime_id, new_time, coordinate, block ],
        )

    # 绕坐标轴旋转
    @staticmethod
    def rotate_by_origin_and_axis(
        runtime_id: int,
        time: float = 2,
        point_1: str=AxisType.LOCAL,
        coordinate_1: List[float] = [0, 0, 0],
        point_2: str=AxisType.LOCAL,
        coordinate_2: List[float]= [0, 0, 1],
        angle: float=90,
        block: bool = False,
    ):
        new_time = max(time, 0)
        _interface.call_api(
            'unity',
            "unity.actor.rotateByOringinAndAxis",
            [
                runtime_id,
                coordinate_1,
                point_1,
                coordinate_2,
                point_2,
                angle,
                new_time,
                block 
            ],
        )


class Property:
    # 新增自定义属性
    @staticmethod
    def add_attr(runtime_id: int, attr_name: str, attr_value: str):
        _interface.call_api(
            'unity',
            "unity.actor.addCustomProp",
            [runtime_id, attr_name, attr_value],
        )

    # 删除自定义属性
    @staticmethod
    def del_attr(runtime_id: int, attr_name: str):
        _interface.call_api(
            'unity',
            "unity.actor.delCustomProp",
            [runtime_id, attr_name],
        )

    # 修改自定义属性
    @staticmethod
    def set_attr(runtime_id: int, attr_name: str, attr_value: str):
        _interface.call_api(
            'unity',
            "unity.actor.setCustomProp",
            [runtime_id, attr_name, attr_value],
        )

    # 获取自定义属性的值
    @staticmethod
    def get_value(runtime_id: int, attr_name: str):
        result = _interface.call_api(
            'unity',
            "unity.actor.getCustomProp",
            [runtime_id, attr_name],
        )
        return result

    # 获取自定义属性组中某一项的值
    @staticmethod
    def get_value_by_idx(runtime_id: int, index: int = 1):
        result= _interface.call_api(
            'unity',
            "unity.actor.getCustomPropValueByIdx",
            [runtime_id, index],
        )
        return result

    # 获取自定义属性组中某一项的名称
    @staticmethod
    def get_key_by_idx(runtime_id: int, index: int = 1):
        result=_interface.call_api(
            'unity',
            "unity.actor.getCustomPropKeyByIdx",
            [runtime_id, index],
        )
        return result


class Show:
    # 3d文本-RGB
    @staticmethod
    def set_3D_text_status_rgb(runtime_id: int, rgb: List[int] = [255, 255, 255], size: int = 30, text: str = '文本'):
        _interface.call_api(
            'unity',
            "unity.building.set3DTextStatus",
            [runtime_id, rgb, size, text],
        )
