# Plant Scientific Name Checker

This Python tool checks plant scientific names using the [Plants of the World Online (POWO)](https://powo.science.kew.org) API and outputs accepted names, authors, and synonyms.

## 🔍 Features

- Input: Excel file with a list of scientific names
- Checks against POWO database
- Returns accepted name, author, and more
- Output saved as Excel for easy use

## 📂 Input Format

| Scientific Name           |
|---------------------------|
| Bulbophyllum superpositum |
| Phalaenopsis amabilis     |
| ...                       |

## ⚙️ Setup

Install required packages:

```bash
pip install pandas requests openpyxl
