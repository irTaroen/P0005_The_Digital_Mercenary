import json
import os
from datetime import datetime, timezone

_DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "clients.json"))


def _read() -> list[dict]:
    if not os.path.exists(_DB_PATH):
        return []
    with open(_DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _write(data: list[dict]) -> None:
    with open(_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def list_clients() -> list[dict]:
    return [{"name": c["name"], "omgeving": c["omgeving"]} for c in sorted(_read(), key=lambda c: c["name"])]


def get_client(name: str) -> dict | None:
    row = next((c for c in _read() if c["name"] == name), None)
    if not row:
        return None
    return {
        "name": row["name"],
        "omgeving": row["omgeving"],
        "token_live": row["token_live"],
        "token_test": row["token_test"],
    }


def upsert_client(name: str, omgeving: int, token_live: str, token_test: str) -> None:
    data = _read()
    entry = {
        "name": name,
        "omgeving": omgeving,
        "token_live": token_live,
        "token_test": token_test,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    idx = next((i for i, c in enumerate(data) if c["name"] == name), None)
    if idx is not None:
        entry["created_at"] = data[idx].get("created_at", entry["created_at"])
        data[idx] = entry
    else:
        data.append(entry)
    _write(data)


def delete_client(name: str) -> bool:
    data = _read()
    new_data = [c for c in data if c["name"] != name]
    if len(new_data) == len(data):
        return False
    _write(new_data)
    return True
