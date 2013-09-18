db.define_table('company',Field('name'),Field('info'))
db.define_table('employee',Field('employer',db.company),Field('name'),Field('info'))