day_rest = int(input())
minutes_needed_for_rest = 30000
when_working = 63
when_resting = 127
working_days = 365 - day_rest

summary = (working_days * 63) + (day_rest * 127)
complete_summary = minutes_needed_for_rest - summary
hours = 0
minutes = 0

if summary < minutes_needed_for_rest:
    hours = complete_summary // 60
    minutes = complete_summary % 60
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    complete_summary = summary - minutes_needed_for_rest
    hours = complete_summary // 60
    minutes = complete_summary % 60
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
