from db_config import connect_to_db

def retrieve_patient_names_and_genders():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT PatientName, Gender FROM patients;
    """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def list_all_doctors_and_specialties():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
     SELECT DoctorName, Specialty FROM doctors;
     """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_insurance_policies_for_patient(patient_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT PolicyNumber, EffectiveDate, ExpirationDate from patient_insurance where PatientID = {patient_id};
     """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def find_appointments_for_patient(patient_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT a.AppointmentDate, a.AppointmentTime, a.AppointmentReason, d.DoctorName
    FROM appointments a
    INNER JOIN doctors d ON a.DoctorID = d.DoctorID
    WHERE a.PatientID = {patient_id};
     """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def list_all_diagnosed_diseases():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            p.PatientName,
            d.DiagnosisDescription,
            a.AppointmentDate
        FROM diagnoses d
        INNER JOIN appointments a ON a.AppointmentID = d.AppointmentID 
        INNER JOIN patients p ON p.PatientID = a.PatientID
     """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_patients_prescribed_specific_medication(medication_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT
            p.PatientName,
            premed.PrescribedDosage,
            premed.StartDate,
            premed.EndDate
        FROM appointments a
        INNER JOIN patients p ON a.PatientID = p.PatientID 
        INNER JOIN prescribed_medications premed ON a.AppointmentID = premed.AppointmentID
        INNER JOIN medications m ON m.MedicationID = premed.MedicationID
        WHERE premed.MedicationID = {medication_id};
     """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def count_appointments_per_doctor():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            d.DoctorName,
            d.Specialty,
            COUNT(a.DoctorID) as ApptCount
        FROM doctors d
        INNER JOIN appointments a ON a.DoctorID = d.DoctorID 
        GROUP BY a.DoctorID
        ORDER BY ApptCount DESC
     """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def list_patients_with_claims():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            p.PatientName,
            SUM(c.ClaimAmount),
            c.ClaimStatus
        FROM patients p
        INNER JOIN claims c ON c.PatientID = p.PatientID
        GROUP BY p.PatientName, c.ClaimStatus
        ORDER BY p.PatientName ASC, c.ClaimStatus ASC
     """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def generate_lab_tests_report():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            p.PatientName,
            tests_type.LabTestName,
            tests_ordered.Result
        FROM patients p
        INNER JOIN patient_lab_tests tests_ordered ON tests_ordered.PatientID = p.PatientID
        INNER JOIN lab_tests tests_type ON tests_type.LabTestID = tests_ordered.LabTestID
        WHERE (CURRENT_DATE() - INTERVAL 30 DAY) <= tests_ordered.OrderedDate
     """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def most_common_procedure():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
     SELECT  name, num
        FROM (
            SELECT
                p.ProcedureName AS name, COUNT(pp.ProcedureID) AS num
            FROM patient_procedures pp
                INNER JOIN procedures p ON pp.ProcedureID = p.ProcedureID
            GROUP BY p.ProcedureName
        )  AS proc_counts
        ORDER BY num DESC
        LIMIT 1;
     """) 
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def find_doctors_with_overlapping_appointments():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""     
      SELECT DISTINCT
                   a1.DoctorID,
                   d.DoctorName,
                   a1.AppointmentID,
                   a1.AppointmentDate,
                   a1.AppointmentTime,
                   a2.AppointmentID,
                   a2.AppointmentDate,
                   a2.AppointmentTime
        FROM appointments a1
        JOIN appointments a2
        ON 
                a1.DoctorID = a2.DoctorID AND
                a1.AppointmentID <> a2.AppointmentID AND
                a1.AppointmentDate = a2.AppointmentDate AND
                a1.AppointmentTime < a2.AppointmentTime AND
               ABS(TIMESTAMPDIFF(SECOND, a1.AppointmentTime, a2.AppointmentTime)) < 1800
        JOIN doctors d
        ON
                d.DoctorID = a1.DoctorID
        ORDER BY a1.DoctorID, a1.AppointmentDate, a1.AppointmentTime
      
     """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def find_active_patient_insurance_policies():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT  PatientName, PolicyNumber, EffectiveDate    
        FROM patient_insurance insur
        INNER JOIN patients p ON insur.PatientID = p.PatientID
        WHERE ExpirationDate >= CURRENT_DATE()
    """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

