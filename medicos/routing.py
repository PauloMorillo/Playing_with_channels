from djangochannelsrestframework.consumers import view_as_consumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from webapi import views

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("users/", view_as_consumer(views.UserList.as_view())),
        ])
    ),
 })