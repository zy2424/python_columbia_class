import question_one
import question_two
import question_three
import question_four
import question_five
import question_six
import question_seven
import question_eight
import question_nine
import question_ten
import question_11
import question_12
import question_13
import question_14
import question_15
import question_16
import question_17
import question_18
import question_19
import question_20
import question_21
import question_22
import question_23
import question_24
import question_25
import question_26
import question_27
import question_28
import question_29
import question_30

def test_question_one():
    assert question_one.x == (4 + 17)

def test_question_two():
    assert question_two.store == (256 - 170)

def test_question_three():
    assert question_three.result == 1/12

def test_question_four():
    assert question_four.result == (12//3)

def test_question_five():
    assert question_five.name == "my name is" + " bob"

def test_question_six():
    assert question_six.scream == "a" * 1000

def test_question_seven():
    assert question_seven.result == (37 % 15)

def test_question_eight():
    assert question_eight.result == (24 % 2)

def test_question_nine():
    assert question_nine.result == 100

def test_question_ten():
    assert question_ten.result == 5

def test_question_11():
    assert question_11.result == "divisible by 2"

def test_question_12():
    assert question_12.result == "not divisible by 3"

def test_question_13():
    assert question_13.result == (54 * 12)

def test_question_14():
    assert question_14.x == 1.5912397

def test_question_15():
    assert question_15.result == (-12 * 6)

def test_question_16():
    assert question_16.result == "charles"[2]

def test_question_17():
    assert question_17.result == "charles"[-1]

def test_question_18():
    assert question_18.result == "charles"[0]

def test_question_19():
    assert question_19.result == "action jackson"[0]

def test_question_20():
    assert question_20.result == "charles in charge".index(" ")

def test_question_21():
    assert question_21.result == "jam box"

def test_question_22():
    assert question_22.result == (True and False)

def test_question_23():
    assert question_23.result == (True and True)

def test_question_24():
    assert question_24.result == (False and True)

def test_question_25():
    assert question_25.result == (False and False)

def test_question_26():
    assert question_26.result == (True or False)

def test_question_27():
    assert question_27.result == (True or True)

def test_question_28():
    assert question_28.result == (False or True)

def test_question_29():
    assert question_29.result == (False or False)

def test_question_30():
    assert question_30.result == (not False)
