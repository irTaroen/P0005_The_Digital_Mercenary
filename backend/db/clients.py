import os
from cryptography.fernet import Fernet
from db.supabase_client import get_supabase


def _fernet() -> Fernet:
    key = os.getenv("SECRET_KEY")
    if not key:
        raise RuntimeError("SECRET_KEY must be set")
    return Fernet(key.encode())


def list_clients() -> list[dict]:
    supabase = get_supabase()
    rows = supabase.table("clients").select("name, omgeving").order("name").execute()
    return rows.data


def get_client(name: str) -> dict:
    f = _fernet()
    supabase = get_supabase()
    result = supabase.table("clients").select("*").eq("name", name).maybe_single().execute()
    if not result.data:
        return None
    row = result.data
    return {
        "name": row["name"],
        "omgeving": row["omgeving"],
        "token_live": f.decrypt(row["token_live_enc"].encode()).decode(),
        "token_test": f.decrypt(row["token_test_enc"].encode()).decode(),
    }


def upsert_client(name: str, omgeving: int, token_live: str, token_test: str) -> None:
    f = _fernet()
    supabase = get_supabase()
    supabase.table("clients").upsert({
        "name": name,
        "omgeving": omgeving,
        "token_live_enc": f.encrypt(token_live.encode()).decode(),
        "token_test_enc": f.encrypt(token_test.encode()).decode(),
    }, on_conflict="name").execute()


def delete_client(name: str) -> bool:
    supabase = get_supabase()
    result = supabase.table("clients").delete().eq("name", name).execute()
    return len(result.data) > 0
