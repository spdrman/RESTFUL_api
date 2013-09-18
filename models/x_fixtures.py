#Populate the database with default values...
if db(db.company).count() == 0:
    db.company.insert(
        name='Python Constructor',
        info='This is a great company...'
)
company = db(db.company.name == 'Python Constructor').select().first()
if company:
    if db(db.employee.employer == company).count() == 0:
        db.employee.insert(
            employer = company,
            name='espern',
            info='nice guy!'
        )