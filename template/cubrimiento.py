import json
from pathlib import Path
from typing import Any, TextIO

if __name__ == "__main__":
    ruta = Path("coverage.json")
    if not ruta.exists():
        print(
            "!!! No se encontró coverage.json. Generalo con `coverage json` o `python -m coverage json`."
        )
        exit()

    print("\n=== Análisis de Coverage ===\n")

    coverage: TextIO = open("coverage.json", "r", encoding="utf-8")
    data: dict[str, Any] = json.load(coverage)
    coverage.close()

    totals: dict[str, str | int] = data["totals"]
    total_lines_covered = totals["covered_lines"]
    total_lines = totals["num_statements"]
    total_branch_covered = totals["covered_branches"]
    total_branches = totals["num_branches"]

    if total_lines:
        print(
            f"➡️  Porcentaje global de líneas cubiertas ({total_lines_covered}/{total_lines}): {total_lines_covered / total_lines * 100:.2f}%"
        )
    if total_branch_covered:
        print(
            f"➡️  Porcentaje global de ramas cubiertas ({total_branch_covered}/{total_branches}): {total_branch_covered / total_branches * 100:.2f}%"
        )
