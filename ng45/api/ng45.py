"""NG45 functionality

A collection of functions that return required tests as per NICE guideline ng45

"""

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
