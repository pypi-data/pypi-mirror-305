# EasyPyDB - Beginner-Friendly Database Management for Python

EasyPyDB is a powerful yet simple SQLite database wrapper that makes database operations a breeze. Perfect for beginners and small to medium projects!

## 🌟 Features

- ✨ Intuitive, descriptive API
- 🔒 Automatic connection handling
- 💾 Backup & restore system
- 📤 CSV import/export
- 🔍 Full-text search
- 📊 Pagination support
- ⚡ Database indexing
- 🛠️ Schema modifications
- 📦 Zero dependencies!

## 📥 Installation & Setup

### Option 1: Direct Download
1. Download `EasyPyDB.py` from this repository
2. Place it in your project directory
3. Import and start using!

```python
from easypydb import EasyPyDB
```

### Option 2: Using pip (Coming Soon)
```bash
pip install python-easydb
```

### Option 3: Clone Repository
```bash
git clone https://github.com/yourusername/easydb.git
cd easypydb
python setup.py install
```

## 🚀 Quick Start

```python
from easypydb import EasyPyDB

# Create database with auto-backup
db = EasyPyDB('myapp.db', auto_backup=True)

# Create a users table
db.createTable('users',
    id = 'INTEGER PRIMARY KEY',
    name = 'TEXT NOT NULL',
    email = 'TEXT UNIQUE',
    age = 'INTEGER'
)

# Add a user
db.insertRecord('users', 
    name='John Doe',
    email='john@example.com',
    age=30
)

# Find user
user = db.getRecord('users', name='John Doe')
print(user)  # {'id': 1, 'name': 'John Doe', 'age': 30, 'email': 'john@example.com'}
```

## 📖 Complete Guide

### Database Setup

```python
# Basic setup
db = EasyPyDB('myapp.db')

# With automatic backups
db = EasyPyDB('myapp.db', auto_backup=True)

# Custom backup directory
db = EasyPyDB('myapp.db', auto_backup=True, backup_dir='my_backups')

# Using context manager (recommended)
with EasyPyDB('myapp.db') as db:
    # your code here
    pass
```

### Table Management

```python
# Create table
db.createTable('products',
    id = 'INTEGER PRIMARY KEY',
    name = 'TEXT NOT NULL',
    price = 'REAL',
    created_at = 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
)

# Add new column
db.addColumn('products', 'category', 'TEXT')

# Create index for faster searches
db.createIndex('products', 'name')
db.createIndex('products', 'category', unique=True)

# Get table information
tables = db.getTableNames()
schema = db.getTableSchema('products')
```

### Record Operations

```python
# Insert single record
user_id = db.insertRecord('users',
    name='John Doe',
    email='john@example.com',
    age=30
)

# Insert multiple records
db.insertMany('users', [
    {'name': 'Jane', 'email': 'jane@example.com', 'age': 25},
    {'name': 'Bob', 'email': 'bob@example.com', 'age': 35}
])

# Get records
user = db.getRecord('users', email='john@example.com')
adult_users = db.getAllRecords('users', age=30)

# Search records
results = db.searchRecords('users', ['name', 'email'], 'john')

# Update records
db.updateRecords('users', 
    where_conditions={'name': 'John'},
    age=31,
    status='active'
)

# Delete records
db.deleteRecords('users', email='john@example.com')
```

### Pagination

```python
# Get paginated results
page_number = 1
items_per_page = 10
records, total_count = db.getPaginatedRecords('users', 
    page=page_number, 
    per_page=items_per_page
)

print(f"Showing {len(records)} of {total_count} records")
```

### Data Import/Export

```python
# Export table to CSV
db.exportToCsv('users', 'users_backup.csv')

# Import data from CSV
db.importFromCsv('users', 'new_users.csv')
```

### Backup & Restore

```python
# Create manual backup
backup_path = db.createBackup()

# Create named backup
db.createBackup('before_update.backup')

# Restore from backup
db.restoreFromBackup('backups/myapp.db_20240324_123456.backup')
```

### Utility Functions

```python
# Count records
user_count = db.countRecords('users', status='active')

# Check existence
exists = db.recordExists('users', email='john@example.com')

# Get unique values
categories = db.getDistinctValues('products', 'category')

# Optimize database
db.vacuum()
```

## 💡 Examples

### User Authentication System

```python
# Setup users table
db.createTable('users',
    id = 'INTEGER PRIMARY KEY',
    username = 'TEXT UNIQUE NOT NULL',
    password_hash = 'TEXT NOT NULL',
    last_login = 'TIMESTAMP'
)

# Create indexes
db.createIndex('users', 'username', unique=True)

# Add user
def register_user(username, password_hash):
    if not db.recordExists('users', username=username):
        return db.insertRecord('users',
            username=username,
            password_hash=password_hash
        )
    return None

# Update last login
def update_login(user_id):
    db.updateRecords('users',
        where_conditions={'id': user_id},
        last_login='CURRENT_TIMESTAMP'
    )
```

