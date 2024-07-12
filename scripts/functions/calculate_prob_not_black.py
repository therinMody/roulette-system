def calculate_prob_not_black(spins, total_slots=38, black_slots=18):
    not_black_slots = total_slots - black_slots
    prob_not_black_one_spin = not_black_slots / total_slots
    return prob_not_black_one_spin ** spins