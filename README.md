This repo shows an example of a bug where:

1. If async resolver
2. If extension is an instance

In extension, `self.execution_context` is not isolated between requests.


## How to run

Run server

```bash
pdm run server
```

Run test

```bash
pdm run test
```

## How to reproduce

Server will print out the following:

```
12:46:40 ❯ pdm run server
Running strawberry on http://0.0.0.0:8000/graphql 🍓
FAIL query before BookQuery_2 query after BookQuery_1 error
FAIL query before BookQuery_0 query after BookQuery_1 error
FAIL query before BookQuery_0 query after BookQuery_2 error
FAIL query before BookQuery_1 query after BookQuery_2 error
FAIL query before BookQuery_0 query after BookQuery_1 error
```

Here we can see that the `self.execution_context` is not isolated between requests.
