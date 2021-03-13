def get_all_questions_from_so_for_last_two_days():
    import time

    time_now = int(time.time())
    two_days_ago = time_now - 86400 * 2

    check_for_questions_on_page = 1
    page = 1
    list_of_questions = []

    while check_for_questions_on_page != 0:
        import requests
        resp = requests.get(
            "https://api.stackexchange.com//2.2/questions",
            params={
                "fromdate": two_days_ago,
                "todate": time_now,
                "tagged": "python",
                "site": "stackoverflow",
                "page": page,
                "pagesize": "100"
            }
        )
        resp.raise_for_status()
        questions = resp.json()["items"]

        check_for_questions_on_page = len(questions)

        if check_for_questions_on_page != 0:
            page += 1
            for question in questions:
                list_of_questions.append(question["title"])
    list_of_questions = set(list_of_questions)
    list_of_questions = list(list_of_questions)
    return list_of_questions


list_of_questions = get_all_questions_from_so_for_last_two_days()

print(len(list_of_questions))
for question in list_of_questions:
    print(question)
