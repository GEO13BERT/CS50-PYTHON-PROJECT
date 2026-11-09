from project import valid_sku, check_stock, get_stock


def test_valid_sku():
    assert valid_sku("CWDE-288","Nike")==True
    assert valid_sku("CWDE-123288","Nike")==False
    assert valid_sku("IF6490","Adidas")==True
    assert valid_sku("JR23466","Adidas")==False

def test_check_stock():
    inventory=[{'id': '111', 'size': 42.0 ,'stock': 2.0}, {'id': '222','size':43.0 ,'stock': 10.0}]
    assert check_stock(inventory, 42.0,'111')==2.0
    assert check_stock(inventory, 6.0,'876')==-1

def test_get_stock():
    inventory=[{'id': '111', 'stock': 2.0}, {'id': '222', 'stock': 10.0}]
    assert get_stock(inventory, 6.0) == [2.0]