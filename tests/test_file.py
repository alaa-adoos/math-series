from math_series.series import fibonacci,lucas,sum_series # import functions from series module

#test the result from the funcitons

#test fibonacci function from line 5 to line 19
def test_fibonacci():
    actual=fibonacci(0)
    excepted=0
    assert actual==excepted

def test_fibonacci2():
    actual=fibonacci(1)
    excepted=1
    assert actual==excepted

def test_fibonacci3():
    actual=fibonacci(6)
    excepted=8
    assert actual==excepted

#test lucas function from line 22 to line 35
def test_lucas():
    actual=lucas(0)
    excepted=2
    assert actual==excepted

def test_lucas1():
    actual=lucas(1)
    excepted=1
    assert actual==excepted

def test_lucas2():
    actual=lucas(7)
    excepted=29
    assert actual==excepted

#test sum_series function from line 38 to the end
def test_sum():
    actual=sum_series(6,0,1)
    excepted=8
    assert actual==excepted
def test_sum2():
    actual=sum_series(6,2,1)
    excepted=18
    assert actual==excepted
def test_sum3():
    actual=sum_series(6,3,4)
    excepted=47
    assert actual==excepted    