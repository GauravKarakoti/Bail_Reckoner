from pymongo import MongoClient

def connect_to_mongo(uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def find_section_info(section_number):
    uri = "mongodb+srv://sharmabhishek:shinchan@cluster0.lbb24.mongodb.net/"
    db_name = "ipc_sections"
    collection_name = "noidea"
    
    collection = connect_to_mongo(uri, db_name, collection_name)
    retrieve="IPC_"+str(section_number)
    query = {"Section": retrieve}
    result = collection.find_one(query)
    if result:
        if result['Bailable']==True:
            output=f'''It is bailable offense.
            The offense is {result['Offense']}.
            The punishment is {result['Punishment']}
            {result['Description']}'''
        else:
            output=output=f'''Sadly , It is a non bailable offense.
            The offense is {result['Offense']}.
            The punishment is {result['Punishment']}
            {result['Description']}'''
        return output
    else:
        return "No information found for this section."


