from datetime import datetime

dob, mob, yob = [int(x) for x in input("Enter your age (DD/MM/YYYY): ").split('/')]
bdy = datetime(yob, mob, dob)

print(f"you are {datetime.now() - bdy} old.")