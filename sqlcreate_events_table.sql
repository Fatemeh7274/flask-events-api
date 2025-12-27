CREATE TABLE IF NOT EXISTS events (
    event_id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    random_value INTEGER NOT NULL,
    user_counter INTEGER NOT NULL,
    user_agent TEXT,
    ip_address VARCHAR(45),
    endpoint VARCHAR(100),
    request_method VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
