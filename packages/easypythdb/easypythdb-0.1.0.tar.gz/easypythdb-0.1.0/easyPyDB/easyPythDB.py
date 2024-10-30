import sqlite3
from typing import List, Dict, Any, Union, Optional, Tuple
from contextlib import contextmanager
from datetime import datetime, timedelta
import json
import os
import csv
import shutil
from pathlib import Path


class EasyPythDB:
    """A super simple database manager with powerful features."""

    def __init__(
        self, db_name: str, auto_backup: bool = False, backup_dir: str = "backups"
    ):
        """
        Initialize database with optional auto-backup.

        Args:
            db_name (str): Database name (e.g., 'myapp.db')
            auto_backup (bool): Enable automatic backups
            backup_dir (str): Directory for backups
        """
        self.db_name = db_name
        self.auto_backup = auto_backup
        self.backup_dir = backup_dir
        self._connect()

        if auto_backup:
            os.makedirs(backup_dir, exist_ok=True)

    def _connect(self):
        """Connect to database with dictionary cursor."""
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row

    def createBackup(self, backup_name: str = None) -> str:
        """Create a backup of the database."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = backup_name or f"{self.db_name}_{timestamp}.backup"
        backup_path = os.path.join(self.backup_dir, backup_name)
        shutil.copy2(self.db_name, backup_path)
        return backup_path

    def restoreFromBackup(self, backup_path: str) -> bool:
        """Restore database from a backup file."""
        try:
            self.close()
            shutil.copy2(backup_path, self.db_name)
            self._connect()
            return True
        except Exception as e:
            self._connect()
            raise Exception(f"Failed to restore backup: {e}")

    def createTable(self, table_name: str, **columns):
        """
        Create a new table with specified columns.

        Example:
            db.createTable('users',
                id = 'INTEGER PRIMARY KEY',
                name = 'TEXT NOT NULL',
                age = 'INTEGER'
            )
        """
        cols = ", ".join(f"{col} {type_}" for col, type_ in columns.items())
        self.executeQuery(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})")

    def insertRecord(self, table_name: str, **data) -> int:
        """
        Insert a single record into table.

        Example:
            db.insertRecord('users', name='John', age=30)
        """
        cols = ", ".join(data.keys())
        vals = ", ".join(["?" for _ in data])
        query = f"INSERT INTO {table_name} ({cols}) VALUES ({vals})"
        return self.executeQuery(query, list(data.values()))

    def insertMany(self, table_name: str, records: List[Dict]) -> None:
        """Insert multiple records at once."""
        if not records:
            return
        cols = ", ".join(records[0].keys())
        vals = ", ".join(["?" for _ in records[0]])
        query = f"INSERT INTO {table_name} ({cols}) VALUES ({vals})"
        self.executeManyQueries(query, [list(r.values()) for r in records])

    def getRecord(self, table_name: str, **conditions) -> Optional[Dict]:
        """Get first record matching conditions."""
        where, values = self._buildWhereClause(conditions)
        query = f"SELECT * FROM {table_name} {where} LIMIT 1"
        return self.fetchOne(query, values)

    def getAllRecords(self, table_name: str, **conditions) -> List[Dict]:
        """Get all records matching conditions."""
        where, values = self._buildWhereClause(conditions)
        query = f"SELECT * FROM {table_name} {where}"
        return self.fetchAll(query, values)

    def searchRecords(
        self, table_name: str, columns: List[str], search_term: str
    ) -> List[Dict]:
        """
        Search for records where any specified column contains the search term.

        Example:
            db.searchRecords('users', ['name', 'email'], 'john')
        """
        conditions = " OR ".join([f"{col} LIKE ?" for col in columns])
        query = f"SELECT * FROM {table_name} WHERE {conditions}"
        params = [f"%{search_term}%" for _ in columns]
        return self.fetchAll(query, params)

    def updateRecords(self, table_name: str, where_conditions: Dict, **new_values):
        """Update records matching conditions."""
        set_clause = ", ".join(f"{k} = ?" for k in new_values.keys())
        where_clause = " AND ".join(f"{k} = ?" for k in where_conditions.keys())
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
        values = list(new_values.values()) + list(where_conditions.values())
        self.executeQuery(query, values)

    def deleteRecords(self, table_name: str, **conditions):
        """Delete records matching conditions."""
        where, values = self._buildWhereClause(conditions)
        query = f"DELETE FROM {table_name} {where}"
        self.executeQuery(query, values)

    def countRecords(self, table_name: str, **conditions) -> int:
        """Count records matching conditions."""
        where, values = self._buildWhereClause(conditions)
        query = f"SELECT COUNT(*) as count FROM {table_name} {where}"
        result = self.fetchOne(query, values)
        return result["count"] if result else 0

    def recordExists(self, table_name: str, **conditions) -> bool:
        """Check if any records exist matching conditions."""
        return self.countRecords(table_name, **conditions) > 0

    def getTableNames(self) -> List[str]:
        """Get list of all tables in database."""
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        return [row["name"] for row in self.fetchAll(query)]

    def getTableSchema(self, table_name: str) -> List[Dict]:
        """Get detailed schema information for table."""
        return self.fetchAll(f"PRAGMA table_info({table_name})")

    def clearTable(self, table_name: str):
        """Delete all records from table."""
        self.executeQuery(f"DELETE FROM {table_name}")

    def dropTable(self, table_name: str):
        """Drop table from database."""
        self.executeQuery(f"DROP TABLE IF EXISTS {table_name}")

    def exportToCsv(self, table_name: str, file_path: str):
        """Export table data to CSV file."""
        data = self.getAllRecords(table_name)
        if not data:
            return

        with open(file_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def importFromCsv(self, table_name: str, file_path: str):
        """Import data from CSV file into table."""
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            self.insertMany(table_name, list(reader))

    def addColumn(self, table_name: str, column_name: str, column_type: str):
        """Add new column to existing table."""
        self.executeQuery(
            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"
        )

    def getDistinctValues(self, table_name: str, column_name: str) -> List[Any]:
        """Get distinct values in a column."""
        query = f"SELECT DISTINCT {column_name} FROM {table_name}"
        return [row[column_name] for row in self.fetchAll(query)]

    def getPaginatedRecords(
        self, table_name: str, page: int = 1, per_page: int = 10
    ) -> Tuple[List[Dict], int]:
        """
        Get paginated records with total count.

        Returns:
            Tuple[List[Dict], int]: (records, total_count)
        """
        total = self.countRecords(table_name)
        offset = (page - 1) * per_page
        query = f"SELECT * FROM {table_name} LIMIT ? OFFSET ?"
        records = self.fetchAll(query, (per_page, offset))
        return records, total

    def executeQuery(self, query: str, params: tuple = ()) -> Any:
        """Execute query and return last row id."""
        cur = self.conn.execute(query, params)
        self.conn.commit()
        if self.auto_backup:
            self.createBackup()
        return cur.lastrowid

    def executeManyQueries(self, query: str, params_list: List[tuple]):
        """Execute multiple queries with parameters."""
        self.conn.executemany(query, params_list)
        self.conn.commit()
        if self.auto_backup:
            self.createBackup()

    def fetchOne(self, query: str, params: tuple = ()) -> Optional[Dict]:
        """Execute query and return first result."""
        cur = self.conn.execute(query, params)
        row = cur.fetchone()
        return dict(row) if row else None

    def fetchAll(self, query: str, params: tuple = ()) -> List[Dict]:
        """Execute query and return all results."""
        cur = self.conn.execute(query, params)
        return [dict(row) for row in cur.fetchall()]

    def _buildWhereClause(self, conditions: Dict) -> Tuple[str, List]:
        """Build WHERE clause from conditions."""
        if not conditions:
            return "", []
        where_clause = " AND ".join(f"{k} = ?" for k in conditions.keys())
        return f"WHERE {where_clause}", list(conditions.values())

    def createIndex(self, table_name: str, column_name: str, unique: bool = False):
        """Create index on table column."""
        index_name = f"idx_{table_name}_{column_name}"
        unique_str = "UNIQUE" if unique else ""
        self.executeQuery(
            f"CREATE {unique_str} INDEX IF NOT EXISTS {index_name} ON {table_name}({column_name})"
        )

    def vacuum(self):
        """Optimize database and reclaim unused space."""
        self.executeQuery("VACUUM")

    def close(self):
        """Close database connection."""
        if hasattr(self, "conn") and self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
