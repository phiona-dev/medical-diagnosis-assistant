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

def main():
    print("MEDICAL EXPERT SYSTEM")
    print("Rule-Based Diagnosis with Forward Chaining")
    print("-"*50)
    
    display_symptoms()
    
if __name__ == "__main__":
    main()
    