from dao.mongodb import MongoDBHelper


class ConfigDA(MongoDBHelper):

    coll = "___config_db___configs___"

    def create(self, config):
        self.update_one(
            {"applicationId": config.get("applicationId")},
            config,
            upsert=True
        )

    def update(self, config):
        self.update_one(
            {"applicationId": config.get("applicationId")},
            config,
            upsert=True
        )

    def delete(self, applicationId):
        self.delete_one({"applicationId": applicationId})

    def get(self, applicationId):
        return self.find_one({"applicationId": applicationId})
