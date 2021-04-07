from main import main

# Test Case 1:
# Input: 93
# Output: “Change: 50 20 20 2 1”
def test_main_1(capfd):
    main(93)
    out, err = capfd.readouterr()
    assert out == "Change: 50 20 20 2 1\n"

# Test Case 2:
# Input: 113
# Output: “Change: 100 10 2 2”
def test_leap_year_false(capfd):
    main(11)
    out, err = capfd.readouterr()
    assert out == "Change: 100 10 2 2\n"
