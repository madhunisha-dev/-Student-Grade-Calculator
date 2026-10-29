from app import calculate_metrics

def test_calculate_metrics_valid():
    total, average = calculate_metrics([85, 90, 80])
    assert total == 255
    assert average == 85.0

def test_calculate_metrics_empty():
    total, average = calculate_metrics([])
    assert total == 0
    assert average == 0
