from src.calculator import add,sub

def test_add():
    assert add(1,3)==4
    assert add(3,4)==7
    assert add(-1,-1)==-2
    assert add(0,-3)==-3
    assert add(0,0)==0
    
    
def test_sub():
    assert sub(0,1)==-1
    assert sub(6,3)==3
    assert sub(4,5)==-1
    assert sub(0,0)==0