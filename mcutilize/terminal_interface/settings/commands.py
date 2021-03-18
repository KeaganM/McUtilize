def test(x:int,y:int) -> int:
    return x + y

def test2(x:int,y:int) -> int:
    return x - y

def test3(items:list) -> str:
    return ','.join(items)

def test4(items:tuple) -> None:
    print(items)

COMMANDS = {
    'test':test,
    'test2':test2,
    'test3':test3,
    'test4':test4
}