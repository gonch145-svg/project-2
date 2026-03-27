
#Function that calculates the variables needed to calculate the completion rate of users who completed the whole process (start-->confirm), without missing a step 

def completion_var(df):
#Set the required steps a user needs to follow to complete the online process
    required_steps = {"start","step_1","step_2","step_3","confirm"}
    
#Groups by each visit_id (unique user), selects only the process_step column, and converts all steps in each visit into a set of unique steps for each visit_id. By using a set it ignores duplicated and the order of the steps it just makes sure that each user that has reached confirmed has at least finished each step once. 

    visit_steps = df.groupby("visit_id")["process_step"].apply(set)

#Calculates the number of users who completed the whole process by checking that all required steps inside the users step set and repeats this for each visit_id giving you the count of users/visit_id's that completed the process

    completed = visit_steps.apply(lambda x: required_steps.issubset(x)).sum()
    total = df["visit_id"].nunique()
    return completed, total




#Calculates the completion rate by dividing the total number of users(unique visit_id) that completed the whole process by the total number of users who started the process and gives it back as a percentage

def completion_rate(completed: int, total: int, label=""):
    if total == 0:
        raise ZeroDivisionError ("Cannot divide by zero")
    completion_rate = (completed / total) * 100
    print(f"Completion rate {label}: {completion_rate:.2f}%")
    return completion_rate


#This function calculates the relative percentage change between a control value and a test value to measure how much the test result improved or decreased relative to the control.
def relative_change(control: float, test: float):
    if control == 0:
        print("Cannot compute relative change (control = 0)")
        return 0
    relative_change = ((test - control) / control) * 100
    print(f"The relative change from {control:.2f}% to {test:.2f}% is {relative_change:.2f}%")
    return relative_change


#Calculate completion rates for each step in a funnel.

#Parameters
    #df : pandas.DataFrame --> DataFrame containing the funnel events.
    #steps : list --> Ordered list of funnel steps.
    #user_col : str --> Column identifying unique users or visits (default: visit_id).
    #step_col : str --> Column containing the step name (default: process_step)

def cr_steps(df, steps, user_col="visit_id", step_col="process_step"):
# Keep only relevant columns and remove duplicate (user, step) combinations so each user is counted once per step
    df_clean = df[[user_col, step_col]].drop_duplicates()

 # Create a dictionary mapping each step to the set of users who reached it
    step_users = {
        step: set(df_clean[df_clean[step_col] == step][user_col])
        for step in steps}
    
    results = []

# Loop through the ordered steps   
    for i, step in enumerate(steps):
# Get users who reached the current step
        current_users = step_users.get(step, set())
        
# Special case for the first step --> all users who reached the first step attempted and completed it
        if i == 0:
            started = len(current_users)
            completed = len(current_users)
        else:
# Users who reached the previous step
            prev_users = step_users.get(steps[i-1], set())
# Users who progressed from previous step to current step
            progressed = prev_users & current_users
# Number of users attempting the step            
            started = len(prev_users)
# Number of users completing the step
            completed = len(progressed)
# Calculate completion rate, protecting against division by zero 
        rate = completed / started if started else 0

        results.append({
            "step": step,
            "attempts": started,
            "completions": completed,
            "completion_rate": rate})
# Convert results list into a DataFrame for easy analysis
    return pd.DataFrame(results)



def missing_start(df: pd.DataFrame):
    # Sort the dataframe so events within each visit are in chronological order
    # This ensures we correctly identify the first step taken in each visit

    # Group by visit_id and select the first recorded process_step for each visit
    # This gives the starting step of each visit

    # Identify visits where the first step is not "start"
    # Bad visits represent visits that entered the funnel mid-process
   
    # Return the visit_ids of visits that did not begin with "start"


    def missing_start (df: pd.DataFrame) --> pd.DataFrame:
    start_users = set(df[df["process_step"] == "start"]["visit_id"])
    all_users = set(df["visit_id"])
    missing_start = all_users - start_users
    df = df[~df["visit_id"].isin(missing_start)]
    return df