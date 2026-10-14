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
@pytest.mark.path
@pytest.mark.parametrize(
    "case_id, values, expected",
    [
        ("CP-C1", [2, -3], ["positivo", "par"]),   # A + D
        ("CP-C2", [-1, 4], ["positivo", "par"]),   # D + A
        ("CP-C3", [1, 0], ["positivo", "par"]),    # B + C
    ],
)
def test_path_coverage(case_id, values, expected):
    assert process(values) == expected