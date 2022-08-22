from dataclasses import dataclass, field, asdict

@dataclass
class Comm:
    api_id:str
    
@dataclass
class RequestList:
    item_code:str
    shipping_date:str
    zaikosu:int
    
@dataclass
class RequestData:
    comm:Comm
    request_data:list(RequestList)
    
data1 = RequestData()
data1.comm.api_id="132123123"
arr=list(RequestList)
rq1=RequestList
rq1.item_code="A"
rq1.shipping_date="20220413"
rq1.zaikosu=12
arr.append(rq1)

data1.request_data=arr

print(data1)