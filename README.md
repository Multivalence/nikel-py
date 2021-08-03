# nikel-py

[![PyPI](https://img.shields.io/pypi/v/nikel-py.svg)](https://pypi.org/project/nikel-py/) [![Versions](https://img.shields.io/pypi/pyversions/nikel-py.svg)](https://pypi.org/project/nikel-py/) [![Build Status](https://api.travis-ci.com/Multivalence/nikel-py.svg?branch=master)](https://travis-ci.com/github/Multivalence/nikel-py)

A modern, easy to use, async and sync API wrapper for the nikel API written in Python.

## Key Features

- Gather Data about UofT Courses, Programs, Textbooks, Services, and more
- Gather Data asynchronously so main event loop isn't blocked

## Installation

**Python 3.6 or higher is required**

```shell
#Linux/macOS
python3 -m pip install -U nikel-py

#Windows
py -3 -m pip install -U nikel-py
```

## Current list of endpoints

- Courses
- Programs
- Textbooks
- Examples
- Evals
- Food
- Services
- Buildings
- Parking


## Methods

- ```get(query : Dict, limit : int=10)``` Synchronous
- ```async_get(query : Dict, limit : int=10)``` Asynchronous

## Basic Examples

### Synchronous

```py
from nikel_py import Courses

#Creates a list (limited to 1) of courses that have the name 'Introduction to Computer Programming'
x = Courses.get({'name' : 'Introduction to Computer Programming'}, limit=1)

print(x[0].code)

# >> CSC108H1
```

### Asynchronous

```py
import asyncio
from nikel_py import Textbooks

async def main():
    
    #Creates a list (limited to 1) of Textbooks that have the ID '10552179'
    x = await Textbooks.async_get({'id' : '10552179'}, limit=1)
    print(x[0].name)
    

asyncio.run(main())

# >> Where The Wild Things Are
```

## Advanced Examples (Filtering & Extra Fields)

### Synchronous

```py
from nikel_py import Foods

#Creates a list (limited to 10) of Restaurants that provide Gluten Free Foods
x = Foods.get({'attributes' : '~Gluten Free'}, limit=10)

print(x[0].address)

# >> 89 Chestnut Street, Toronto, ON M5G 1R1
```

### Asynchronous

```py
import asyncio
from nikel_py import Programs

async def main():
    
    #Creates a list (limited to 1) of Programs that start with Computer Science and are done at the St. George Campus
    x = await Programs.async_get({'campus' : 'St. George', 'name' : '(Computer Science'}, limit=1)
    print(x[0].type)
    

asyncio.run(main())

# >> major
```

## Filters
| Operator | String | Numerical/Boolean |
| ----------- | ----------- | -----------|
|  | Fuzzy Search | Equality |
| = | Equality | Equality |
| ! | Inequality | Inequality |
| < | N/A | Less than |
| <= | N/A | Less than or equal to |
| \> | N/A | Greater than |
| \>= | N/A | Greater than or equal to |
| ( | Starts with | N/A |
| ) | Ends with | N/A |
| ~ | Serialization | N/A |

*Note: the `~` operator essentially "yolos" and tries to search within nested arrays and hard to navigate nested structures.*

**For more information. Please go [Here](https://docs.nikel.ml/docs/query_guide)**


## Query & Properties Lookup Table

| Courses | Programs | Textbooks | Exams | Evals | Food | Services | Buildings | Parking
| ----------- | ----------- | -----------|----------- | ----------- | -----------| ----------- | ----------- | -----------|
| id | id | id | id | id | id | id | id | id
| code | name | isbn | course_id | name | name | name | code | name 
| name | type | title | course_code | campus | description | alias | tags | alias 
| description | campus | edition | campus | terms | tags | building_id | name | building_id
| division | description | author | date | last_updated | campus | description | short_name | description
| department | enrollment | image | start | | address | campus | address | campus
| prerequisites | completion | price | end | | coordinates | address | coordinates | address
| corequisites |last_updated | url | duration | | hours | image | last_updated | coordinates
| exclusions |              | courses | sections | | image | coordinates | | last_updated
| recommended_preparation | | last_updated | last_updated | | url | tags |
| level | | | | | twitter | attributes |
| campus | | | | | facebook | last_updated |
| term | | | | | attributes |
| arts_and_science_breadth | | | | | last_updated |
| arts_and_science_distribution |
| utm_distribution |
| utsc_breadth |
| apsc_electives |
| meeting_sections |
| last_updated |

**For more info please refer to the Schemas of each Endpoint [Here](https://docs.nikel.ml/docs/)**

