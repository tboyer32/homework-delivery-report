def process_deliveries(the_file, day):
    print(f"Day {day}")
    
    the_file = open("um-deliveries-day-1.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for a total of ${amount}")
    the_file.close()

process_deliveries("um-deliveries-day-1.txt", 1)
process_deliveries("um-deliveries-day-2.txt", 2)
process_deliveries("um-deliveries-day-3.txt", 3)