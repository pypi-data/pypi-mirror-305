from datetime import date
import json
from typing import List, Tuple
import unittest
import uuid

from pynpdc.models import (
    AccessLevel,
    AccountWithToken,
    AttachmentQuery,
    AttachmentQuerySerializer,
    DatasetQuery,
    DatasetQuerySerializer,
    RecordCreateDTO,
    RecordCreateDTOEncoder,
)

# ------------------------------------------------------------------------------
# Account and auth models
# ------------------------------------------------------------------------------


class TestAccountWithToken(unittest.TestCase):
    def test_update_token(self) -> None:
        account = AccountWithToken(
            {
                "id": str(uuid.uuid4()),
                "email": "test@example.org",
                "accessLevel": AccessLevel.EXTERNAL,
                "token": "token-123",
                "directoryUser": False,
            }
        )

        self.assertEqual(account.token, "token-123")
        self.assertDictEqual(account.headers, {"Authorization": "Bearer token-123"})

        account.token = "token-124"
        self.assertEqual(account.token, "token-124")


# ------------------------------------------------------------------------------
# Queries
# ------------------------------------------------------------------------------


class TestAttachmentQuerySerializer(unittest.TestCase):
    def test(self) -> None:
        tests: List[Tuple[AttachmentQuery, str]] = [
            ({}, ""),
            ({"skip": 25}, "?skip=25"),
            ({"take": 50}, "?take=50"),
            ({"count": True}, "?count=true"),
            ({"recursive": True}, "?recursive=true"),
            ({"from": date(2024, 10, 2)}, "?from=2024-10-02"),
            ({"until": date(2024, 10, 3)}, "?until=2024-10-03"),
        ]

        ser = AttachmentQuerySerializer()

        for query, result in tests:
            self.assertEqual(ser(query), result)


class TestDatasetQuerySerializer(unittest.TestCase):
    def test(self) -> None:
        tests: List[Tuple[DatasetQuery, str]] = [
            ({}, ""),
            ({"skip": 25}, "?skip=25"),
            ({"take": 50}, "?take=50"),
            ({"count": True}, "?count=true"),
            ({"from": date(2024, 10, 2)}, "?from=2024-10-02"),
            ({"until": date(2024, 10, 3)}, "?until=2024-10-03"),
        ]

        ser = DatasetQuerySerializer()

        for query, result in tests:
            self.assertEqual(ser(query), result)


# ------------------------------------------------------------------------------
# Record DTOs
# ------------------------------------------------------------------------------


class TestRecordCreateDTOEncoder(unittest.TestCase):
    def test(self) -> None:
        ru = RecordCreateDTO(content={"id": 0}, type="T", id="1", parent_id="2")
        j = json.dumps(ru, cls=RecordCreateDTOEncoder)

        self.assertEqual(
            j,
            json.dumps({"content": {"id": 0}, "type": "T", "id": "1", "parentId": "2"}),
        )
