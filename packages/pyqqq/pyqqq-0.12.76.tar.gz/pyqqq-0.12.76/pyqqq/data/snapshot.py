from typing import Optional
from pyqqq.utils.api_client import raise_for_status, send_request
from pyqqq.utils.logger import get_logger
import datetime as dtm
import pandas as pd
import numpy as np
import pyqqq.config as c


logger = get_logger(__name__)


def get_all_snapshot_for_date(date: dtm.date) -> pd.DataFrame:
    """ """

    url = f"{c.PYQQQ_API_URL}/snapshot/daily/all/{date}"
    r = send_request("GET", url)
    raise_for_status(r)

    rows = r.json()
    for data in rows:
        for iso_date in ["date", "listing_date"]:
            value = data[iso_date]
            data[iso_date] = dtm.date.fromisoformat(value)

    df = pd.DataFrame(rows)

    return _to_snapshot(df)


def get_snapshot_by_code_for_period(
    code: str,
    start_date: dtm.date,
    end_date: Optional[dtm.date] = None,
) -> pd.DataFrame:
    """ """

    url = f"{c.PYQQQ_API_URL}/snapshot/daily/series"
    params = {
        "code": code,
        "start_date": start_date,
    }
    if end_date is not None:
        params["end_date"] = end_date

    r = send_request("GET", url, params=params)
    raise_for_status(r)

    rows = r.json()
    for data in rows:
        for iso_date in ["date", "listing_date"]:
            value = data[iso_date]
            data[iso_date] = dtm.date.fromisoformat(value)

    df = pd.DataFrame(rows)

    return _to_snapshot(df)


def _to_snapshot(df: pd.DataFrame) -> pd.DataFrame:
    alert = {0: None, 1: "caution", 2: "alert", 3: "risk"}

    if df.empty:
        return df

    dtypes = df.dtypes

    for k in [
        "change",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "value",
        "days_since_listing",
        "sales_account",
        "cumulative_sales_account",
        "operating_profit",
        "cumulative_operating_profit",
        "net_income",
        "cumulative_net_income",
        "current_assets",
        "fixed_assets",
        "total_assets",
        "flow_liabilities",
        "fixed_liabilities",
        "total_liabilities",
        "capital_stock",
        "shareholders_equity",
    ]:
        if k in dtypes:
            dtypes[k] = np.dtype("int64")

    for k in ["change_percent", "retention_ratio", "debt_ratio", "roa", "roe", "per", "pbr"]:
        if k in dtypes:
            dtypes[k] = np.dtype("float64")

    df["alert_issue"] = df["alert_issue"].apply(lambda level: alert[level])

    df = df[
        [
            "date",
            "market",
            "code",
            "name",
            "type",
            "change",
            "change_percent",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "value",
            "listing_date",
            "days_since_listing",
            "administrative_issue",
            "alert_issue",
            "fiscal_quarter_end",
            "sales_account",
            "cumulative_sales_account",
            "operating_profit",
            "cumulative_operating_profit",
            "net_income",
            "cumulative_net_income",
            "current_assets",
            "fixed_assets",
            "total_assets",
            "flow_liabilities",
            "fixed_liabilities",
            "total_liabilities",
            "capital_stock",
            "shareholders_equity",
            "retention_ratio",
            "debt_ratio",
            "roa",
            "roe",
            "eps",
            "sps",
            "per",
            "pbr",
        ]
    ]
    df.set_index("code", inplace=True)

    return df
