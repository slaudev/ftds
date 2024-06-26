# SQL Assignment Instructions

![DB Schema](./assets/db-schema.png)

## Objective

Please implement the functions in `solution.py` as per the specifications provided.

## Functions to Implement

1. **retrieve_patient_names_and_genders()**:
    - Description: Retrieve all patient names and their genders.
    - Output: List of tuples with patient names and genders.

2. **list_all_doctors_and_specialties()**:
    - Description: List all doctors along with their specialties.
    - Output: List of tuples with doctor names and specialties.

3. **get_insurance_policies_for_patient(patient_id)**:
    - Description: Get all insurance policies for a specific patient (e.g., PatientID = 1).
    - Input: `patient_id` (int)
    - Output: List of tuples with insurance policies.

4. **find_appointments_for_patient(patient_id)**:
    - Description: Find all appointments for a specific patient (e.g., PatientID = 1) and display the corresponding doctor’s name and appointment details.
    - Input: `patient_id` (int)
    - Output: List of tuples with appointment details and doctors' names.

5. **list_all_diagnosed_diseases()**:
    - Description: List all diagnosed diseases (DiagnosisDescription) along with the patient name and the date of diagnosis.
    - Output: List of tuples with diseases, patient names, and dates.

6. **get_patients_prescribed_specific_medication(medication_id)**:
    - Description: Get all patients who were prescribed a specific medication (e.g., MedicationID = 1) along with the prescribed dosage and date range.
    - Input: `medication_id` (int)
    - Output: List of tuples with patient details, dosages, and dates.

7. **count_appointments_per_doctor()**:
    - Description: Find the number of appointments each doctor has had and order the results by the number of appointments in descending order.
    - Output: List of tuples with doctor names, their Specialities and appointment counts.

8. **list_patients_with_claims()**:
    - Description: List all patients along with the total amount claimed and the status of their most recent claims.
    - Output: List of tuples with patient details, total amounts claimed, and claim statuses.

9. **generate_lab_tests_report()**:
    - Description: Generate a report showing the patients' names, the lab test names, and their results for tests ordered in the last 30 days.
    - Output: List of tuples with patient names, lab test names, and results.

10. **most_common_procedure()**:
    - Description: Identify the most common procedure performed on patients and the total number of times it has been performed.
    - Output: A tuple with the most common procedure name and its count.

11. **find_doctors_with_overlapping_appointments()**:
    - Description: Find doctors who have overlapping appointments (time conflicts).
    - Output: List of tuples with doctor details and their overlapping appointments.

12. **find_active_patient_insurance_policies()**:
    - Description: Find all active (non-expired) insurance policies for patients.
    - Output: List of tuples with patient names, insurance details, and policy dates.

## Submission

1. Clone this repository.
2. Implement the required functions in `solution.py`.
3. Commit and push your changes to your GitHub repository.

## Notes

You do not need to run tests locally. Automated testing will be performed through GitHub Actions once you push your changes. Ensure your functions match the specified requirements, as the results of the tests will be based on these specifications.