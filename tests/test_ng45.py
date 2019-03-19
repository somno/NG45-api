from ng45.api import ng45

def test_kidney_risk():
    assert ng45.kidney_risk(41, False, False, False, False, False) == False
    assert ng45.kidney_risk(67, False, False, False, False, False) == True
    assert ng45.kidney_risk(41, True, False, False, False, False) == True
    assert ng45.kidney_risk(41, False, True, False, False, False) == True
    assert ng45.kidney_risk(41, False, False, True, False, False) == True
    assert ng45.kidney_risk(41, False, False, False, True, False) == True
    assert ng45.kidney_risk(41, False, False, False, False, True) == True

def test_fbc():

    assert ng45.full_blood_count(2, "minor", False, False) == "Not Routinely"
    assert ng45.full_blood_count(2, "major", False, False) == "Yes"

    assert ng45.full_blood_count(3, "minor", False, False) == "Not Routinely"
    assert ng45.full_blood_count(3, "intermediate", False, False) == "Not Routinely"
    assert ng45.full_blood_count(3, "intermediate", True, False) == "Consider"
    assert ng45.full_blood_count(3, "major", True, False) == "Yes"


def test_ue():

    assert ng45.kidney_function(1, "minor", False, ) == "Not Routinely"
    assert ng45.kidney_function(1, "major", False, ) == "Not Routinely"
    assert ng45.kidney_function(1, "major", True, ) == "Consider"

    assert ng45.kidney_function(2, "minor", False, ) == "Not Routinely"
    assert ng45.kidney_function(2, "intermediate", False, ) == "Not Routinely"
    assert ng45.kidney_function(2, "intermediate", True, ) == "Not Routinely"
    assert ng45.kidney_function(2, "major", False, ) == "Yes"

    assert ng45.kidney_function(4, "minor", False, ) == "Not Routinely"
    assert ng45.kidney_function(4, "minor", True, ) == "Consider"
    assert ng45.kidney_function(4, "intermediate", True, ) == "Yes"
    assert ng45.kidney_function(4, "major", False, ) == "Yes"
