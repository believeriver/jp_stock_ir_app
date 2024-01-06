import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
from app.views.streamlit import start_streamlit_db


if __name__ == '__main__':
    start_streamlit_db()
