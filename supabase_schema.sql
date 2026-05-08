-- Run this once in the Supabase SQL editor
-- Project: The Digital Mercenary

CREATE TABLE clients (
  id          SERIAL PRIMARY KEY,
  name        TEXT UNIQUE NOT NULL,
  omgeving    INTEGER NOT NULL,
  token_live_enc TEXT NOT NULL,
  token_test_enc TEXT NOT NULL,
  created_at  TIMESTAMPTZ DEFAULT now()
);

-- Disable public access — only the service_role key (backend) can read/write
ALTER TABLE clients ENABLE ROW LEVEL SECURITY;
-- No RLS policies added, so no anon/authenticated access is possible
