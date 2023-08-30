import requests

telegram_api="https://api.telegram.org/bot"
bot_token="5532149163:AAFhLJVKzejhzckx50QQnq6pvxstGochqQk"
chat_id="@flyitbot"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def telegram_notification(self,text):
        url=f"{telegram_api}{bot_token}/sendMessage?{chat_id}/&parse_mode=Markdown&text={text}"
        response=requests.get(url=url)
        return response.json()
