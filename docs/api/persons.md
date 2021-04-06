# Persons
Supports CRUD operations on person records.

## Get employees of a company

**Request**

`GET` `/persons/?company=:company_id`

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
      "created_at": "2021-04-05T13:27:22+0000",
      "updated_at": "2021-04-05T13:27:22+0000",
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
      "company": 1
    },
    {
      "index": 580,
      "created_at": "2021-04-05T13:27:22+0000",
      "updated_at": "2021-04-05T13:27:22+0000",
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
      "company": 1
    },
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

`GET` `/persons/:id/`

**Response**

```json
Content-Type application/json
200 OK

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
}
```
