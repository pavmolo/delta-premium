import streamlit as st
import os.path
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')
#credentials = service_account.Credentials.from_service_account_file(
#        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1qZS-Y7NxD15B3rPTGpYIsZfF67ySaBjAEsUEsDIwTdo'
SAMPLE_RANGE_NAME = 'base'

service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()

resp = service.append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, valueInputOption='USER_ENTERED', body={'values': 1}).execute()
