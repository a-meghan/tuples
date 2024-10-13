def format_flight(schedule_info):
    formatted_schedule = []
    for info in schedule_info:
        flyer_name, take_off, destination = info
        formatted_scheduleInfo = f"{flyer_name} is going from {take_off} to {destination}."
        formatted_schedule.append(formatted_scheduleInfo)
    return "\n".join(formatted_schedule)
# Note to self: newline + join ensures that output comes back
# formatted rather than returning the sentences in a list form.

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(format_flight(itineraries))