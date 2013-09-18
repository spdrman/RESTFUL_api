# -*- coding: utf-8 -*-

patterns = [
            "/companies[company]",
            "/company/id/{company.id}",
            "/company/name/{company.name.contains}",
            "/company/id/{company.id}/:field",
            "/company/id/{company.id}/employees[employee.employer]",
            "/company/id/{company.id}/employee[employee.employer]/name/{employee.name.contains}",
            "/company/id/{company.id}/employee[employee.employer]/id/{employee.id}",
            "/company/id/{company.id}/employee[employee.employer]/id/{employee.id}/:field"
            ]

@request.restful()
def api():
    def GET(*args,**vars):
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(table_name,**vars):
        return db[table_name].validate_and_insert(**vars)
    def PUT(table_name,record_id,**vars):
        return db(db[table_name]._id==record_id).update(**vars)
    def DELETE(table_name,record_id):
        return db(db[table_name]._id==record_id).delete()
    return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)

def index():
    return dict(patterns=patterns)

def user():
    return dict(form=auth())

@cache.action()
def download():
    return response.download(request, db)

def call():
    return service()

@auth.requires_signature()
def data():
    return dict(form=crud())
