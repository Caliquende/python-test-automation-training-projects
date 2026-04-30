"""
TR: JSONPlaceholder testleri için yeniden kullanılabilir veri paketleri (payloads) ve beklenen değerler.
EN: Reusable payloads and expected values for JSONPlaceholder tests.
"""

# Testlerde kullanılacak sabit ID değerleri.
# Constant ID values to be used in tests.
POST_ID = 1
USER_ID = 1

# Yeni bir gönderi oluştururken API'ye gönderilecek veri yapısı.
# The data structure to be sent to the API when creating a new post.
CREATE_POST_PAYLOAD = {
    "title": "test title",
    "body": "test body",
    "userId": USER_ID,
}

# Bir gönderiyi güncellerken API'ye gönderilecek veri yapısı.
# The data structure to be sent to the API when updating a post.
UPDATE_POST_PAYLOAD = {
    "id": POST_ID,
    "title": "updated title",
    "body": "updated body",
    "userId": USER_ID,
}

# Var olmayan bir gönderi için ID.
# ID for a non-existent post.
NON_EXISTENT_POST_ID = 999