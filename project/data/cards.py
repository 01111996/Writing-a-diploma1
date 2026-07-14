BASE_URL = "http://localhost:8080/"

class TestCard:
    #Валидные данные карты
    APPROVED_CARD = {
    "number": "4444 4444 4444 4441",
    "month": "08",
    "year": "27",
    "owner": "Ivan Ivanovich Vetrov",
    "cvc": "999",
    "transaction_type": "credit" #для кредита
}
    #Невалидные данные карты
    DECLINED_CARD = {
    "number": "4444 4444 4444 4442",
    "month": "08",
    "year": "15",
    "owner": "Ivan Ivanovich Vetrov",
    "cvc": "999",
    "transaction_type": "credit" #для кредита
}
    
    #15 цифр в номере карты
    MISSING_NUMBER_CARD = {
    "number": "4444 4444 4444 444",
    "month": "08",
    "year": "27",
    "owner": "Ivan Ivanovich Vetrov",
    "cvc": "999",
}
    
    #без номера карты
    WITHOUT_CARD = {
    "number": " ",
    "month": "08",
    "year": "27",
    "owner": "Ivan Ivanovich Vetrov",
    "cvc": "999",   
}
    
    #CVC из двух цифр
    CVC_CARD = {
    "number": "4444 4444 4444 4441",
    "month": "08",
    "year": "27",
    "owner": "Ivan Ivanovich Vetrov",
    "cvc": "35",   
}
    
    #без CVC
    CVC1_CARD = {
    "number": "4444 4444 4444 4441",
    "month": "08",
    "year": "27",
    "owner": "Ivan Ivanovich Vetrov",
    "cvc": " ",
}

#ФИО на русском
    CYRILLIC_CARD = {
    "number": "4444 4444 4444 4441",
    "month": "08",
    "year": "27",
    "owner": "Иван Иванович Ветров",
    "cvc": "999",
}
    
    #без фамилии
    F_CARD = {
    "number": "4444 4444 4444 4441",
    "month": "08",
    "year": "27",
    "owner": "Ivan Ivanovich",
    "cvc": "999",
}
    
    #без имени
    N_CARD = {
    "number": "4444 4444 4444 4441",
    "month": "08",
    "year": "27",
    "owner": "Ivanovich Vetrov",
    "cvc": "999",
}
