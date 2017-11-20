import models

##################################################################
#                   PUBLIC METHODS CRUD                          #
##################################################################


def store_json(tablename, jsondata):
    """
    Store json data into DB
    @parameter declaration
    tablename: the table to insert
    jsondata:  json data like {id:"123",name:"asf"}

    """
    table = getattr(models, tablename)
    table.objects.create(**jsondata)




def delete_json(tablename, filter=None):
    """
    Delete all data or qualified data
    @parameter declaration
    tablename: the table you want delete
    filter:  Filter condition use dict type to define the context

    """
    table = getattr(models, tablename)
    if filter:
        table.objects.filter(**filter).delete()
    else:
        table.objects.filter().delete()


def query_json(tablename, filter=None):
    """
    Returns all data or qualified data
    @parameter declaration
    tablename: The table name
    filter: Filter condition use dict type to define the context
    """
    table = getattr(models, tablename)
    if filter:
        querySet = table.objects.filter(**filter)
    else:
        querySet = table.objects.all()
    return querySet


def update(tablename, filter, context):
    """
    update qualified data
    @parameter declaration
    tablename: The table name
    filter: Filter condition use dict type to define the context
    context: The json data
    """
    table = getattr(models, tablename)
    table.objects.filter(**filter).update(**context)




