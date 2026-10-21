CREATE EXTENSION IF NOT EXISTS vector;


CREATE TABLE IF NOT EXISTS resumes (
 id SERIAL PRIMARY KEY,
 filename TEXT NOT NULL,
 s3_key TEXT,
 full_text TEXT NOT NULL,
 uploaded_at TIMESTAMP DEFAULT now()
);


CREATE TABLE IF NOT EXISTS chunks (
 id SERIAL PRIMARY KEY,
 resume_id INT REFERENCES resumes(id) ON DELETE CASCADE,
 chunk_index INT NOT NULL,
 content TEXT NOT NULL,
 embedding VECTOR(1024) -- Titan V2 default dimension
)
