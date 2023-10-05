# from patient import Patient
# from risk_category import Risk_Category
# from lipid_biomarkers import Lipid_Biomarkers
# from careplan import CarePlan

# patient = Patient(
#     123456789,
#     'John Doe',
#     35,
#     'Male'
# )

# lipid_biomarkers = Lipid_Biomarkers(
#     hdl_c=30, ldl_c=120, lp_a=180, triglycerides=200, apo_b=105, hs_crp=0.4, apo_a1=148.2, units='mg/dl'
# )

# risk_category = Risk_Category(
#     ascvd_score=25,
# )

# careplan = CarePlan(
#     actions='abcd',
#     medications='efgh',
#     rationale='ijkl',
#     recommendations='mnop',
#     alternatives='qrst'
# )


# risk_category.cvd_risk()
# print(risk_category.ascvd_score)

# # print("ASCVD Risk:", risk_category.ascvd_risk)

# # careplan.ascvd_careplan(risk_category)
# # print(careplan.actions,
# #       careplan.medications,
# #       careplan.rationale,
# #       careplan.recommendations,
# #       careplan.alternatives)

# # lipid_biomarkers.check_and_convert_units()

# # lipid_biomarkers.biomarker_risk()

# # print("HDL-C Risk:", lipid_biomarkers.hdl_c_risk)
# # print("LDL-C Risk:", lipid_biomarkers.ldl_c_risk)
# # print("LP(a) Risk:", lipid_biomarkers.lp_a_risk)
# # print("Triglycerides Risk:", lipid_biomarkers.triglycerides_risk)
# # print("Apo-B Risk:", lipid_biomarkers.apo_b_risk)
# # print("Apo-A1 Risk:", lipid_biomarkers.apo_a1_risk)
# # print("hs-CRP Risk:", lipid_biomarkers.hs_crp_risk)

# # careplan.biomarker_careplan(lipid_biomarkers)
# # print(careplan.actions,
# #       careplan.medications,
# #       careplan.rationale,
# #       careplan.recommendations,
# #       careplan.alternatives)
