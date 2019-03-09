# task 4


def solution(A):
    COST_DAY = 2
    COST_WEEK = 7
    COST_MONTH = 25

    def aux(pending_days_index):
        if pending_days_index >= len(A):
            return 0

        next_index_if_buy_day = pending_days_index + 1

        i = pending_days_index
        while i < len(A) and A[i] < A[pending_days_index] + 7:
            i += 1
        next_index_if_buy_week = i

        return min(COST_DAY + aux(next_index_if_buy_day),
                   COST_WEEK + aux(next_index_if_buy_week))

    return min(COST_MONTH, aux(0))
