judges_count = int(input())
presentation_count = 0
total_total_score = 0

command = input() #"Finish" or name of presentation
while command != "Finish":

    presentation = command
    total_score = 0
    presentation_count += 1

    for _ in range(judges_count):
        total_score += float(input())

    avg_score = total_score / judges_count
    print(f"{presentation} - {avg_score:.2f}.")
    total_total_score += total_score


    command = input()
overall_score = total_total_score / (presentation_count * judges_count)
print(f"Student's final assessment is {overall_score:.2f}.")