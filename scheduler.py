from schedule_helpers import generate_schedule, print_summary, schedule_summary, teams_from_signup

def main():
    print("Welcome to the Schedule Generator!\n")
    
    # Get user input for teams, weeks, and groups
    print("signup file must be in the bpl_logic directory.")
    file_path = str(input("Enter the name of the .xlsx file containing the team signup (ex: team_signup.xlsx): "))

    teams = teams_from_signup(file_path)

    num_wks = int(input("How many weeks would you like the schedule to run? "))
    num_groups = int(input("How many groups of teams would you like to have each week? "))

    # Generate schedule
    result_schedule = generate_schedule(teams, num_wks, num_groups)

    # Display the schedule in a more structured format
    print("Schedule:")
    for i, week in enumerate(result_schedule, 1):
        print(f"Week {i}:")
        for j, group in enumerate(week, 1):
            print(f"  Group {j}: {', '.join(group)}")
        print()

    # Generate and display schedule summary
    summary = schedule_summary(result_schedule)
    print_summary(summary)

if __name__ == "__main__":
    main()


