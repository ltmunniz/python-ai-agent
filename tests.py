#from functions.get_file_content import get_file_content
#from ai_agent.functions.write_file_content import write_file
from functions.run_python_file import run_python_file

def test():
    
    # result = get_file_content("calculator", "lorem.txt")
    # print("Result for current file:")
    # print(result)
    # print("")

    
    # result = get_file_content("calculator", "main.py")
    # print(result)
    # print("")
    
    # result=get_file_content("calculator", "pkg/calculator.py")
    # print(result)
    # print("")
    
    # result=get_file_content("calculator", "/bin/cat") 
    # print(result)
    # print("")
    
    # result=get_file_content("calculator", "pkg/does_not_exist.py")
    # print(result)
    # print("")
    
    # write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    
    # run_python_file("calculator", "main.py")
    # run_python_file("calculator", "main.py", ["3 + 5"])
    # run_python_file("calculator", "tests.py")
    # run_python_file("calculator", "../main.py")
    # run_python_file("calculator", "nonexistent.py")
    # run_python_file("calculator", "lorem.txt")
    
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)

    result = run_python_file("calculator", "lorem.txt")
    print(result)
    
if __name__ == "__main__":
    test()