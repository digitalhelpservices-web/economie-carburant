name: Articles piliers et mise a jour

on:
  schedule:
    # Tous les lundis a 05h00 UTC (07h Paris) : genere/maj les piliers
    - cron: "0 5 * * 1"
  workflow_dispatch: {}

permissions:
  contents: write

jobs:
  piliers:
    runs-on: ubuntu-latest
    steps:
      - name: Recuperer le code
        uses: actions/checkout@v4

      - name: Installer Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Generer / mettre a jour les articles piliers
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: python3 auto-blog/generate_piliers.py

      - name: Publier les changements
        run: |
          git config user.name "Blog Bot"
          git config user.email "bot@economie-carburant.fr"
          git add -A
          if git diff --cached --quiet; then
            echo "Aucun changement."
          else
            git commit -m "Articles piliers / mise a jour du $(date +%Y-%m-%d)"
            git push
          fi
