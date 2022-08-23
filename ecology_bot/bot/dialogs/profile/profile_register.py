from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Cancel, Back

from ecology_bot.bot.dialogs.states import RegisterProfileSG
from ecology_bot.bot.services.repo import Repo
from ecology_bot.bot.windows.activity_window import ActivityWindow
from ecology_bot.bot.windows.confirm_window import ConfirmWindow
from ecology_bot.bot.windows.district_window import DistrictWindow
from ecology_bot.bot.windows.region_window import RegionWindow


async def complete_registration(c: CallbackQuery, widget: Any, dialog_manager: DialogManager):
    activities_widget = dialog_manager.dialog().find('m_activities')
    activity_ids = list(map(int, activities_widget.get_checked()))
    repo: Repo = dialog_manager.data['repo']
    region_id = dialog_manager.current_context().dialog_data['region_id']
    district_id = dialog_manager.current_context().dialog_data['district_id']

    await repo.user_dao.create_profile(
        user=await repo.user_dao.get_user(c.from_user.id),
        region_id=region_id,
        district_id=district_id,
        activities=await repo.activity_dao.get_activities(ids=activity_ids),
    )
    await c.message.answer(
        'Мы пришлем тебе уведомления на основе подписок! '
        'Также ты можешь зайти в меню каждой подписки и посмотреть подробности')
    dialog_manager.show_mode = ShowMode.SEND
    await dialog_manager.done()
    dialog_manager.show_mode = ShowMode.EDIT


def get_dialog() -> Dialog:
    region_window = RegionWindow(state=RegisterProfileSG.region, prev=Cancel)
    district_window = DistrictWindow(state=RegisterProfileSG.district)
    activity_window = ActivityWindow(state=RegisterProfileSG.activity, prev=Back)
    confirm_window = ConfirmWindow(
        text='Зарегистрировать профиль?',
        state=RegisterProfileSG.confirm,
        on_confirm=complete_registration,
    )
    profile_register = Dialog(
        region_window,
        district_window,
        activity_window,
        confirm_window,
    )
    return profile_register