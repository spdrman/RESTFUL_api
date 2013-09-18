RESTFUL_api
===========

Example of a Restful Web Service using python Web2py

The model contains a "company" table, and a "employee" table.
Each employee had an employer (foreign key for "company" table)

You can drive the API using the GUI or by sending requests to /default/api/WhatEver.json
Example of allowed GET patterns :

    /companies[company]
    /company/id/{company.id}
    /company/name/{company.name.contains}
    /company/id/{company.id}/:field
    /company/id/{company.id}/employees[employee.employer]
    /company/id/{company.id}/employee[employee.employer]/name/{employee.name.contains}
    /company/id/{company.id}/employee[employee.employer]/id/{employee.id}
    /company/id/{company.id}/employee[employee.employer]/id/{employee.id}/:field
