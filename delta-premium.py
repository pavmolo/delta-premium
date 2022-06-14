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
#credentials = service_account.Credentials.from_service_account_file(
#        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1etUSlGdjQruAn5AjPCat2R-k9LhXnapnXm4szTZJ3Pg'
SAMPLE_RANGE_NAME = 'sector_margin'

service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()

resp = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
df = pd.DataFrame.from_dict(resp['values'])
st.write(df)
