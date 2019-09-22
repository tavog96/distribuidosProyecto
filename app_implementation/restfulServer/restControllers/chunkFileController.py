from flask_restful import reqparse, abort, Resource

class chunkFileController(Resource):

    def __init__(self):
        super().__init__()

    def get(self, uidParam, chunkNumber):
        chunkNumberParam = False
        try:
            chunkNumberParam = int(chunkNumber)
        except:
            abort(404, message="A correct numeric Chunk index must be provided")
        abort_if_todo_doesnt_exist(uidParam)
        ### Look here for ChunkFile bianry content
        return True

    def abort_if_todo_doesnt_exist(self, uid):
        if False:
            abort(404, message="There isn't any resource with that provided ID")