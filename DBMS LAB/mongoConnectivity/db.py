def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client['DbmsPract']


if __name__ == "__main__":
    from createorder import createOrders
    dbname = get_database()
    collection_name = dbname["Connectivity"]
    itemArray = createOrders()
    collection_name.insert_many(itemArray)
