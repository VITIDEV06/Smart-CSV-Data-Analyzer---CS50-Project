import pytest
from project import load_data, clean_data, analyze_data, generate_charts, generate_report
import pandas as pd
import sys


def test_load_data():
    df = load_data("popular_people.csv")

    assert df is not None


def test_clean_data():

    df = pd.DataFrame({
        "age": [20, None, 20],
        "salary": [1000, 1000, 1000]
    })

    cleaned = clean_data(df)

    assert cleaned.shape[0] == 1


def test_analyze_data():

    df = pd.DataFrame({
        "age": [20, 30]
    })

    result = analyze_data(df)

    assert result["age"]["mean"] == 25
    assert result["age"]["max"] == 30
    assert result["age"]["min"] == 20
    assert result["age"]["median"] == 25


def test_analyze_data_returns_dictionary():

    df = pd.DataFrame({
        "numbers": [1, 2, 3]
    })

    result = analyze_data(df)

    assert isinstance(result, dict)
    
