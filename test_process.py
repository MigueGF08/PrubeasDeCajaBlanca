import pytest
from process import process


# 1. Cobertura de sentencias (Statement Coverage)
@pytest.mark.statement
@pytest.mark.parametrize(
    "case_id, values, expected",
    [
        ("CP-S1", [2], ["positivo", "par"]),
        ("CP-S2", [3], ["positivo"]),
        ("CP-S3", [-2], ["par"]),
    ],
)
def test_statement_coverage(case_id, values, expected):
    assert process(values) == expected


# 2. Cobertura de decisiones / ramas (Branch Coverage)
@pytest.mark.branch
@pytest.mark.parametrize(
    "case_id, values, expected",
    [
        ("CP-D1", [2], ["positivo", "par"]),
        ("CP-D2", [-1], []),
        ("CP-D3", [], []),
    ],
)
def test_branch_coverage(case_id, values, expected):
    assert process(values) == expected


# 3. Cobertura de caminos (Path Coverage) con 2 valores de entrada
@pytest.mark.parametrize(
    "case_id, camino, values, expected",
    [
        ("CP-C1",  "A+D", [2, -3],  ["positivo", "par"]),
        ("CP-C2",  "D+A", [-1, 4],  ["positivo", "par"]),
        ("CP-C3",  "B+C", [1, 0],   ["positivo", "par"]),
        ("CP-C4",  "A+A", [2, 4],   ["positivo", "par", "positivo", "par"]),
        ("CP-C5",  "A+B", [2, 3],   ["positivo", "par", "positivo"]),
        ("CP-C6",  "A+C", [2, -2],  ["positivo", "par", "par"]),
        ("CP-C7",  "B+A", [3, 4],   ["positivo", "positivo", "par"]),
        ("CP-C8",  "B+B", [1, 3],   ["positivo", "positivo"]),
        ("CP-C9",  "B+D", [3, -1],  ["positivo"]),
        ("CP-C10", "C+A", [0, 2],   ["par", "positivo", "par"]),
        ("CP-C11", "C+B", [-2, 1],  ["par", "positivo"]),
        ("CP-C12", "C+C", [0, -2],  ["par", "par"]),
        ("CP-C13", "C+D", [-4, -1], ["par"]),
        ("CP-C14", "D+B", [-3, 5],  ["positivo"]),
        ("CP-C15", "D+C", [-1, 0],  ["par"]),
        ("CP-C16", "D+D", [-1, -3], []),
    ],
    ids=lambda p: p if isinstance(p, str) else None,
)
def test_path_coverage(case_id, camino, values, expected):
    assert process(values) == expected