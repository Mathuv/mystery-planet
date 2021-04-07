# Persons
Supports CRUD and other operations on person records.


## Get employees of a company (1)

Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.

**Request**

`GET` `/companies/<index>/employees`

Parameters:

Name       | Type   | Description
-----------|--------|---
index      | integer| ID value of the company object

**Response**

```json
Content-Type application/json
200 Ok

{
  "count": 7,
  "next": null,
  "previous": null,
  "results": [
    {
      "index": 289,
      "created_at": "2021-04-06T09:06:16+0000",
      "updated_at": "2021-04-06T09:06:16+0000",
      "guid": "faac24dc-48ce-4998-9846-a899b163bee0",
      "name": "Frost Foley",
      "age": 22,
      "gender": "male",
      "has_died": true,
      "picture": "http://placehold.it/32x32",
      "balance": "1328.74",
      "eye_color": "blue",
      "phone": "+1 (987) 436-3916",
      "address": "824 Clark Street, Utting, New Mexico, 3994",
      "about": "Cillum fugiat velit cillum nisi do esse id aute anim. Ut ullamco aliqua non dolor officia sint voluptate fugiat Lorem dolor fugiat dolore eu. Non consectetur minim aute tempor qui minim.\r\n",
      "greeting": "Hello, Frost Foley! You have 1 unread messages.",
      "tags": [
        "consectetur",
        "cillum",
        "ea",
        "do",
        "sunt",
        "aliqua",
        "incididunt"
      ],
      "registered": "2017-05-22T14:40:47+0000",
      "company": 1,
      "favourite_foods": [
        "banana",
        "beetroot",
        "celery",
        "orange"
      ],
      "friends": [
        0,
        1,
        2,
        3,
        4,
        5
      ]
    },
    {
      "index": 580,
      "created_at": "2021-04-06T09:06:20+0000",
      "updated_at": "2021-04-06T09:06:20+0000",
      "guid": "ba65b636-fab9-4813-809a-0e663cff5473",
      "name": "Luna Rodgers",
      "age": 56,
      "gender": "male",
      "has_died": true,
      "picture": "http://placehold.it/32x32",
      "balance": "1310.82",
      "eye_color": "blue",
      "phone": "+1 (889) 544-3275",
      "address": "430 Frank Court, Camino, American Samoa, 2134",
      "about": "Commodo cillum dolor sit aute commodo. Eiusmod deserunt et do nulla officia aliqua qui irure. Laborum anim adipisicing mollit nostrud eiusmod aliqua occaecat do cillum elit culpa ea incididunt.\r\n",
      "greeting": "Hello, Luna Rodgers! You have 7 unread messages.",
      "tags": [
        "commodo",
        "proident",
        "magna",
        "ullamco",
        "proident",
        "labore",
        "ipsum"
      ],
      "registered": "2015-09-07T18:26:03+0000",
      "company": 1,
      "favourite_foods": [
        "banana",
        "beetroot",
        "celery",
        "cucumber"
      ],
      "friends": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15
      ]
    }
  ]
}
```

## Get a list of common friends given two people

Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.

**Request**

`GET` `/persons/<person_1_index>/common-friends/<person_2_index>`

Parameters:

Name           | Type    | Description
---------------|---------|---
person_2_index | integer | ID value of the first person object
person_2_index | integer | ID value of the second person object


**Response**

```json
Content-Type application/json
200 Ok


{
  "person_1": {
    "name": "Vasquez Evans",
    "age": 31,
    "address": "599 Provost Street, Chesterfield, New Jersey, 872",
    "phone": "+1 (834) 544-2792"
  },
  "person_2": {
    "name": "Shauna Mann",
    "age": 35,
    "address": "692 Jackson Court, Vienna, Puerto Rico, 2919",
    "phone": "+1 (876) 519-3737"
  },
  "common_friends": [
    {
      "name": "Decker Mckenzie",
      "age": 60,
      "address": "492 Stockton Street, Lawrence, Guam, 4854",
      "phone": "+1 (893) 587-3311"
    },
    {
      "name": "Mindy Beasley",
      "age": 62,
      "address": "628 Brevoort Place, Bellamy, Kansas, 2696",
      "phone": "+1 (862) 503-2197"
    }
  ]
}

```

