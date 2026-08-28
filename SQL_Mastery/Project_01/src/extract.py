import pandas as pd
from sqlalchemy import text
from database import engine

def load_raw_data():
    """Load all raw data into PostgreSQL"""
    
    # Read CSV files
    customers = pd.read_csv('../data/raw/customers.csv')
    products = pd.read_csv('../data/raw/products.csv')
    orders = pd.read_csv('../data/raw/orders.csv')
    order_items = pd.read_csv('../data/raw/order_items.csv')
    payments = pd.read_csv('../data/raw/payments.csv')
    
    # Load to database
    with engine.connect() as conn:
        # Load raw data
        customers.to_sql('raw_customers', conn, if_exists='replace', index=False)
        products.to_sql('raw_products', conn, if_exists='replace', index=False)
        orders.to_sql('raw_orders', conn, if_exists='replace', index=False)
        order_items.to_sql('raw_order_items', conn, if_exists='replace', index=False)
        payments.to_sql('raw_payments', conn, if_exists='replace', index=False)
        
        print("✅ Raw data loaded successfully")
        
        # Verify counts
        for table in ['raw_customers', 'raw_products', 'raw_orders', 
                     'raw_order_items', 'raw_payments']:
            result = conn.execute(text(f"SELECT COUNT(*) FROM {table}"))
            count = result.fetchone()[0]
            print(f"   {table}: {count} rows")

def execute_sql_file(filepath):
    """Execute SQL file"""
    with open(filepath, 'r') as f:
        sql = f.read()
    
    with engine.connect() as conn:
        # Split and execute each statement
        for statement in sql.split(';'):
            if statement.strip():
                try:
                    conn.execute(text(statement))
                except Exception as e:
                    print(f"⚠️  Error executing: {statement[:50]}...")
                    print(f"   {e}")
        
        print(f"✅ Executed {filepath}")

def run_data_pipeline():
    """Run the complete data pipeline"""
    print("🚀 Starting data pipeline...")
    
    # 1. Load raw data
    print("\n📥 Loading raw data...")
    load_raw_data()
    
    # 2. Run schema
    print("\n📊 Creating schema...")
    execute_sql_file('../sql/01_schema.sql')
    
    # 3. Run quality checks
    print("\n🔍 Running data quality checks...")
    execute_sql_file('../sql/02_data_quality.sql')
    
    # 4. Run cleaning
    print("\n🧹 Cleaning data...")
    execute_sql_file('../sql/03_cleaning.sql')
    
    # 5. Run transformations
    print("\n🔄 Running transformations...")
    execute_sql_file('../sql/04_transformations.sql')
    
    # 6. Run feature engineering
    print("\n⚙️ Engineering features...")
    execute_sql_file('../sql/05_feature_engineering.sql')
    
    print("\n✅ Pipeline complete!")

def load_ml_dataset():
    """Load the ML dataset into Python"""
    query = """
    SELECT * FROM customer_ml_features
    """
    
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    
    # Save to processed directory
    df.to_csv('../data/processed/ml_dataset.csv', index=False)
    print(f"✅ ML dataset saved: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    run_data_pipeline()
    df = load_ml_dataset()
    print(f"\n📊 Dataset sample:\n{df.head()}")