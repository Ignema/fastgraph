import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from src.api.query import Query
from src.api.mutation import Mutation

app = FastAPI()

# GraphQL endpoint initialisation
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)