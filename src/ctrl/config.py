from ctrl.base_ctrl import BaseCtrl
from submodules.utils.idate import IDate
from dao.config_dao import ConfigDA
from view.errors import PopupError


class ConfigCtrl(BaseCtrl):

    dao = ConfigDA()

    def create(self):
        params = self.params
        config = {
            "applicationId": self.applicationId,
            "createTime": IDate.now_timestamp(),
            "updateTime": IDate.now_timestamp(),
            "params": params
        }
        self.dao.create(config)
        return config

    def update(self):
        params = self.params
        config = {
            "applicationId": self.applicationId,
            "updateTime": IDate.now_timestamp(),
            "params": params
        }
        self.dao.update(config)
        return config

    def query(self):
        config = self.dao.get(self.applicationId)
        if not config:
            raise PopupError("配置不存在")
        return config
