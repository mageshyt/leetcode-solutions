"""
"""
# ===================== PART 1 =====================
def lobbyBattery(batteries):
    joltage_sum = 0
    for battery in batteries:
        max_voltage = float('-inf')
        for i in range(len(battery)):
            for j in range(i+1,len(battery)):
                max_voltage = max(max_voltage , int(battery[i]+battery[j]))
        
        joltage_sum +=max_voltage

    return joltage_sum
# ===================== PART 2 =====================
"""

"""

def lobbyBattery2(batteries):
    joltage_sum = 0
    for battery in batteries:
        st = []

        for i in range(len(battery)):
            if not st:
                st.append(battery[i])
            else:

                if int(st[-1]) >= int(battery[i]):
                    st.append(battery[i])
                else:
                    while st and len(st) + (len(battery)-i) >12  and int(st[-1]) <  int(battery[i]):
                        st.pop()

                    st.append(battery[i])
        
        # remove extra
        while st and len(st) > 12:
            st.pop()
        print(st)
        joltage_sum += int(''.join(st))
    return joltage_sum

import os

os.chdir(os.path.dirname(__file__))
# read the input file
with open("input.txt", "r") as file:
    input_data = file.read().strip().split('\n')
    result = lobbyBattery(input_data)
    result2 = lobbyBattery2(input_data)
    print(result,result2)

