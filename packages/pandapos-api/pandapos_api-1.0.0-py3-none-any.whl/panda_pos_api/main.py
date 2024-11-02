import datetime
from time import sleep
from typing import List
import requests
from panda_pos_api.graphql_query_builder import get_query_arguments
from graphql_query import Operation, Query, Field as GraphQLField
from panda_pos_api.models import OrderTag, Ticket, Product, ProductTag, TicketTag, TicketState
import json as json_module


class GraphQL:
    
    
    def __init__(self, username: str, password: str, client_id: str, client_secret: str, message_server_host: str, message_server_port: str) -> None:
        self.session = requests.Session()
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_expired_timestamp: int = None
        self.message_server_url = f"{message_server_host}:{message_server_port}"
        self.access_token = None
        self.headers = {
            "Authorization": ""
        }
    
    
    def request(self, url: str, method: str, data: dict = {}, params: dict = {}, json: dict = {}, timeout: int = 60, retry_timeout: int = 10):
        if self.access_token is None or  self.token_expired_timestamp < datetime.datetime.timestamp(datetime.datetime.now()):
            token_json = self.get_token()
            self.access_token = token_json["access_token"]
            self.token_expired_timestamp = datetime.datetime.timestamp(datetime.datetime.now()) + token_json["expires_in"]
        
        self.headers.update({"Authorization": f"Bearer {self.access_token}"})
        res = None
        while res is None:
            try:
                res = self.session.request(method=method, url=url, data=data, json=json, params=params, timeout=timeout, headers=self.headers)
            except requests.exceptions.ReadTimeout:
                print("Retry request...")
                sleep(retry_timeout)
                continue
        
        if res.json()["errors"]:
            with open("errors.json", "w") as f:
                json_module.dump(res.json(), f, indent=4)
            for error in res.json()["errors"]:
                
                print(f"""
                      Message: {error['innerException'].get('Message', '')}
                      Param: {error['innerException'].get('ParamName', '')}
                      """)
                print(error.get("message", ''))
            return None
        
        return res.json()
    
    def get_token(self):
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        
        res = self.session.post(f"{self.message_server_url}/Token", data=data)
        return res.json()
    
    def get_graphql_query_str(self, operation_type: str, operation_name: str, payload: dict, fields: list[str] = []):
        graphql_operation = Operation(
            name="m",
            type=operation_type,
            queries=[
                Query(
                    name=operation_name,
                    arguments=get_query_arguments(payload),
                    fields=fields,
                    
                    
                )
            ]
        )
        return graphql_operation.render()
    
    
    def register_terminal(self, user: str, ticketType: str, terminal: str, department: str) -> str:
        mutation_name = "registerTerminal"
        params = {
            "user": user,
            "ticketType": ticketType,
            "terminal": terminal,
            "department": department
        }
                
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, params),
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res["data"]["registerTerminal"]

    
    
    def unregister_terminal(self, id: str):
        params = {
            "terminalId": id,
        }
        
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", "unregisterTerminal", params),
        }
        
        self.request(f"{self.message_server_url}/api/graphql/", method="POST", json=payload)
        return "Ok."
    
    
    
    def create_ticket(self, ticket: Ticket):
        mutation_name = "addTicket"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, {"ticket": ticket.dict()}, fields=[]),
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res
    
    def create_terminal_ticket(self, terminal_id: str) -> str:
        mutation_name = "createTerminalTicket"
        params = {
            "terminalId": terminal_id 
        }
                
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, params, fields=["uid"]),
            
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res["data"]["createTerminalTicket"]["uid"]
    
    
    
    def add_product(self, product: Product):
        mutation_name = "addProduct"
        
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, product.dict(), fields=["id"]),
            
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        if res is None:
            return None
        
        return res["data"]["addProduct"]["id"]
    
    
    def get_product(self, name: str = "", id: str = ""):
        query_name = "getProduct"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("query", query_name, {"name": name, "id": id}, fields=["id", "name", "groupCode", "barcode", GraphQLField(name="portions", fields=["id", "name", "price"]), "tags"])
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        if res is None:
            return None
        
        return res["data"]["getProduct"]
    
    def get_all_products(self):
        query_name = "getProducts"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("query", query_name, {}, fields=["id", "name", "groupCode", "barcode", GraphQLField(name="portions", fields=["id", "name", "price"]), "tags"])
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res["data"]["getProducts"]
    
    def get_products_by_tag(self, productTag: ProductTag):
        query_name = "getProducts"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("query", query_name, {"itemTag": productTag.dict()}, fields=["id", "name", "groupCode", "barcode", GraphQLField(name="portions", fields=["id", "name", "price"]), "tags"])
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res["data"]["getProducts"]
    
    def get_products_by_barcode(self, barcode: str):
        query_name = "getProducts"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("query", query_name, {"barcode": barcode}, fields=["id", "name", "groupCode", "barcode", GraphQLField(name="portions", fields=["id", "name", "price"]), "tags"]),
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res["data"]["getProducts"]
    
    def get_products_by_groupCode(self, groupCode: str):
        query_name = "getProducts"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("query", query_name, {"groupCode": groupCode}, fields=["id", "name", "groupCode", "barcode", GraphQLField(name="portions", fields=["id", "name", "price"]), "tags"]),
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res["data"]["getProducts"]
    
    def ticket_refresh_message(self, id: int = 0):
        mutation_name = "postTicketRefreshMessage"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, {"id": id}, fields=["id"]),
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res["data"]
    
    def product_refresh_message(self):
        mutation_name = "postResetProductCacheMessage"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, {}, fields=[]),
        }
        
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res
    
    
    def add_order_to_terminal_ticket(self, terminal_id: str, product_name: str, quantity: float = 1, price: float = 0, enforce_quantity: bool = False, portion: str = "", order_tags: str = "", groupTagName: str = "", groupTagFormat: str = ""):
        mutation_name = "addOrderToTerminalTicket"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, {
                "terminalId": terminal_id,
                "productName": product_name,
                "quantity": quantity,
                "price": price,
                "enforceQuantity": enforce_quantity,
                "portion": portion,
                "orderTags": order_tags,
                "groupTagName": groupTagName,
                "groupTagFormat": groupTagFormat
                }, fields=["totalAmount", GraphQLField(name="orders", fields=["uid"])]),
        }        
        
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        
        return res["data"]["addOrderToTerminalTicket"]["orders"]
    
    
    def add_calculation_to_terminal_ticket(self, terminal_id: str, calculation_name: str, amount: float):
        mutation_name = "addCalculationToTerminalTicket"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, {
                "terminalId": terminal_id,
                "calculationName": calculation_name,
                "amount": amount
                }, fields=["totalAmount"]),
        }
        
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res["data"]["addCalculationToTerminalTicket"]["totalAmount"]
    
    
    def update_terminal_ticket(self, terminal_id: str, note: str, tags: list[TicketTag], states: list[TicketState]):
        mutation_name = "updateTerminalTicket"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, {
                "terminalId": terminal_id,
                "note": note,
                "tags": [tag.dict() for tag in tags],
                "states":[state.dict() for state in states]
                }, fields=["id"]),
        }
        
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res
    
    def close_terminal_ticket(self, terminal_id: str):
        mutation_name = "closeTerminalTicket"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, {"terminalId": terminal_id}, fields=[]),
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res
    
    def update_order_of_terminal_ticket(self, terminal_id: str, order_uid: str, orderTags: List[OrderTag]):
        mutation_name = "updateOrderOfTerminalTicket"
        payload = {
            "operationName": "m",
            "query": self.get_graphql_query_str("mutation", mutation_name, {
                "terminalId": terminal_id,
                "orderUid": order_uid,
                "orderTags": [orderTag.dict() for orderTag in orderTags]
                }, fields=[]),
        
        }
        res = self.request(f"{self.message_server_url}/api/graphql", method="POST", json=payload)
        return res
    
    
    