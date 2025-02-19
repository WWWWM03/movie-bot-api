from enum import Enum
from typing import Dict, Optional

from moviebotapi import Session


class SystemNotifyType(str, Enum):
    Login = "登陆"
    SmartDownload = "智能下载"
    System = "系统消息"
    SystemError = "系统错误"
    Plugin = "插件消息"


class NotifyApi:
    def __init__(self, session: Session):
        self._session: Session = session

    def send_message_by_tmpl_name(self, template_name: str, context: Dict, to_uid: Optional[int] = None):
        self._session.post('notify.send_message_by_tmpl_name', {
            'to_uid': to_uid,
            'template_name': template_name,
            'context': context
        })

    def send_message_by_tmpl(self, title: str, body: str, context: Dict, to_uid: Optional[int] = None):
        self._session.post('notify.send_message_by_tmpl_name', {
            'to_uid': to_uid,
            'title': title,
            'body': body,
            'context': context
        })

    def send_text_message(self, title: str, body: str, to_uid: Optional[int] = None):
        self._session.post('notify.send_text_message', {
            'to_uid': to_uid,
            'title': title,
            'body': body
        })

    def send_system_message(self, to_uid: Optional[int], title: str, message: str,
                            message_type: SystemNotifyType = None):
        if not message_type:
            message_type = SystemNotifyType.Plugin
        self._session.post('notify.send_system_message', {
            'to_uid': to_uid,
            'title': title,
            'message': message,
            'type': message_type.name
        })

    def clear_system_message(self, uid: int):
        self._session.get('notify.clear_system_message', {
            'uid': uid
        })
