import pandas as pd
import requests
import streamlit as st
from apps.config import BASE_URL, ENVIRONMENT


def app():

    st.write(
        """
    ## *Buffer Finance*
    # All Option Details
    """
    )

    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    response = requests.get(
        f"{BASE_URL}/options_and_predictions/?environment={environment}")
    data = response.json()
    for _data in data:
        asset = _data.pop('asset')
        _data['asset_name'] = asset.get('name')

    df = pd.DataFrame(data)
    st.table(df)
