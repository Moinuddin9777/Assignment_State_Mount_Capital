from datetime import datetime
from lib2to3.pgen2 import token
from sqlite3 import Timestamp
from unittest import result
import graphene
import json


class Coin(graphene.ObjectType):
    id = graphene.ID()
    token = graphene.String()
    Timestamp = graphene.DateTime()



class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_Users(self, info):
        return [
            Coin(token='Uniswap',id=, Timestamp=datetime.now()),
            Coin(token='WrappedEthereum',id=, Timestamp=datetime.now()),
            Coin(token='Ethereum',id=, Timestamp=datetime.now()),
        ]



schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        Coin{
            token
            timestamp
        }
    }
    '''
)

items = dict(result.data.items())
print(json.dumps(items, indent=4))