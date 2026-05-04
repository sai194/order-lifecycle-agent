CREATE TABLE orders (
  order_id TEXT PRIMARY KEY,
  order_status TEXT,
  order_date DATE,
  delivery_date DATE
);

CREATE TABLE returns (
  order_id TEXT PRIMARY KEY,
  return_status TEXT,
  refund_status TEXT,
  return_date DATE
);

INSERT INTO orders VALUES
('1001', 'DELIVERED', '2026-04-20', '2026-04-25'),
('1002', 'DELIVERED', '2026-04-10', '2026-04-12'),
('1003', 'DELIVERED', '2026-04-01', '2026-04-03');

INSERT INTO returns VALUES
('1001', 'COMPLETED', 'INITIATED', '2026-04-27'),
('1002', 'COMPLETED', 'COMPLETED', '2026-04-13'),
('1003', 'COMPLETED', 'FAILED', '2026-04-04');