## Get a list of fruits and vegetables a person likes.

Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

**Request**

`GET` `/persons/<index>/favourite-food`

Parameters:

Name       | Type    | Description
-----------|---------|---
index      | integer | ID value of the person object


**Response**

```json
Content-Type application/json
200 Ok

{
  "name": "Dawn Marshall",
  "age": 42,
  "fruits": [
    "banana",
    "orange",
    "strawberry"
  ],
  "vegetables": [
    "beetroot"
  ]
}
```


## Get employees of a company (2)

This is second method to retrieve all the employees of a company which is based on filtering against the resource 'persons'.

**Request**

`GET` `/persons/?company=<index>`

Parameters:

Name       | Type    | Description
-----------|---------|---
index      | integer | The ID value of the company object


**Response**

```json
Content-Type application/json
200 Ok


{
  "count": 7,
  "next": null,
  "previous": null,
  "results": [
    {
      "index": 289,
      "created_at": "2021-04-06T09:06:16+0000",
      "updated_at": "2021-04-06T09:06:16+0000",
      "guid": "faac24dc-48ce-4998-9846-a899b163bee0",
      "name": "Frost Foley",
      "age": 22,
      "gender": "male",
      "has_died": true,
      "picture": "http://placehold.it/32x32",
      "balance": "1328.74",
      "eye_color": "blue",
      "phone": "+1 (987) 436-3916",
      "address": "824 Clark Street, Utting, New Mexico, 3994",
      "about": "Cillum fugiat velit cillum nisi do esse id aute anim. Ut ullamco aliqua non dolor officia sint voluptate fugiat Lorem dolor fugiat dolore eu. Non consectetur minim aute tempor qui minim.\r\n",
      "greeting": "Hello, Frost Foley! You have 1 unread messages.",
      "tags": [
        "consectetur",
        "cillum",
        "ea",
        "do",
        "sunt",
        "aliqua",
        "incididunt"
      ],
      "registered": "2017-05-22T14:40:47+0000",
      "company": 1,
      "favourite_foods": [
        "banana",
        "beetroot",
        "celery",
        "orange"
      ],
      "friends": [
        0,
        1,
        2,
        3,
        4,
        5
      ]
    },
    {
      "index": 580,
      "created_at": "2021-04-06T09:06:20+0000",
      "updated_at": "2021-04-06T09:06:20+0000",
      "guid": "ba65b636-fab9-4813-809a-0e663cff5473",
      "name": "Luna Rodgers",
      "age": 56,
      "gender": "male",
      "has_died": true,
      "picture": "http://placehold.it/32x32",
      "balance": "1310.82",
      "eye_color": "blue",
      "phone": "+1 (889) 544-3275",
      "address": "430 Frank Court, Camino, American Samoa, 2134",
      "about": "Commodo cillum dolor sit aute commodo. Eiusmod deserunt et do nulla officia aliqua qui irure. Laborum anim adipisicing mollit nostrud eiusmod aliqua occaecat do cillum elit culpa ea incididunt.\r\n",
      "greeting": "Hello, Luna Rodgers! You have 7 unread messages.",
      "tags": [
        "commodo",
        "proident",
        "magna",
        "ullamco",
        "proident",
        "labore",
        "ipsum"
      ],
      "registered": "2015-09-07T18:26:03+0000",
      "company": 1,
      "favourite_foods": [
        "banana",
        "beetroot",
        "celery",
        "cucumber"
      ],
      "friends": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15
      ]
    }
  ]
}

```

## Get all the person records

**Request**

`GET` `/persons/`

**Response**:

