"""Testes estáticos do arquivo Apache para o redirecionamento Mappy."""
from pathlib import Path
import re
import unittest

RULES = (Path(__file__).resolve().parents[1] / "go" / ".htaccess").read_text(encoding="utf-8")

class RedirectTests(unittest.TestCase):
    def test_mappy_rule(self):
        self.assertRegex(RULES, r"(?m)^RewriteRule \^mappy/\?\$ https://happytech\.com\.br/apps/happyhouse/external/products/mappy/ \[R=302,L,NE,NC\]$")

    def test_rewrite_engine_enabled(self):
        self.assertRegex(RULES, r"(?m)^RewriteEngine On$")

    def test_author_present(self):
        self.assertIn("Fabio Castilhos <fabcastilhos@gmail.com>", RULES)

if __name__ == "__main__":
    unittest.main()
