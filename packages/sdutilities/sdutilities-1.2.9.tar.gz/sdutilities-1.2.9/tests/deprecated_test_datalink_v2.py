
# Paste your test function here
import pytest
from sdutilities.datalink import DataLink  # Replace 'your_module' with the actual module name
from unittest.mock import MagicMock, patch
import pandas as pd
from faker import Faker

# Create a sample DataFrame for testing
fake = Faker()
@pytest.fixture
def sample_df():
    """Creates a sample DataFrame with fake data for testing."""
    fake_data = {'col1': [fake.random_number(digits=3) for _ in range(10)],
                 'col2': [fake.name() for _ in range(10)],
                 'col3': [fake.date() for _ in range(10)]}
    return pd.DataFrame(fake_data)

def test_upsert(mock_datalink, sample_df):
    """Tests the upsert functionality with a sample DataFrame."""
    # Setup - create a table in the in-memory SQLite database
    sample_df.to_sql('test_table', con=mock_datalink._engine, index=False, if_exists='replace')

    # Test the upsert method
    mock_datalink.upsert(sample_df, 'test_table', 'public')  # 'public' schema is a dummy value for SQLite

    # Verify that the data is upserted correctly
    result_df = pd.read_sql_table('test_table', con=mock_datalink._engine)
    assert result_df.equals(sample_df)
