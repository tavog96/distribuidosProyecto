from flask_restful import reqparse, abort, Resource

class resourceController(Resource):

    def __init__(self):
        super().__init__()

    def get(self, uidParam):
        self.abort_if_todo_doesnt_exist(uidParam)
        ### Look here for Source
        return True

    def abort_if_todo_doesnt_exist(self, uid):
        if False:
            abort(404, message="There isn't any resource with that provided ID")
