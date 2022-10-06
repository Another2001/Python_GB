from CheckNumber import realnumb


def differ():
    mini = maxi = 0
    mini = min(realnumb())
    maxi = max(realnumb())
    diff = maxi - mini
    return print(' Разница между мин. и макс. эле - ми списка = ' + diff)
