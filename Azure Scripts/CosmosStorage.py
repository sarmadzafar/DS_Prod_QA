from azure.cosmos import CosmosClient, PartitionKey, exceptions
from datasets import load_dataset



class DatabaseStorage:

    def __init__(self) -> None:
        self.endPoint = "https://productdevelopmentstorage.documents.azure.com:443/"
        self.primaryKey = "nVds9dPOkPuKu8RyWqigA1DIah4SVZtl1DIM0zDuRKd95an04QC0qv9TQIgrdtgluZo7Z0HXACFQgKgOQEAx1g=="
        self.client = CosmosClient(self.endPoint, self.primaryKey)

    def CreateDatabase(self, databaseName):
        database = self.client.create_database_if_not_exists(id=databaseName)


    def CreateContainer(self, databaseName, containerName) -> None:
        container_name = containerName
        database = self.client.get_database_client(databaseName)

        container = database.create_container_if_not_exists(
            id=container_name, 
            partition_key=PartitionKey(path="/id"),
            offer_throughput=400
        )

    def InsertPresetDataIntoContainer(self, databaseName, containerName) -> None:
        dataset = load_dataset("squad")

        database = self.client.get_database_client(databaseName)
        container = database.get_container_client(containerName)

        datatype = ""
        if (containerName == "squadtraincontainer"):
            datatype = "train"
        elif (containerName == "squadtestcontainer"):
            datatype = "validation"

        tracker = 0
        for i in dataset[datatype]:
            container.upsert_item(i)
            tracker = tracker + 1
            if (tracker % 1000 == 0):
                print(datatype + " - Batch number: " + str(tracker) + " Uploaded")

        print("Insertion Complete")
         


cosmosStorage = DatabaseStorage()
cosmosStorage.CreateDatabase("squadstorage")
cosmosStorage.CreateContainer("squadstorage","squadtraincontainer")
cosmosStorage.CreateContainer("squadstorage","squadtestcontainer")
cosmosStorage.InsertPresetDataIntoContainer("squadstorage","squadtraincontainer")

cosmosStorage.InsertPresetDataIntoContainer("squadstorage","squadtestcontainer")


























