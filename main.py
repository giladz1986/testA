
from logic import logic_print, new_logic_other_print

def test_print(val : str):
    print("Hey " + val)
    
value = "gilad"
test_print(value)

logic_print(value)

new_logic_other_print(value)