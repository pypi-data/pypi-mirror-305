import time
import uuid
import os
import csv


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        if not os.path.exists(db_name):
            os.makedirs(db_name)

    def _get_table_path(self, table_name):
        return os.path.join(self.db_name, f"{table_name}.csv")

    def create_table(self, table_name, columns):
        table_path = self._get_table_path(table_name)
        if os.path.exists(table_path):
            os.remove(table_path)
        with open(table_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(columns)  # Write column headers

    def insert(self, table_name, data):
        table_path = self._get_table_path(table_name)
        if not os.path.exists(table_path):
            raise Exception(f"Table {table_name} does not exist.")

        with open(table_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def select(self, table_name, conditions=None):
        table_path = self._get_table_path(table_name)
        if not os.path.exists(table_path):
            raise Exception(f"Table {table_name} does not exist.")

        results = []
        with open(table_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if conditions:
                    # Apply conditions if provided (like where clause)
                    if all(row[col] == str(val) for col, val in conditions.items()):
                        results.append(row)
                else:
                    results.append(row)

        return results

    def update(self, table_name, conditions, new_data):
        table_path = self._get_table_path(table_name)
        if not os.path.exists(table_path):
            raise Exception(f"Table {table_name} does not exist.")

        updated = False
        rows = []
        with open(table_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if all(row[col] == str(val) for col, val in conditions.items()):
                    for key, val in new_data.items():
                        row[key] = str(val)
                    updated = True
                rows.append(row)

        # Rewrite the file with updated data
        with open(table_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

        return updated

    def delete(self, table_name, conditions):
        table_path = self._get_table_path(table_name)
        if not os.path.exists(table_path):
            raise Exception(f"Table {table_name} does not exist.")

        deleted = False
        rows = []
        with open(table_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if all(row[col] == str(val) for col, val in conditions.items()):
                    deleted = True  # Skip rows that match the conditions (delete)
                else:
                    rows.append(row)

        # Rewrite the file without the deleted rows
        with open(table_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

        return deleted


class auth:
    def __init__(self):
        self.subscriptions: dict[str, list[callable]] = {}

        self.database = Database("sulfur-db")

        self.database.create_table("users", ["username", "passwordHash"])
        self.database.create_table("tokens", ["username", "token", "expiresAt"])

    def subscribe(self, topic: str, callback: callable):
        self.subscriptions[topic].append(callback)

    def unsubscribe(self, topic: str, callback: callable):
        self.subscriptions[topic].remove(callback)

    def publish(self, topic: str, ctx: any):
        for callback in self.subscriptions[topic]:
            callback(ctx)

    def check_if_user_exists(self, username: str):
        if self.database.select("users", {"username": username}):
            return True
        else:
            return False

    def check_if_authorized(self, token: str):
        self.prune_token(token)

        if self.database.select("tokens", {"token": token}):
            return self.database.select("tokens", {"token": token})[0]["username"]
        else:
            return False

    def gen_auth_token(self, username: str):
        if not self.check_if_user_exists(username):
            return {}

        expires_at = int(time.time()) + (60 * 60 * 12)  # 12 hours

        return {
            "username": username,
            "expiresAt": expires_at,
            "token": str(uuid.uuid4()),
        }

    def prune_token(self, token: str):
        if not self.database.select("tokens", {"token": token}):
            return False

        if (
            int(time.time())
            >= self.database.select("tokens", {"token": token})[0]["expiresAt"]
        ):
            self.database.delete("tokens", {"token": token})
            return True

        return False

    def remove_all_tokens(self, username: str):
        self.database.delete("tokens", {"username": username})

    def verify_password(self, username: str, password_hash: str):
        if not self.check_if_user_exists(username):
            return False

        if (
            self.database.select("users", {"username": username})[0]["passwordHash"]
            == password_hash
        ):
            return True
        else:
            return False

    def register(self, username: str, password_hash: str):
        if self.check_if_user_exists(username):
            self.publish("userRegister", "User already exists")
            return {}

        self.database.insert("users", [username, password_hash])

        self.publish(
            "userRegister", {"username": username, "passwordHash": password_hash}
        )
        return self.gen_auth_token(username)

    def auth(self, username: str, password_hash: str):
        if not self.verify_password(username, password_hash):
            self.publish("userAuth", "Invalid username or password")
            return {}

        token = self.gen_auth_token(username)

        self.database.insert("tokens", [username, token["token"], token["expiresAt"]])

        self.publish(
            "userAuth",
            {
                "username": username,
                "token": token["token"],
                "expiresAt": token["expiresAt"],
            },
        )
        return token
