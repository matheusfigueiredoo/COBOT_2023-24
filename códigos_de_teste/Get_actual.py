import rtde_receive
rtde_r = rtde_receive.RTDEReceiveInterface("10.224.2.69")

actual_q = rtde_r.getActualQ()


print(actual_q)