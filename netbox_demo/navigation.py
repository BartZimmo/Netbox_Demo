from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton


accesslist_buttons = [
    PluginMenuButton(
        link='plugins:netbox_demo:accesslist_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]

accesslistrule_buttons = [
    PluginMenuButton(
        link='plugins:netbox_demo:accesslistrule_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_demo:accesslist_list',
        link_text='Access Lists',
        buttons=accesslist_buttons

    ),
    PluginMenuItem(
        link='plugins:netbox_demo:accesslistrule_list',
        link_text='Access List Rules',
        buttons=accesslist_buttons
    ),
)


