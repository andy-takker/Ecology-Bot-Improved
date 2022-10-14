ON_HELP_TEXT = "on_help_text"
ON_ORG_REGISTRATION_END_TEXT = "on_org_registration_end_text"
ON_PROFILE_REGISTRATION_END_TEXT = "on_profile_registration_end_text"
ON_RETURN_TEXT = "on_return_text"
ON_START_TEXT = "on_start_text"
ON_GLOBAL_EVENT_LIST = "on_global_event_list"
ON_SUBSCRIBE_GLOBAL_EVENT = "on_subscribe_global_event"
ON_UNSUBSCRIBE_GLOBAL_EVENT = "on_unsubscribe_global_event"

MESSAGE_KEYS = (
    (ON_HELP_TEXT, 'Сообщение "Что может этот бот?"'),
    (ON_ORG_REGISTRATION_END_TEXT, "Сообщение в конце регистрации организации"),
    (ON_PROFILE_REGISTRATION_END_TEXT, "Сообщение в конце регистрации профиля"),
    (ON_RETURN_TEXT, "Сообщение при возвращении пользователя"),
    (ON_START_TEXT, "Сообщение для нового пользователя"),
    (ON_GLOBAL_EVENT_LIST, "Сообщение для списка глобальных событий"),
    (ON_SUBSCRIBE_GLOBAL_EVENT, "Сообщение о подписке на мероприятие"),
    (ON_UNSUBSCRIBE_GLOBAL_EVENT, "Сообщение об отписке от мероприятия"),
)

DEFAULT_MESSAGES = {
    ON_HELP_TEXT: (
        "С помощью бота волонтеры могут получать персонализированные "
        "уведомления о мероприятиях и волонтерских вакансиях в своем "
        "районе, а экологически активные сообщества - найти волонтеров и"
        " привлечь участников на свои мероприятия и акции.\n\nБот может "
        "пригласить Вас в чат, где собрались экоактивисты из вашего "
        "района. Общайтесь, делитесь опытом, объединяйтесь для создания"
        " экособытий!\n\nСовсем скоро всем пользователям бота будет "
        "доступна справочная информация: адреса пунктов приема "
        "вторсырья, контакты движений и организаций.\n\n"
        "Пока работает пилотная версия, функционал будет расширяться."
    ),
    ON_ORG_REGISTRATION_END_TEXT: (
        "Организация создана и отправлена на модерацию! "
        "Когда мы ее проверим, Вы получите уведомление."
    ),
    ON_PROFILE_REGISTRATION_END_TEXT: (
        "Мы пришлем тебе уведомления на основе подписок! "
        "Также ты можешь зайти в меню каждой подписки и посмотреть подробности"
    ),
    ON_RETURN_TEXT: "С возвращением!",
    ON_START_TEXT: (
        "Привет!\n"
        "Это пилотная версия экобота Союза эковолонтерских "
        "организаций.\nЗдесь Вы сможете узнать об экологических "
        "мероприятиях и проектах, стать волонтёром или найти "
        "единомышленников.\n Сейчас бот работает с Ленинградской"
        " областью, но далее охватит другие регионы.\n"
        "Помогите улучшить бота: опробуйте весь функционал."
    ),
    ON_GLOBAL_EVENT_LIST: ("Активные мероприятия, на которые можно подписаться"),
    ON_SUBSCRIBE_GLOBAL_EVENT: ("Вы подписались на мероприятие!"),
    ON_UNSUBSCRIBE_GLOBAL_EVENT: ("Вы отписались от мероприятия!"),
}
