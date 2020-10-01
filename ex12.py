def percent_list(votes, n):
    """принимает список голосов, создает из него новый список [№ участника, процент голосов]"""
    sum = 0
    percent_list = []
    for i in votes:
        sum += i
    for i in range(0, n):
        percent_list.append(i)
        current_candidate = (votes[i] / sum) * 100
        current_candidate = float('{:.2f}'.format(current_candidate))
        percent_list.append(current_candidate)
    return percent_list


def results(perc_list=list):
    """Выбирает максимальный результат(процент) и определяет было ли повторение максимального результата,
    возвращает список [мах, %]"""
    max_votes = perc_list[1]
    equal_votes = False  # Повторение максимального результата
    for i in range(3, len(perc_list),2):
        if perc_list[i] == max_votes:
            equal_votes = True
        if perc_list[i] > max_votes:
            max_votes = perc_list[i]
            equal_votes = False
    return [max_votes, equal_votes]


def publication(results_list=list, list_of_percent=list):
    """Публикация результатов"""
    if results_list[1] is True:  # ничья, перевыборы при равенстве %
        result = 'no winner'
        return result
    if results_list[0] > 50:  # победа по процентам при 50 и более
        index_of_winner = list_of_percent[list_of_percent.index(results_list[0]) - 1] + 1
        result = f'majority winner {index_of_winner}'
        return result
    if results_list[0] <= 50:  # победа по процентам менее 50
        index_of_winner = list_of_percent[list_of_percent.index(results_list[0]) - 1] + 1
        result = f'minority winner {index_of_winner}'
        return result


def MassVote(n, votes):
    list_of_percent = percent_list(votes, n)
    result = results(list_of_percent)
    victory = publication(result, list_of_percent)
    return victory


a = MassVote(4, [150, 10, 100, 100])
print(a)






