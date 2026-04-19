"""Handels Responses and Converts to XML/CSV"""
from dicttoxml import dicttoxml
from fastapi import Response
import csv
import io


def to_xml(data: dict) -> Response:
    """Convert a dict to an XML response."""
    content = dicttoxml(data, custom_root="response", attr_type=False)
    return Response(content=content, media_type="application/xml")


def to_csv(data: list) -> Response:
    """Convert a list of dicts to a CSV"""
    buffer = io.StringIO()
    if not data:
        return Response(content="", media_type="text/csv")

    writer = csv.DictWriter(buffer, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return Response(content=buffer.getvalue(), media_type="text/csv")
