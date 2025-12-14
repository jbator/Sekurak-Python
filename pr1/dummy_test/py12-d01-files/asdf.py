# Plik-tablica do tłumaczenia rzeczy ;)

print(
  "ala ma kota"
)


# JSON
[
  { "date": "2025-11-26", "loc": 1234 },
  { "date": "2025-11-27", "loc": 1235, "asdf": "alamakota" }
]

# JSON-Schema

# Protobuf
Message entry {
  option string date = 1;
  option int loc = 2;
}

repeated entry entries = 1;


# CSV
date,loc
2025-11-26,1234
2025-11-27,1235




