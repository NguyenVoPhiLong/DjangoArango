from django.shortcuts import render
from django.http import request
from home.alib import *

# Create your views here.


def excute(request):
    sys_db = connect_system_db('Abcd@123')
    create_or_connect_db('CourseManagement')
    cltcourse = create_or_connect_collection('Course')

    # Insert new documents into the collection.

    courses.insert({'name': 'jane', 'age': 19})
    courses.insert({'name': 'josh', 'age': 18})
    students.insert({'name': 'jake', 'age': 21})

    # Execute an AQL query. This returns a result cursor.
    cursor = db.aql.execute('FOR doc IN students RETURN doc')

    # Iterate through the cursor to retrieve the documents.
    student_names = [document['name'] for document in cursor]

    context = {

    }
    
    return render(request, 'home/index.html', context)

