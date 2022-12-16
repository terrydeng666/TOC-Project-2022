from fsm import TocMachine
# coding=utf-8

def create_machine():
    machine = TocMachine(
        states=["user", "menu", "region", "store_name", "random_store","store_info","store_menu", "store_comment",  "store_time", "store_address",
                 "taipei", "taichung", "tainan", "shinchu", "kaoshung", "taoyuan","test","name","fsm"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "test",
                "conditions": "is_going_to_test",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "region",
                "conditions": "is_going_to_region",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "store_name",
                "conditions": "is_going_to_store_name",
            },
            {
                "trigger": "advance",
                "source": "region",
                "dest": "taipei",
                "conditions": "is_going_to_taipei",
            },
            {
                "trigger": "advance",
                "source": ["taipei", "taichung", "tainan", "shinchu", "kaoshung", "taoyuan"],
                "dest": "store_info",
                "conditions": "is_going_to_store_info",
            },
            {
                "trigger": "advance",
                "source": "region",
                "dest": "taichung",
                "conditions": "is_going_to_taichung",
            },
            {
                "trigger": "advance",
                "source": "region",
                "dest": "tainan",
                "conditions": "is_going_to_tainan",
            },
            {
                "trigger": "advance",
                "source": "region",
                "dest": "shinchu",
                "conditions": "is_going_to_shinchu",
            },
            {
                "trigger": "advance",
                "source": "region",
                "dest": "kaoshung",
                "conditions": "is_going_to_kaoshung",
            },
            {
                "trigger": "advance",
                "source": "region",
                "dest": "taoyuan",
                "conditions": "is_going_to_taoyuan",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "store_name",
                "conditions": "is_going_to_store_name",
            },
            {
                "trigger": "advance",
                "source": "store_info",
                "dest": "store_menu",
                "conditions": "is_going_to_store_menu",
            },
            {
                "trigger": "advance",
                "source": ["store_menu","store_address","store_time","store_comment"],
                "dest": "store_info",
                "conditions": "go_back_store_menu",
            },
            
            # {
            #     "trigger": "advance",
            #     "source": "store_info",
            #     "dest": "store_commment",
            #     "conditions": "is_going_to_store_comment",
            # },
            # {
            #     "trigger": "advance",
            #     "source": "store_info",
            #     "dest": "store_photo",
            #     "conditions": "is_going_to_store_photo",
            # },
            {
                "trigger": "advance",
                "source": "store_info",
                "dest": "store_address",
                "conditions": "is_going_to_store_address",
            },
            {
                "trigger": "advance",
                "source": "store_info",
                "dest": "store_time",
                "conditions": "is_going_to_store_time",
            },
            {
                "trigger": "advance",
                "source": "store_info",
                "dest": "store_comment",
                "conditions": "is_going_to_store_comment",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "random_store",
                "conditions": "is_going_to_random_store",
            },
            {
                "trigger": "advance",
                "source": "store_name",
                "dest": "name",
                "conditions": "is_going_to_name",
            },
            {
                "trigger": "advance",
                "source": ["random_store","name"],
                "dest": "store_info",
                "conditions": "is_going_to_store_info",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "fsm",
                "conditions": "is_going_to_fsm",
            },
            {"trigger": "go_back", "source": ["region", "store_name","fsm","store_info"], "dest": "menu",},
            {"trigger": "advance", "source": ["region", "store_name", "random_store","store_info","store_menu", "store_comment",  "store_time", "store_address",
                 "taipei", "taichung", "tainan", "shinchu", "kaoshung", "taoyuan","test","name","fsm"], "dest": "menu",
                "conditions":"is_going_back"},
            {"trigger": "go_info", "source": ["name"], "dest": "store_info",},

            
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine