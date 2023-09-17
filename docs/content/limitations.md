# Limitations

:::{note}
_Almost_ all Python functionality is available in Brightway Live. However, there are some limitations. \
If you find that something is not working as expected, [please report it here](https://github.com/brightway-lca/brightway-live/discussions/new?category=report-limitation).
:::

## Filesystem (Data Storage)

### SQL Database Access

```{admonition} Related Issues
:class: note
https://github.com/brightway-lca/brightway-live/issues/10
```

Currently, an error is raised when trying to query a SQLite database in JupyterLite. This affects the use of Brightway, which stores data in sqlite databases through the `peewee` Python library. For instance, this simple test of the `peewee` library:

```python
from peewee import *

# Define a database object
db = SqliteDatabase('my_database.db')

# Define a model class
class Person(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db

# Create the table in the database
db.connect()
db.create_tables([Person])

person1 = Person(name='Alice', age=25)
person1.save()
```

raises the following error:

```
DatabaseError: database disk image is malformed
```

Instead of the default storage location a different location at `/tmp/` must be specified for the database. This is done [by setting the `BRIGHTWAY_DIR` environment variable](https://docs.brightway.dev/en/latest/content/faq/data_management.html#how-do-i-change-my-data-directory).

### Searchable Databases

```{admonition} Related Issues
:class: note
https://github.com/pyodide/pyodide/discussions/4150
```

### Restoring Brightway Project Backups (from `*.tar.gz`)

```{admonition} Related Issues
:class: note
https://github.com/brightway-lca/brightway-live/issues/37 \
https://github.com/jupyterlite/jupyterlite/issues/1153
```

### Download Databases (eg. USEEIO)

```{admonition} Related Issues
:class: note
test
```