"""NG45 functionality

A collection of functions that return required tests as per NICE guideline ng45
"""
from flask import request

def full_blood_count(asa: int, surgery: str, kidney: bool, cardiac: bool) -> str:
    """ Returns if FBC should be offered

    Inputs:
        - ASA
        - Surgery grade
            minor, intermediate, major
        - Kidney risk
        - Cardiovascular disease

    Outputs:
        Recommendation using nice wording
        - "Yes"
        - "Not routinely"
        - "Consider"

    Reference:
        recommendation 1.1.10 of full guidance
    """

    if asa < 3:
        if surgery == "major":
            return "Yes"
        else :
            return "Not Routinely"
    else:
        if surgery == "major":
            return "Yes"
        elif surgery == "intermediate":
            if kidney:
                return "Consider"
            elif cardiac:
                return "Consider"
            else:
                return "Not Routinely"
        else:
            return "Not Routinely"

def kidney_risk(age: float, ckd:bool, liver:bool, hf:bool, dm: bool, intra:bool) -> bool:
    """ function that returns if patient at increased risk of kidney injury
    as defined by recommendation 1.1.8 of NICE guideline cg169 for ELECTIVe surgery

    Inputs:
        - Intraperitoneal surgery
        - Chronic Kidney disease
        - Diabetes
        - Heart Failure
        - Age (>65)
        - Liver Disease

    If any of these are true then the function will return true
    """
    at_risk = False

    if age > 65:
        at_risk = True

    if ckd :
        at_risk = True

    if liver :
        at_risk = True

    if hf :
        at_risk = True

    if dm :
        at_risk = True

    if intra :
        at_risk = True

    return at_risk

def kidney_function(asa: int, surgery: str, kidney: bool,) -> str:
    """ Returns if test forUrea and Electrolytes should be offered

    Inputs:
        - ASA
        - Surgery grade
            minor, intermediate, major
        - Kidney risk

    Outputs:
        Recommendation using nice wording
        - "Yes"
        - "Not routinely"
        - "Consider"

    Reference:
        recommendation 1.1.11 of full guidance
    """
    if asa == 1:
        if surgery == "major":
            if kidney:
                return "Consider"
            else:
                return "Not Routinely"
        else:
            return "Not Routinely"

    if asa == 2:
        if surgery == "major":
            return "Yes"
        elif surgery == "intermediate":
            if kidney:
                return "Consider"
            else:
                return "Not Routinely"
        else:
            return "Not Routinely"

    if asa > 2:
        if surgery == "minor":
            if kidney:
                return "Consider"
            else:
                return "Not Routinely"
        else:
            return "Yes"

def ecg(asa: int, surgery: str, age: float) -> str:
    """ Returns if ECG needed pre-op

    Inputs:
        - Age
        - Surgery grade
            minor, intermediate, major
        - ASA

    Outputs:
        Recommendation using nice wording
        - "Yes"
        - "Not routinely"
        - "Consider"

    Reference:
        recommendation 1.1.4 of full guidance
    """

    if asa == 1:
        if surgery == "major":
            if age > 65:
                return "Consider"
            else:
                return "Not Routinely"
        else:
            return "Not Routinely"

    elif asa == 2:
        if surgery == "minor":
            return "Not Routinely"
        elif surgery == "intermediate":
            return "Consider"
        else:
            return "Yes"

    else:
        if surgery == "minor":
            return "Consider"
        else:
            return "Yes"

def put():
    """ handles API request

    INPUT:
        - ASA
        - Age
        - Surgery ["minor", "intermediate", "major"]
        - Intraperitoneal surgery
        - Chronic Kidney disease
        - Diabetes
        - Heart Failure/Cadiac Disease
        - Liver Disease
    """

    asa = request.json['asa']
    age = request.json['age']
    surgery = request.json['surgery']
    diabetes = request.json['diabetes']
    ckd = request.json['ckd']
    cardiac = surgery = request.json['cardiac']
    liver = surgery = request.json['liver']
    intraperitoneal = cardiac = surgery = request.json['intraperitoneal']

    kid_risk = kidney_risk(age, ckd, liver, cardiac, diabetes, intraperitoneal)
    tests = {
        "ecg": ecg(asa, surgery, age),
        "full_blood_count": full_blood_count(asa, surgery, kid_risk, cardiac),
        "kidney_function": kidney_function(asa, surgery, kid_risk)
    }


    return tests
