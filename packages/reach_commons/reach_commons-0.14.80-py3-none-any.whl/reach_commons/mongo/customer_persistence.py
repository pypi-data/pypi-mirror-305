from urllib.parse import urlencode

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError

from reach_commons.app_logging.logger import get_reach_logger
from reach_commons.mongo.validation.customer import validate_customer


class MongoCustomerCRUD:
    def __init__(
        self,
        connection_info: dict,
        logger=get_reach_logger(),
    ):
        self.logger = logger
        self.mongo_client = MongoClient(
            "{}://{}:{}@{}/?{}".format(
                connection_info["schema"],
                connection_info["username"],
                connection_info["password"],
                connection_info["host"],
                urlencode(connection_info["extra_args"]),
            )
        )
        self.db = self.mongo_client.get_database(connection_info["database"])
        self.collection: Collection = self.db.get_collection("customers")

    def validate_and_execute(self, record: dict, operation: str):
        validation = validate_customer(record)
        if isinstance(validation, str):
            self.logger.error(f"Validation failed: {validation} - {str(record)}")
            raise ValueError(f"Validation failed: {validation} - {str(record)}")

        customer_id = record.get("customer_id")
        business_id = record.get("business_id")

        if not customer_id or not business_id:
            self.logger.error("Missing customer_id or business_id in record.")
            raise ValueError(
                "Both customer_id and business_id are required in the record."
            )

        query = {"customer_id": customer_id, "business_id": business_id}

        if operation == "upsert":
            self.upsert_record(query, record)
        elif operation == "insert":
            self.insert_record(record)
        elif operation == "update":
            self.update_record(query, record)
        elif operation == "delete":
            self.delete_record(query)
        else:
            raise ValueError(f"Invalid operation: {operation}")

    def upsert_record(self, query: dict, record: dict):
        self.logger.info(
            f"Upserting document for customer_id: {query['customer_id']}, business_id: {query['business_id']}."
        )
        update_fields = {"$set": record}
        if "updated_at" not in record:
            update_fields["$currentDate"] = {"updated_at": True}

        result = self.collection.update_one(query, update_fields, upsert=True)
        status_message = (
            f"Document for customer_id: {query['customer_id']}, business_id: {query['business_id']} "
            f"{'updated successfully.' if result.modified_count > 0 else ''}"
            f"{'inserted with ID: ' + str(result.upserted_id) if result.upserted_id else ''}"
            f"{'No documents were updated or inserted.' if result.modified_count == 0 and not result.upserted_id else ''}"
        )
        self.logger.info(status_message)

    def insert_record(self, record: dict):
        try:
            self.logger.info(
                f"Inserting document for customer_id: {record['customer_id']}, business_id: {record['business_id']}."
            )
            self.collection.insert_one(record)
        except DuplicateKeyError:
            self.logger.error(
                f"Document with customer_id {record['customer_id']} and business_id {record['business_id']} already exists."
            )

    def update_record(self, query: dict, record: dict):
        self.logger.info(
            f"Updating document for customer_id: {query['customer_id']}, business_id: {query['business_id']}."
        )
        self.collection.update_one(
            query,
            {"$set": record, "$currentDate": {"updated_at": True}},
            upsert=False,
        )

    def delete_record(self, query: dict):
        self.logger.info(
            f"Deleting document for customer_id: {query['customer_id']}, business_id: {query['business_id']}."
        )
        self.collection.delete_one(query)


"""
Uses example
connection_info = {
    "database":"db0",
    "schema": "mongodb+srv",
    "username": "databricks_rw",
    "password": "Lh4GsNx7cQUPtDmONqVGI9Dy7Jy6TbAxmq",
    "host": "cluster0.rwha2.mongodb.net",
    "extra_args": {
        "retryWrites": "true",
        "w": "majority",
        "appName": "Cluster0",
    },
}


mongo_crud = MongoCustomerCRUD(connection_info)

message = {
    "metadata": {"operation": "upsert"},
    "records": [{"customer_id": "123", "business_id": "456", "name": "John Doe"}],
}

for record in message["records"]:
    mongo_crud.validate_and_execute(record, message["metadata"]["operation"])
"""