### Product Inventory System

```python
# Setup inventory
db.createTable('inventory',
    id = 'INTEGER PRIMARY KEY',
    product_name = 'TEXT NOT NULL',
    quantity = 'INTEGER DEFAULT 0',
    price = 'REAL NOT NULL',
    last_updated = 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
)

# Add product
db.insertRecord('inventory',
    product_name='Awesome Widget',
    quantity=100,
    price=29.99
)

# Update stock
def update_stock(product_id, quantity_change):
    current = db.getRecord('inventory', id=product_id)
    new_quantity = current['quantity'] + quantity_change
    
    db.updateRecords('inventory',
        where_conditions={'id': product_id},
        quantity=new_quantity,
        last_updated='CURRENT_TIMESTAMP'
    )
```

### Indexes

Indexes are a powerful tool for improving query performance, especially for frequently searched columns. EasyPyDB makes it easy to create indexes on your tables:

```python
# Create index on email column (unique)
db.createIndex('users', 'email', unique=True)

# Create index on product name
db.createIndex('products', 'name')
```

When you create an index, EasyPyDB automatically names it based on the table and column names. The index name will be in the format `idx_{table}_{column}`.

Indexes work by maintaining a sorted data structure that allows the database to quickly locate the desired records. This is especially helpful for:

- Queries with `WHERE` clauses on indexed columns
- Queries that sort results by indexed columns
- Queries that join tables on indexed columns

**Best Practices for Indexes:**
- Index columns that are frequently used in `WHERE`, `JOIN`, and `ORDER BY` clauses
- Use unique indexes when the column values are guaranteed to be unique
- Avoid indexing columns with high cardinality (many unique values) as this can make the indexes large and inefficient
- Monitor index usage and remove unused indexes to save space

### Vacuum

Over time, as you insert, update, and delete records, the database file can become fragmented and inefficient. The `VACUUM` command can be used to reclaim unused space and optimize the database.

```python
db.vacuum()
```

It's a good idea to run `VACUUM` periodically, especially after major data modification operations. This can help improve query performance and reduce the database file size.

**When to run VACUUM:**
- After large delete or update operations
- Before creating a backup
- During periods of low database activity

### Pagination

When working with large datasets, it's important to use pagination to avoid overwhelming your application or the user. EasyDB makes this easy with the `getPaginatedRecords()` method:

```python
page = 1
per_page = 25

records, total_count = db.getPaginatedRecords('users', page=page, per_page=per_page)
print(f"Showing {len(records)} of {total_count} total users")
```

This method returns the records for the specified page, as well as the total number of records. You can use this information to display pagination controls in your application.

**Pagination Best Practices:**
- Use page and per_page parameters to control the number of records returned
- Adjust per_page value based on your application's needs and the user's device
- Display the total number of records to provide context for the pagination

By leveraging these optimization techniques, you can ensure your EasyPyDB-powered applications remain fast and efficient, even as your data grows.

## 🚦 Best Practices

1. **Use Context Managers**
   ```python
   with EasyDB('myapp.db') as db:
       db.insertRecord('users', name='John')
   ```

2. **Enable Auto-Backup for Important Data**
   ```python
   db = EasyDB('myapp.db', auto_backup=True)
   ```

3. **Create Indexes for Frequently Searched Columns**
   ```python
   db.createIndex('users', 'email', unique=True)
   ```

4. **Use Pagination for Large Datasets**
   ```python
   records, total = db.getPaginatedRecords('logs', page=1, per_page=50)
   ```

5. **Regular Maintenance**
   ```python
   # Optimize database periodically
   db.vacuum()
   ```

## ⚠️ Error Handling

```python
try:
    db.insertRecord('users',
        username='john',
        email='john@example.com'
    )
except Exception as e:
    print(f"Error: {e}")
finally:
    db.close()
```

## 🔍 Troubleshooting

Common issues and solutions:

1. **Database locked**
   - Make sure to close connections properly
   - Use context managers

2. **Unique constraint failed**
   - Check if record already exists before inserting
   - Use `recordExists()` method

3. **Table doesn't exist**
   - Verify table name with `getTableNames()`
   - Check if table was created successfully

## 📊 Performance Tips

1. Use indexes for frequently searched columns
2. Use pagination for large datasets
3. Run vacuum periodically
4. Create backups during low-traffic periods
5. Use bulk inserts instead of multiple single inserts

## 🚧 Limitations

- SQLite-only (no other databases supported)
- No built-in connection pooling
- Limited complex query building
- No ORM features
- No async support

## 🛠️ Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Support

If you found this helpful, please give it a ⭐!

---

Created with ❤️ by kserafin17