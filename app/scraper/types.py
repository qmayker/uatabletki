from typing import NamedTuple 


class Item(NamedTuple):
    name:str 
    price:str

class Pharmacy(NamedTuple):
    name:str 
    items:list[list[Item]]