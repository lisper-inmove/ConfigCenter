from dao.mongodb import MongoDBHelper


class ApplicationDA(MongoDBHelper):

    coll = "___application_db___applications___"

    def create(self, application):
        self.update_one({"id": application.get("id")}, application, upsert=True)

    def delete(self, id):
        self.delete_one({"id": id})

    def get(self, id):
        return self.find_one({"id": id})

    def list(self):
        return list(self.find_many({}))
