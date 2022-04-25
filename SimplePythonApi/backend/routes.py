import models
from flask import current_app as app
from flask_restful import Resource, reqparse


def initialize_routes(api):
    """POST AND GET"""
  
    api.add_resource(DocumentsApi, '/blog/documents')
    
    api.add_resource(GetDocumentsApi, '/blog/documents/<integer:recordId>')
                     
    """DELETE"""
    api.add_resource(DeleteDocumentsApi, '/blog/documents/<integer:relativePath>')  
    
    
    
@contextmanager
def session_scope():
    session = models.db.session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()



class DocumentsApi(Resource):

 
                    
    def post(self):

        print("Post data:{}".format(request.json), flush=True)
        data=request.json        
        name=data.get("name","Default name")
        type=data.get("type","Default type")
        source=data.get("name","Default source")
        blog=data.get("blog","Default blog")
        active=data.get("active",True)
        
              
        try:
            with session_scope() as session:
                new_document=models.Document(name,type,source,blog,active)
        except Exception as ex:
            return {"message": "An error occurred updating the item.{}".format(str(ex))}, 500
             
        return models.document_schema.dump(new_document)


class GetDocumentsApi(Resource):


    def get(self,recordId):
        print("Get recordId:{}".format(recordId), flush=True)
        try:
            with session_scope() as session:
                new_document=models.Document.query.filter_by(id=recordId).first()
        except Exception as ex:
            return {"message": "An error occurred updating the item.{}".format(str(ex))}, 500
        
        return models.document_schema.dump(new_document)
    
    
    

