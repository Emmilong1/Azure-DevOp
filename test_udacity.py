from click.testing import CliRunner     #allows me to invoke the tool to run its required function
from udacity import udacity                 #import the command line tool

def test_hello():                       #make test case
    runner = CliRunner()                                                
    result = runner.invoke(hello, ["--name", "Samuel", "--color", "blue"]) #invoke and allow it takes the names stored in strings
    assert "Samuel" in result.output          #you can test the basic contract of the code and assert specifies the output - it makes sure after invocation, it'll come back and still say Samuel in the output
