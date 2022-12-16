from transitions.extensions import GraphMachine
from utils import push_message ,tainan_list,send_menu,tainan_menu,taichung_list,send_names,send_address,send_time,send_comment,taipei_list,kaoshung_list,shinchu_list,taoyuan_list,rand_store,search_name
from utils import send_text_message ,send_fsm
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage ,ImageSendMessage
# coding=utf-8
global store_id
store_id=-1
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        print("entering menu state")
        
        return True
    def is_going_to_random_store(self,event):
        text = event.message.text
        return "random" in text.lower()
    def is_going_back(self, event):
        text = event.message.text
        # if(text.lower()=="go_back"): self.go_back(event)
        return "go_back" in text.lower()
    def is_going_to_fsm(self,event):
        text=event.message.text
        return "fsm" in text.lower()
    def is_going_to_region(self, event):
        global store_id
        store_id=-1
        text = event.message.text
        return  "region" in text.lower()
    def is_going_to_taipei(self, event):
        text = event.message.text
        return "台北" in text
    def is_going_to_taichung(self, event):
        text = event.message.text
        return "台中" in text
    def is_going_to_tainan(self, event):
        text = event.message.text
        return "台南" in text
    def is_going_to_shinchu(self, event):
        text = event.message.text
        return "新竹" in text
    def is_going_to_kaoshung(self, event):
        text = event.message.text
        return "高雄" in text
    def is_going_to_taoyuan(self, event):
        text = event.message.text
        return "桃園" in text
    def is_going_to_test(self,event):
        text=event.message.text
        return "test" in text
    def is_going_to_store_name(self,event):
        text=event.message.text
        return  "name" in text.lower()
    def is_going_to_store_info(self,event):
        text=event.message.text
        return True
    def is_going_to_name(self,event):
        text=event.message.text
        return True
    def is_going_to_store_menu(self,event):
        text=event.message.text
        return  "menu" in text.lower()
    def is_going_to_store_address(self,event):
        text=event.message.text
        return "address" in text.lower()
    def is_going_to_store_time(self,event):
        text=event.message.text
        return "time" in text.lower()
    def is_going_to_store_comment(self,event):
        text=event.message.text
        return "comment" in text.lower()
    def go_back_store_menu(self,event):
        text=event.message.text
        return "more" in text.lower()
    def on_enter_store_comment(self,event):
        print("in comment")
        send_comment(event.source.user_id,store_id-1)
        tmp="請輸入\"more\"來選擇其他店家資訊"
    def on_enter_random_store(self,event):
        print("in random")
        global store_id
        store_id=rand_store(event.source.user_id)
        tmp="請輸入\"show\"來取得隨機店家資訊"
        push_message(event.source.user_id,tmp)
    def on_enter_store_time(self,event):
        print("in time")
        send_time(event.source.user_id,store_id-1)
        tmp="請輸入\"more\"來選擇其他店家資訊"
        push_message(event.source.user_id,tmp)
    def on_enter_store_info(self,event):
        global store_id
        if(store_id == -1):
            store_id=int(event.message.text)
            if(store_id >10):
                push_message(event.source.user_id,"超過清單長度!")
                self.go_back(event)
                return
        send_names(event.source.user_id,store_id-1)
    def on_enter_fsm(self,event):
        send_fsm(event.source.user_id)
        self.go_back(event)
        
    def on_enter_name(self,event):
        print("name")
        global store_id
        x=search_name(event.message.text,event.source.user_id)
        if(x!=-1):
            store_id=x
            self.go_info(event)
        else:
            push_message(event.source.user_id,"無此結果，請在試一次")
            self.go_back(event)
    def on_enter_store_name(self,event):
        print("search_name")
        push_message(event.source.user_id,"請輸入店家名稱")
            
    def on_enter_store_menu(self,event):
        send_menu(event.source.user_id,store_id-1)
        tmp="請輸入\"more\"來選擇其他店家資訊"
        push_message(event.source.user_id,tmp)
        #self.go_back(event)
    def on_enter_store_address(self,event):
        print("in address")
        send_address(event.source.user_id,store_id-1)
        tmp="請輸入\"more\"來選擇其他店家資訊"
        push_message(event.source.user_id,tmp)

    def on_enter_test(self,event):
        self.go_back(event)
        None
    def on_enter_menu(self, event):
        print("in menu")
        global store_id
        store_id=0
        tmp="請輸入\"region\"來選擇地區\n輸入\"name\"直接搜尋店家名稱\n輸入\"random\"進入隨機店家模式\n輸入\"fsm\"取得fsm圖\n可於任何階段輸入\"go_back\"來返回此處"
        push_message(event.source.user_id,tmp)
    def on_enter_region(self, event):
        text="請輸入地區(目前僅支援台北、桃園、新竹、台中、台南、高雄)"
        push_message(event.source.user_id,text)
        print("in region")
    def on_enter_taipei(self, event):
        print("in taipei")
    def on_enter_taichung(self, event):
        print("in taichung")
        tmp="請輸入清單中的數字來選擇清單中的店家"
        push_message(event.source.user_id,tmp)
        taichung_list(event.source.user_id)
    def on_enter_taipei(self, event):
        print("in taipei")
        tmp="請輸入清單中的數字來選擇清單中的店家"
        push_message(event.source.user_id,tmp)
        taipei_list(event.source.user_id)
    def on_enter_kaoshung(self, event):
        print("in kaoshung1111")
        tmp="請輸入清單中的數字來選擇清單中的店家"
        push_message(event.source.user_id,tmp)
        kaoshung_list(event.source.user_id)
    def on_enter_tainan(self, event):
        tmp="請輸入清單中的數字來選擇清單中的店家"
        push_message(event.source.user_id,tmp)
        print("in tainan")
        tainan_list(event.source.user_id)
    def on_enter_shinchu(self, event):
        print("in shinchu")
        tmp="請輸入清單中的數字來選擇清單中的店家"
        push_message(event.source.user_id,tmp)
        shinchu_list(event.source.user_id)
    def on_enter_taoyuan(self, event):
        print("in taoyuan")
        tmp="請輸入清單中的數字來選擇清單中的店家"
        push_message(event.source.user_id,tmp)
        taoyuan_list(event.source.user_id)
