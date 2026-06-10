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
    risk_list = ["Recent Travel to Malaria Zone",
        "Contact with Infected Person",
        "Weakened Immune System",
        "Unprotected Sex",
        "Shared Needles",
        "Poor Sanitation",
        "Not Vaccinated"]
    
    for risk in risk_list:
        if input(f"   {risk}? (yes/no): ").lower() == 'yes':
            risk_factors.append(risk)
    
    vital_signs = []
    print("\nVITAL SIGNS (answer yes/no)")
    vital_list = ["High Fever (>39°C)", "Low Fever (37.5-39°C)",
        "Normal Temperature","Rapid Breathing", "Low Blood Pressure"]
    for vital in vital_list:
        if input(f" {vital}? (yes/no)").lower() == "yes":
            vital_signs.append(vital)
            
    return symptoms, risk_factors, vital_signs

#forward chaining: start with the symptoms, match rules and then reach the conclusion
def forward_chaining_diagnosis(symptoms, risk_factors, vital_signs):
    #combine all patient facts
    patient_facts = symptoms + risk_factors + vital_signs
    diagnoses=[]
    
    #check each rule
    for rule in kb["rules"]:
        required_symptoms = rule["if"]
        
        #count how many required symptoms match
        matched_symptoms=[]
        missing_symptoms=[]
        
        for req in required_symptoms:
            req_lower = req.lower()
            if req_lower in [fact.lower() for fact in patient_facts]:
                matched_symptoms.append(req)
            else:
                missing_symptoms.append(req)
        
        
        #calculate confidence percentage
        match_percentage = (len(matched_symptoms) / len(required_symptoms)) * 100
        
        #if confidence is high enough (>= 75%), add to diagnoses
        if match_percentage >= 75:
            diagnoses.append({
                "disease": rule["then"],
                "severity": rule["severity"],
                "urgency": rule["urgency"],
                "treatment": rule["treatment"],
                "confidence": round(match_percentage, 1),
                "matched_symptoms": matched_symptoms,
                "missing_symptoms": missing_symptoms,
                "rule_used": rule["id"]
            })
    #sort by confidence(highest first)
    diagnoses.sort(key=lambda x: x["confidence"], reverse=True)
    
    return diagnoses

#explains why each conclusion was reached
def explain_diagnoses(diagnoses):
    if not diagnoses:
        return "\n No diagnosis could be made. No rules were triggered."
    
    print("\n" + "-"*50)
    print("EXPLANATION")
    
    for i, diag in enumerate(diagnoses[:3], 1):
        print(f"\n DIAGNOSIS #{i}: {diag['disease']}\n")
        print(f"The rule '{diag["rule_used"]}' was triggered because: \n")
        
        for symptom in diag["matched_symptoms"]:
            print(f"Patient has: {symptom}")

        if diag["missing_symptoms"]:
            print(f"\nMissing for full confirmation:")
            for symptom in diag["missing_symptoms"][:3]:
                print(f"{symptom} (not reported)")
        
        print(f"Therefore, the system diagnosed: {diag["disease"]}")
        print(f"Confidence: {diag["confidence"]}%")
        print(f"Recommendation: {diag["urgency"]}\n")
    
def main():
    print("MEDICAL EXPERT SYSTEM")
    print("Rule-Based Diagnosis with Forward Chaining")
    print("-"*50)
    
    display_symptoms()
    
    #get patient data
    symptoms, risk_factors, vital_signs = get_patient_data()
    
    print("\n"+"-"*50)
    print("PATIENT INFORMATION SUMMARY")
    print(f"Symptoms: {symptoms if symptoms else 'None entered'}")
    print(f"Risk Factors: {risk_factors if risk_factors else "None"}")
    print(f"Vital Signs: {vital_signs if vital_signs else "None"}")
    
    #run diagnoses
    print("\n" + "-"*50)
    print("RUNNING DIAGNOSES (Forward chaining)")
    diagnoses = forward_chaining_diagnosis(symptoms, risk_factors, vital_signs)
    
    #display results
    if diagnoses:
        print("\n POSSIBLE DIAGNOSES (sorted by confidence)")
        for i, diag in enumerate(diagnoses[:5], 1): #show top 5 diagnoses
            print(f"\n{i}. {diag['disease']}")
            print(f"   Confidence: {diag['confidence']}%")
            print(f"   Severity: {diag['severity']}")
            print(f"   Urgency: {diag['urgency']}")
            print(f"   Treatment: {diag['treatment']}")
            
        #show explanation
        explain_diagnoses(diagnoses)
    else:
        print("\nNo diagnosis could be made with the provided symptoms.")
    
if __name__ == "__main__":
    main()
    