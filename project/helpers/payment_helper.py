import logging
from datetime import datetime, timezone
from project.page.main_page import MainPage

logger = logging.getLogger(__name__)

def perform_payment(driver, card: dict, mode: str = "buy") -> datetime:
    label = "оплата дебетовой картой" if mode == "buy" else "покупка тура в кредит"
    logger.info(f"Открывается страница для {label}")
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode=mode)
    logger.info(f"Заполняется данными карты: {card.get('number', '—')}")
    payment_page.fill_card(card)
    order_id = datetime.now(timezone.utc)
    logger.info("Нажимается кнопка 'Продолжить'")
    if mode == "buy":
        payment_page.click_buy_button()
    else:
        payment_page.click_credit_button()
    return order_id