from ecology_bot.admin.admin.models.view import SecureModelView


class DistrictModelView(SecureModelView):
    column_list = ['name', 'type', 'region', 'parent.name']
    form_columns = ["name", "type", "region", "parent", "invite_link"]
    column_searchable_list = ["name", "region.name", "parent.name"]
    column_labels = {
        "name": "Название района",
        "type": "Тип",
        "region": "Регион",
        "parent": "Надрайон",
        "parent.name": 'Надрайон',
        "invite_link": "Ссылка на чат",
    }
    column_sortable_list = ['name']