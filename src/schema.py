import typing

import strawberry
from strawberry.extensions.base_extension import SchemaExtension


@strawberry.type
class Book:
    title: str


@strawberry.type
class Query:
    books: typing.List[Book]


async def get_books():
    return [
        Book(title="The Great Gatsby"),
    ]


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


class TestExtension(SchemaExtension):
    def __init__(self):
        ...

    def on_execute(self):
        query_name = self.execution_context.operation_name
        yield
        try:
            assert query_name == self.execution_context.operation_name
        except AssertionError as e:
            print(
                "FAIL",
                "query before",
                query_name,
                "query after",
                self.execution_context.operation_name,
                "error",
                e,
            )


schema = strawberry.Schema(
    query=Query,
    extensions=[TestExtension()],
)
