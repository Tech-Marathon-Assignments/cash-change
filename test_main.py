from main import main

# Test Case 1:
# Input: year = 2000
# Output: "2000 is a lap year"
def test_main_1(capfd):
    main(93)
    out, err = capfd.readouterr()
    assert out == "Change: 50 20 20 2 1\n"

# Test Case 2:
# Input: year = 2001
# Output: "2001 is a lap year"
def test_leap_year_false(capfd):
    main(113)
    out, err = capfd.readouterr()
    assert out == "Change: 100 10 2 2\n"
