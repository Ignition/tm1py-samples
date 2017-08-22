""" 
- Create a subset
- Query and manipulate it
- Push it back to TM1
- Delete it
"""

import uuid

from TM1py.Objects import Subset
from TM1py.Services import TM1Service


with TM1Service(address='localhost', port=8001, user='admin', password='apple', ssl=True) as tm1:

    # get a random string that we can use a subset name
    subset_name = str(uuid.uuid4())

    # create subset
    s = Subset(dimension_name='Plan_Department', subset_name=subset_name, alias='', elements=['200', '405', '410'])
    tm1.subsets.create(s, True)

    # get it and print out the elements
    s = tm1.subsets.get(dimension_name='Plan_Department', subset_name=subset_name, private=True)
    print(s.elements)

    # update it
    s.add_elements(['105', '115'])
    tm1.subsets.update(s, True)

    # get it and print out the elements
    s = tm1.subsets.get(dimension_name='Plan_Department', subset_name=subset_name, private=True)
    print(s.elements)

    # delete it
    tm1.subsets.delete(dimension_name='Plan_Department', subset_name=subset_name, private=True)

