import json
from http.client import HTTPResponse

import cbrrr as cbor
import polars as pl


def read_content(content: HTTPResponse):
    try:
        return json.loads(content)
    except (json.JSONDecodeError, UnicodeDecodeError):
        pass

    try:
        return cbor.decode_dag_cbor(content)
    except cbor.CbrrrDecodeError:
        pass

    try:
        return pl.read_parquet(content)
    except pl.exceptions.ComputeError:
        pass

    try:
        return pl.read_csv(content)
    except pl.exceptions.ComputeError:
        pass

    raise ValueError("Unknown data format or unsupported content type")
