

def main():
    input_1 = input().split()
    num_p = int(input_1[0])
    num_d = int(input_1[1])
    doctors = []

    for num in range(num_d):
     patients = input().split()
     patients_list = []
     for patient in patients:
         patients_list.append(int(patient))
     doctors.append(patients_list)

    print(doctors)




main()