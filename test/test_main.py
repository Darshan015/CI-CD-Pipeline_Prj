from src.main import add, subtract

def test_main():
    assert add(2,3)==5
    assert add(5,3)==8
    assert subtract(2,3)==-1
    assert subtract(5,3)==2