no_of_hours_browsed=int(input("enter no of hours browsed"))
no_of_mins_browsed=int(input("enter no of mins browsed"))
total_time_browsed=no_of_mins_browsed+no_of_hours_browsed*60
print(f"total time browsed={total_time_browsed}mins")
amount=no_of_hours_browsed*50+no_of_mins_browsed

if no_of_hours_browsed>7:

    raise ValueError("you have exceeded the max time lim.")
    end

elif no_of_hours_browsed>=5:
    print(200+((no_of_hours_browsed-5)*50+no_of_mins_browsed))
else:
    print(amount)







