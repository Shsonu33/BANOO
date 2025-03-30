name: Run Python Script

on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 * * * *'

jobs:
  run-python:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Set Environment Variables
        run: |
          echo "INSTAGRAM_USERNAME=${{ secrets.INSTAGRAM_USERNAME }}" >> $GITHUB_ENV
          echo "INSTAGRAM_PASSWORD=${{ secrets.INSTAGRAM_PASSWORD }}" >> $GITHUB_ENV
          echo "OPENAI_API_KEY=${{ secrets.OPENAI_API_KEY }}" >> $GITHUB_ENV

      - name: Run Python Script
        run: python bot.py
