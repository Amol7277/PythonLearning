# You want to check whether a web page loads within 3 seconds (performance test condition).
#
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

Time = float(input("Enter time in seconds: ").strip())

if Time >= 0 and Time <= 3:
    print("Page load time is Good")
else:
    print("Page load time is Slow")

