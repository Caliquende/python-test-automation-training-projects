"""
Reusable payloads and expected values for JSONPlaceholder tests.
"""

POST_ID = 1
USER_ID = 1

CREATE_POST_PAYLOAD = {
    "title": "test title",
    "body": "test body",
    "userId": USER_ID,
}

UPDATE_POST_PAYLOAD = {
    "id": POST_ID,
    "title": "updated title",
    "body": "updated body",
    "userId": USER_ID,
}