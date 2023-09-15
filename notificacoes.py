from winotify import Notification

notificacao = Notification(app_id="codigo python", 
                           title="Notificação python", 
                           msg="acabou a zoeira vai estudar",
                           duration="long",
                           )


notificacao.show()