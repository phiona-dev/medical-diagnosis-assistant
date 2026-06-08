import json

#load the json file
with open("knowledge_base.json", "r") as file:
    kb = json.load(file)
    
def display_symptoms():
    """Display available symptoms to the user"""
    print("\n AVAILABLE SYMPTOMS")
    symptoms = kb["symptoms"]
    
    for i in range(0, len(symptoms), 4):
        s1 = symptoms[i]  if i<len(symptoms) else ""
        s2 = symptoms[i+1]  if i+1<len(symptoms) else ""
        s3 = symptoms[i+2]  if i+2<len(symptoms) else ""
        s4 = symptoms[i+3]  if i+3<len(symptoms) else ""
        print(f"    -{s1:<22} - {s2:<22} - {s3:<22} -{s4:<22}")
        
        
#Get symptoms, risk factors and the vital signs from user
def get_patient_data():
    print("\nEnter Patient's Symptoms Separated by commas")
    symptom_input = input(" Symptoms:").strip()
    symptoms = [s.strip().title() for s in symptom_input.split(",") if s.strip()]
    
    risk_factors = []
    print("\nRISK FACTORS (answer yes/no)")
    risk_list = ["Recent Travel to Malaria Zone", "Contact with Infected Person", 
            "Weakened Immune System", "Poor Sanitation"]
    
    for risk in risk_list:
        if input(f"   {risk}? (yes/no): ").lower() == 'yes':
            risk_factors.append(risk)
    
    vital_signs = []
    print("\nVITAL SIGNS (answer yes/no)")
    vital_list = ["High Fever (>39°C)", "Rapid Breathing", "Low Blood Pressure"]
    for vital in vital_list:
        if input(f" {vital}? (yes/no)").lower() == "yes":
            vital_signs.append(vital)
            
    return symptoms, risk_factors, vital_signs
    
def main():
    print("MEDICAL EXPERT SYSTEM")
    print("Rule-Based Diagnosis with Forward Chaining")
    print("-"*50)
    
    display_symptoms()
    symptoms, risk_factors, vital_signs = get_patient_data()
    
    print("\n"+"-"*50)
    print("PATIENT INFORMATION SUMMARY")
    print(f"Symptoms: {symptoms if symptoms else "None entered"}")
    print(f"Risk Factors: {risk_factors if risk_factors else "None"}")
    print(f"Vital Signs: {vital_signs if vital_signs else "None"}")
    
if __name__ == "__main__":
    main()
    