```json
Content-Type application/json
200 Ok

{
  "count": 991,
  "next": "http://localhost:8000/api/v1/persons/?format=json&page=2",
  "previous": null,
  "results": [
    {
      "index": 0,
      "created_at": "2021-04-05T21:38:36+0000",
      "updated_at": "2021-04-05T21:38:36+0000",
      "guid": "5e71dc5d-61c0-4f3b-8b92-d77310c7fa43",
      "name": "Carmella Lambert",
      "age": 61,
      "gender": "female",
      "has_died": true,
      "picture": "http://placehold.it/32x32",
      "balance": "2418.59",
      "eye_color": "blue",
      "phone": "+1 (910) 567-3630",
      "address": "628 Sumner Place, Sperryville, American Samoa, 9819",
      "about": "Non duis dolore ad enim. Est id reprehenderit cupidatat tempor excepteur. Cupidatat labore incididunt nostrud exercitation ullamco reprehenderit dolor eiusmod sit exercitation est. Voluptate consectetur est fugiat magna do laborum sit officia aliqua magna sunt. Culpa labore dolore reprehenderit sunt qui tempor minim sint tempor in ex. Ipsum aliquip ex cillum voluptate culpa qui ullamco exercitation tempor do do non ea sit. Occaecat laboris id occaecat incididunt non cupidatat sit et aliquip.\r\n",
      "greeting": "Hello, Carmella Lambert! You have 6 unread messages.",
      "tags": [
        "id",
        "quis",
        "ullamco",
        "consequat",
        "laborum",
        "sint",
        "velit"
      ],
      "registered": "2016-07-13T22:29:07+0000",
      "company": 58
    },
    {
      "index": 1,
      "created_at": "2021-04-05T21:38:36+0000",
      "updated_at": "2021-04-05T21:38:36+0000",
      "guid": "b057bb65-e335-450e-b6d2-d4cc859ff6cc",
      "name": "Decker Mckenzie",
      "age": 60,
      "gender": "male",
      "has_died": false,
      "picture": "http://placehold.it/32x32",
      "balance": "1562.58",
      "eye_color": "brown",
      "phone": "+1 (893) 587-3311",
      "address": "492 Stockton Street, Lawrence, Guam, 4854",
      "about": "Consectetur aute consectetur dolor aliquip dolor sit id. Sint consequat anim occaecat ad mollit aliquip ut aute eu culpa mollit qui proident eu. Consectetur ea et sit exercitation aliquip officia ea aute exercitation nulla qui sunt labore. Enim veniam labore do irure laborum aute exercitation consectetur. Voluptate adipisicing velit sunt consectetur id sint adipisicing elit elit pariatur officia amet officia et.\r\n",
      "greeting": "Hello, Decker Mckenzie! You have 2 unread messages.",
      "tags": [
        "veniam",
        "irure",
        "mollit",
        "sunt",
        "amet",
        "fugiat",
        "ex"
      ],
      "registered": "2017-06-25T20:03:49+0000",
      "company": 98
    },
  ]
}
```

## Get a person details

**Request**

`GET` `/persons/<index>/`

Parameters:

Name       | Type    | Description
-----------|---------|---
index      | integer | The ID value of the person object


**Response**

```json
Content-Type application/json
200 OK


{
  "index": 100,
  "created_at": "2021-04-06T09:06:13+0000",
  "updated_at": "2021-04-06T09:06:13+0000",
  "guid": "02e9bdf3-f90d-4f4f-8a2e-eeb2cde8a8de",
  "name": "Vasquez Evans",
  "age": 31,
  "gender": "male",
  "has_died": true,
  "picture": "http://placehold.it/32x32",
  "balance": "1946.37",
  "eye_color": "blue",
  "phone": "+1 (834) 544-2792",
  "address": "599 Provost Street, Chesterfield, New Jersey, 872",
  "about": "Magna nisi dolor cillum sit aute non tempor duis. Duis do anim commodo incididunt duis voluptate fugiat ex commodo occaecat ad irure aute et. Proident veniam ipsum cupidatat id. Veniam et ullamco ipsum in laboris pariatur id esse fugiat. Adipisicing reprehenderit occaecat dolore minim ipsum aliquip cupidatat enim est incididunt excepteur id sint ea.\r\n",
  "greeting": "Hello, Vasquez Evans! You have 1 unread messages.",
  "tags": [
    "laborum",
    "duis",
    "ad",
    "reprehenderit",
    "eiusmod",
    "commodo",
    "excepteur"
  ],
  "registered": "2015-11-18T12:08:24+0000",
  "company": 67,
  "favourite_foods": [
    "beetroot",
    "carrot",
    "celery",
    "orange"
  ],
  "friends": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14
  ]
}

```
