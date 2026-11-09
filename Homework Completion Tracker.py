
print("=====Homework Completion Tracker=====")

# PART 1: Set the homework count
total_homework = 4
original_count = total_homework

# PART 2: Create the counters
completed_count = 0
task_num = 1

# PART 3: Repeat until all tasks are completed
while task_num <= total_homework:

    # PART 4: Choose the task using its number
    if task_num == 1:
        next_task = "English Novel Reading"
    elif task_num == 2:
        next_task = "Math Worksheet"
    elif task_num == 3:
        next_task = "Science Project"
    else:
        next_task = "History Essay"

    answer = input(f"Have you completed {next_task}? (yes/no): ")

    # PART 5: Update counters only if completed
    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Great job! Task completed.")
    else:
        print("Okay, finish it and check again!")

    # PART 6: Show remaining homework
    print("Homework tasks remaining:", total_homework - completed_count)
    print()

# PART 7: Completion message
print("===== ALL HOMEWORK COMPLETE! =====")
print("Great work finishing your homework today!\n")

# PART 8: Safe infinite loop example
print("Now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0

while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1

    if safety_counter == 3:
        print("Stopping here on purpose!")
        break

# PART 9: Final summary
print("\n===== HOMEWORK COMPLETION SUMMARY =====")
print("Homework Assigned Today:", original_count)
print("Homework Completed:", completed_count)
print("Homework Remaining:", total_homework - completed_count)
print("=======================================")
