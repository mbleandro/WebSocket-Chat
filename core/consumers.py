# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from core.models import Atendimento, AtendimentoMessage, Group, GroupMessage, Message, Usuario

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        message = text_data_json['message']
        user_id = text_data_json['user_id']
        usuario = Usuario.objects.get(id=user_id)

        if message_type == "ATENDIMENTO":
            atendimento_id = text_data_json['id']
            atendimento = Atendimento.objects.get(id=atendimento_id)
            menssagem = AtendimentoMessage.objects.create(
                atendimento=atendimento,
                remetente='ATENDENTE' if usuario.is_atendente else 'CLIENTE',
                message=Message.objects.create(text=message['message'])
            )
        if message_type == "GRUPO":
            grupo = Group.objects.get(id=1)
            menssagem = GroupMessage.objects.create(
               usuario=usuario,
               grupo=grupo,
               message=Message.objects.create(text=message['message']['text'])
            )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': json.dumps(menssagem.to_dict_json())
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))