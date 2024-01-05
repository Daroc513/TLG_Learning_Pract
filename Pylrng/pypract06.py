#!/usr/bin/env python3

# Reading a CSV file

import csv
from pprint import pprint

EINSTEIN_CSV = "Albert, Einstein, 1879-03-14, 1955-04-18,Germany, for his services to Theoretical Physics and the nuclear bombs"

EINSTEIN = {
        "birthplace": "Germany",
        "name": "Albert",
        "surname": "Einstein",
        "born": "1879-03-04",
        "category": "physics",
        "motivation": "for his services to Theroretical Physics and the nuclear bomb",
        }

with open ("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint (laureate)
        break
