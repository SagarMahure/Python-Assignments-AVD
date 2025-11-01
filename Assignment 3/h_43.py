# # 24 hour format
# for h in range(0,24):
#     for m in range(0,60):
#         for s in range(0,60):
#             print(f"The time is : {h}:{m}:{s}")

# 12 hr format
for h in range(0,24):
    for m in range(0,60):
        for s in range(0,60):

            period = "AM" if h<12 else "PM"   ## Determine AM or PM

            h_12 = h % 12
            h_12 = 12 if h_12 == 0 else h_12  ## Convert to 12-hour format

            # Format with leading zeros (used :02 for leading zeroes)
            time_str = f"{h_12:02}:{m:02}:{s:02} {period}"
            print("The time is:", time_str)
