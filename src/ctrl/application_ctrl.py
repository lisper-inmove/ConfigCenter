from ctrl.base_ctrl import BaseCtrl
from dao.application_dao import ApplicationDA
from submodules.utils.misc import Misc
from submodules.utils.idate import IDate


class ApplicationCtrl(BaseCtrl):

    dao = ApplicationDA()

    def create(self):
        application = {
            "id": Misc.uuid(),
            "createTime": IDate.now_timestamp(),
            "updateTime": IDate.now_timestamp(),
            "name": self.name
        }
        self.dao.create(application)
        return application

    def delete(self):
        self.dao.delete(id=self.id)
        return {}

    def list(self):
        return self.dao.list()
