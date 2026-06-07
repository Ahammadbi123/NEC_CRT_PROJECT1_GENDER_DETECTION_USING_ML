import pandas as pd

# 1. Massive Names Patterns (Real Indian Context)
male_names = [
    'harish', 'rajesh', 'mahesh', 'suresh', 'anil', 'sunil', 'pawan', 'kalyan', 'rahul', 'rohit',
    'vijay', 'ajay', 'sandeep', 'naveen', 'vamsi', 'kiran', 'venkat', 'ramesh', 'prasad', 'nani',
    'shiva', 'ganesh', 'kartik', 'arjun', 'vikram', 'aditya', 'sai', 'prakash', 'abhishek', 'manoj',
    'deepak', 'ashok', 'krishna', 'ram', 'lakshman', 'bharath', 'vinay', 'charan', 'karthik',
    'bhaskar', 'sekhar', 'mohan', 'krish', 'vicky', 'bunty', 'chintu', 'somu', 'ramu', 'babu',
    'raghu', 'madhu', 'srinivas', 'venky', 'balu', 'srinu', 'koti', 'raja', 'rathnam', 'naidu',
    'chowdary', 'reddy', 'rao', 'verma', 'sharma', 'gupta', 'singh', 'khan', 'shaik', 'akram'
] * 15 # Repeat to increase weight

female_names = [
    'anitha', 'sunitha', 'kavitha', 'lavanya', 'priyanka', 'deepika', 'swathi', 'ramya', 'sravani', 'divya',
    'sneha', 'meghana', 'pallavi', 'keerthi', 'shanthi', 'lakshmi', 'parvathi', 'sita', 'geetha', 'vani',
    'anupama', 'sindhu', 'harini', 'sahithi', 'rupa', 'mounika', 'bhargavi', 'gayatri', 'kusuma', 'indira',
    'madhavi', 'shailaja', 'tulasi', 'revathi', 'jyothi', 'sumathi', 'hema', 'pavani', 'sirisha',
    'bhavani', 'durga', 'lalitha', 'sarala', 'nirmala', 'shanti', 'roopa', 'leela', 'jaya', 'vijaya',
    'lakshmamma', 'venkatamma', 'ratnam', 'nagmani', 'padma', 'shravya', 'vyshnavi', 'amulya', 'ananya'
] * 15 # Repeat to increase weight

# Combine and save
names = male_names + female_names
genders = ['male'] * len(male_names) + ['female'] * len(female_names)

df = pd.DataFrame({'name': names, 'gender': genders})
df = df.drop_duplicates().sample(frac=1).reset_index(drop=True) # Shuffle data
df.to_csv('dataset.csv', index=False)

print(f"✅ Big Dataset Created with {len(df)} Unique Names!")