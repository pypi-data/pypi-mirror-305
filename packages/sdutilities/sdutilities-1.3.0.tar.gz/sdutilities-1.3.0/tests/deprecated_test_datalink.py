import pytest
from sdutilities import DataLink  # Replace 'your_module' with the actual module name
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

# def test_logger_output():
#     # Patch the logger method you expect to be called
#     with patch('Datalink.SDLogger.info') as mock_info:
#         datalink = DataLink(cfg_name="test_cfg", db_file="non_existent_file.json")

#         # Check that the logger's info method was called with the expected message
#         mock_info.assert_called_with('DB Configuration file not found')
#         # Add more assertions here if needed for other log messages
    
# # Sample test for the _set_cxn_info method
# def test_set_cxn_info():
#     datalink = DataLink(cfg_name="test_cfg", db_file="test_db.json")
#     assert datalink._db_cfg is not None
#     assert datalink._db_cfg['uname'] == "cdalal"  # Replace with expected username

# # Sample test for the sql_to_df method
# @patch('datalink.create_engine')
# def test_sql_to_df(mock_create_engine):
#     mock_engine = MagicMock()
#     mock_create_engine.return_value = mock_engine
#     mock_engine.execute.return_value = None  # Simulate execute behavior

#     datalink = DataLink(cfg_name="test_cfg", db_file="test_db.json")

#     sql = "SELECT * FROM test_table"
#     df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
#     mock_engine.execute.return_value = df

#     result = datalink.sql_to_df(sql)
#     assert not result.empty
#     assert list(result.columns) == ['col1', 'col2']
#     assert result.iloc[0]['col1'] == 1

# # Sample test for the get_connection_info method
# def test_get_connection_info():
#     datalink = DataLink(cfg_name="test_cfg", db_file="test_db.json")
#     conn_info = datalink.get_connection_info()
#     assert isinstance(conn_info, dict)
#     assert 'uname' in conn_info
#     assert 'pw' in conn_info



