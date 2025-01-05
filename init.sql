-- Table for products
CREATE TABLE IF NOT EXISTS products (
  product_id VARCHAR (50) UNIQUE NOT NULL PRIMARY KEY, 
  product_name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL
);

-- Table for transactions
CREATE TABLE IF NOT EXISTS transactions (
  transaction_id VARCHAR (50) UNIQUE NOT NULL PRIMARY KEY,      
  "timestamp" TIMESTAMP,
  total_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(100),                      
  store_name VARCHAR(100)
);

-- Table for ordered_products
CREATE TABLE IF NOT EXISTS ordered_products (
  transaction_id VARCHAR (50) NOT NULL,
  product_id VARCHAR (50) NOT NULL,
  product_quantity INT NOT NULL,
  PRIMARY KEY (transaction_id, product_id),
  FOREIGN KEY (transaction_id)
  REFERENCES transactions (transaction_id),
  FOREIGN KEY (product_id)
  REFERENCES products (product_id)
)
