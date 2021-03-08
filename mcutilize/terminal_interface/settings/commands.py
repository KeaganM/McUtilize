def test(x:int,y:int) -> int:
    return x + y

def test2(x:int,y:int) -> int:
    return x - y

COMMANDS = {
    'test':test,
    'test2':test2
}