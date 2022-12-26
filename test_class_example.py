from tables_class_example import print_tables
def test_output_file():
    obj=print_tables(4)
    obj.print_table()
    import os
    assert os.path.exists("output.txt")
def test_count_lines():
    f2=open("output.txt","r")
    count=0
    for line in f2:
        count+=1
    assert count>=10