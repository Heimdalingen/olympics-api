# Assignment 1

## Introduction
This API will allow users to query a dataset related to the Olympic Games and their athletes. This includes queries like seeing which countries have the most medals and which countries have the most 

It will have a user system, where users will have a certain amount of tokens, and they will consume tokens as they use the API endpoints. They will start off with some points, buy will have to "buy" more to continue using the API.


### Technical
All endpoints start with `/v<major>.<minor>/...`
E.g., `/v1.2/user`
This includes when not specified in later endpoints.
Having versioning for the API means we can update our endpoints without making older versions outdated.

The user will have a certain amount of tokens. To make it simple, 1 API call costs 1 token.
This means the user will consume points, and will have to fill up every now and then.

All endpoints should support XML and JSON, even though all examples are given in JSON. Where it makes sense, you should/could also add CSV, or even PNG as a bar graph/plot of top 10. (Look up matplotlib.)


## Administrative endpoints
- `POST /user` creates user
- `GET /user` returns users
- `GET /user/<user-id>` returns user
- `PUT/PATCH /user/<user-id>` updates user
- `DEL /user/<user-id>` deletes user

- `POST /tokens` adds tokens to the user

### POST user
Input
```JSON
{
    "username": <string>,
    "email": <string>,
    "password": <string>,
    "authcode???": <string>,
    "admin": <bool>  // Only admins get to update dataset or modify other users
}
```

Return
```JSON
{
    "Status": <string>,  // E.g., "User created!". Or you can use status codes, e.g., 201, 404.
    "URI": <string>,  // E.g., /v1.2/user/104
    "Tokens": <int>  // Initial number of tokens. E.g., 10.
}
```

### POST tokens
Input
```JSON
{
    "tokens": <int>,  // Amount of tokens you wish to buy
    "username": <string>,
    "password": <string>
}
```

Return
```JSON
{
    "Status": <string>,
    "Bought": <int>,  // New tokens added
    "Tokens": <int>  // Total tokens owned
}
```


## Dataset endpoints
The Olympic games dataset has a bunch of data. We would like to be able to run some queries on it. E.g., `GET /medals/NOR` for all the medals Norway has won. You figure out which endpoints makes sense for you.


### POST result

```JSON
{
    // ... whatever data is required to add a new athlete-event.
}
```


### GETs
Notable endpoints

- `GET /athlete/<athlete-id>` returns all results from athlete. If requested CSV, return whole table. If JSON/XML, return medals, but also total medals, total golds, total ... etc.

- `GET /country/<country-id>` returns the same, but per country instead of per athlete.

- `GET /sport/<sport-id>` returns results for this sport.

- `GET /country?medals=gold&count=10` (or medals=all, etc.) should return the 10 countries with the most gold medals.
