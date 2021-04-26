from arango import ArangoClient

def connect_system_db(password, host = 'http://localhost:8529'):
    '''
    Note: Default hosts is http://localhost:8529 and enter your database password \n
    Value: Return system db
    '''
    client = ArangoClient(hosts=host)
    sys_db = client.db('_system', username='root', password=password)
    
    return sys_db

def create_or_connect_db(dbname, username='root', password='Abcd@123'):
    '''
    Note: Default username is root and password is Abcd@123 \n
    Value: Create or connect db
    '''
    if not sys_db.has_database(dbname):
        sys_db.create_database(dbname)
    db = client.db(dbname, username=username, password=password)

def create_or_connect_collection(collectionname):
    '''
    Value: Return collection
    Enhence: Hash Index Fields
    '''
    if db.has_collection(collectionname):
        collectiondb = db.collection(collectionname)
    else:
        collectiondb = db.create_collection(collectionname)

    return collectiondb
   
    # Add a hash index to the collection.
    # students.add_hash_index(fields=['name'], unique=False)
    # Truncate the collection.
    # students.truncate()
