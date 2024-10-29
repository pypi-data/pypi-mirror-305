import pytest
from calculator_bundle import calculate

def test_calculate():
    # Test addition and multiplication with sample values
    a, b = 3, 5
    result = calculate(a, b)
    
    assert result["addition"] == 8, f"Expected 8, got {result['addition']}"
    assert result["multiplication"] == 15, f"Expected 15, got {result['multiplication']}"

def test_calculate_with_zero():
    # Test with zero
    a, b = 0, 5
    result = calculate(a, b)
    
    assert result["addition"] == 5, f"Expected 5, got {result['addition']}"
    assert result["multiplication"] == 0, f"Expected 0, got {result['multiplication']}"

def test_calculate_with_negative_numbers():
    # Test with negative numbers
    a, b = -3, 5
    result = calculate(a, b)
    
    assert result["addition"] == 2, f"Expected 2, got {result['addition']}"
    assert result["multiplication"] == -15, f"Expected -15, got {result['multiplication']}"
