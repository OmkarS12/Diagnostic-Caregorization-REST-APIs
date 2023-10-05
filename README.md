# CDSS_Labs
This is a CVD risk interpreter based on the ASCVD risk score and CVD lab results of a Patient.
The application is built using Python, FastAPI and Postgresql database. The end points accept patient's data and has following fields:
1. MRN: Medical Record Number
2. Name of the Patient
3. Age of the patient
4. Sex of the patient
It accepts the ASCVD Risk score of the patient and a primary careplan is generated based on the risk score in following format:
Directive Actions to be taken for writing prescriptions
Decision support for Medicines: In order to which to target and modifications to be done
rationale for these suggestions
Recommendations such as lifestyle and treatment changes

It accepts the Biomarkers of the patient and a Biomarker careplan is generated based on the risk score in following format:
Directive Actions to be taken for writing prescriptions
Decision support for Medicines: In order to which to target and modifications to be done
rationale for these suggestions
Recommendations such as lifestyle and treatment changes


alternatives to be considered.
Configuration-
1. Docker-compose build
2. Docker-compose up
3. for postgres: docker-compose run app alembic revision --autogenerate -m "New Migration"
4. docker-compose run app alembic upgrade head
