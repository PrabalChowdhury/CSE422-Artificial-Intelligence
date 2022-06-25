import math
import random as Li

identity_st = input("Give student ID : \n")
turn_t = int(identity_st[0]) * 2

health_HP = int(identity_st[-2:][::-1])

lwR, hwR = [int(char) for char in input().split()]


brnch_t = int(identity_st[2])

lvs_ea = []
for i in range(0, turn_t ** brnch_t + 1):
    lvs_ea.append(Li.randrange(lwR, hwR + 1))




print("Depth and Branch ratio is", turn_t, ":", brnch_t)
print("Terminal States are ", *lvs_ea)


check_C = 0

def prunfn(tr_dep, pos, mxPlayer, leaf, alp, beta):
    global check_C
    global turn_t
    global brnch_t

    l = len(lvs_ea)


    if tr_dep == turn_t:
        return leaf[pos]

    if mxPlayer:

        BestV_l = -math.inf

        for j in range(0, brnch_t):

            Xd = prunfn(tr_dep + 1, pos * brnch_t + j, False, leaf, alp, beta)
            BestV_l = max(BestV_l, Xd)
            alp = max(alp, BestV_l)

            if beta <= alp:
                crn_Ch = int((l - 1) / (turn_t - tr_dep))
                cur_pos = pos * brnch_t + j
                if crn_Ch - 1 != cur_pos:
                    check_C += (brnch_t - (cur_pos % brnch_t))-1
                break

        return BestV_l

    else:
        BestV_l = math.inf

        for j in range(0, brnch_t):

            Xd = prunfn(tr_dep + 1, pos * brnch_t + j, True, leaf, alp, beta)
            BestV_l = min(BestV_l, Xd)
            beta = min(beta, BestV_l)


            if beta <= alp:
                crn_Ch = int((l - 1) / (turn_t - tr_dep))
                cur_pos = pos * brnch_t + j
                if crn_Ch - 1 != cur_pos:
                    check_C += (brnch_t - (cur_pos % brnch_t)) - 1
                break
        return BestV_l


abacd = prunfn(0, 0, True, lvs_ea, -math.inf, math.inf)
print("Left Health of the defender after maximum damage caused by the attacker is", health_HP - abacd)
print("After Alpha-Beta Pruning Leaf Node Comparisons ", (len(lvs_ea)-check_C))
