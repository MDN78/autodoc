import pytest
from dotenv import load_dotenv

@pytest.fixture
def load_dotenv():
    load_dotenv()