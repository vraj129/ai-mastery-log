from hypothesis import given, strategies as st
import pytest
import day4


@pytest.fixture
def data_set():
    return day4.Dataset(
        ["image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8", "image9", "image10"],
        ["cat", "cat", "cat", "cat", "cat", "dogs", "dogs", "dogs", "dogs", "dogs"])


def test_dataset(data_set):
    data = data_set
    train, test = data.split(0.8, seed=3)
    assert "cat" in test.labels
    assert "dogs" in test.labels


@given(st.lists(st.integers()))
def test_split_conserves(samples):
    labels = list(range(len(samples)))
    data = day4.Dataset(samples, labels)
    train, test = data.split()
    assert sorted(train.samples + test.samples) == sorted(samples)
