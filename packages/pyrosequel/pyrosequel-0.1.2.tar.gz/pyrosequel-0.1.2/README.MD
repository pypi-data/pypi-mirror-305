# PyroSequel
PyroSequel is a small and asynchronous ORM / SQL query builder. PyroSequel started as a wrapper for the `aiosqlite` library, but now supports using different databases.

Right now, only `SQLiteDatabase` is implemented (using aiosqlite).

# Installation
To install PyroSequel with SQLite support, run this:

> $ pip install pyrosequel

# Example
Here's a small example, showcasing simple use case for the PyroSequel.

```py
import asyncio
from pyrosequel import *

async def main():
    db = await SQLiteDatabase.connect(":memory:")

    @db.register_model()
    class User(Model):
        id = IntegerField(PrimaryKey())
        name = TextField(NotNull())
    
    await User.create_table()

    # insert to specified column
    await User.insert(
        (User.name, "gecko")
    ).cast()

    # or just pass values in
    await User.insert(None, "zedikon").cast()

    # now fetch the user
    print(await User.select()
                    .where(User.name == "gecko")
                    .cast())
    # [(1, 'gecko')]
```

# Licensing
This project is licensed under BSD 3-clause licese. See LICENSE file for more.