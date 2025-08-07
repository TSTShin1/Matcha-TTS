"""Tập ký tự tiếng Việt cho mô hình Matcha-TTS hoặc Tacotron."""

# Ký hiệu đặc biệt
_pad = "_"
_punctuation = ';:,.!?¡¿—…"«»“”() '

# Các chữ cái tiếng Việt có dấu
_letters_vietnamese = (
    "AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXY"
    "aăâbcdđeêghiklmnoôơpqrstuưvxy"
)

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters_vietnamese)

# Special symbol ids
SPACE_ID = symbols.index(" ")
