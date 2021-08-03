from django.db import models
from django.contrib.auth.models import User


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.SET_NULL)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done,
        }


class Usuario(User):
    is_atendente = models.BooleanField()
    disponivel = models.BooleanField()
    avatar = models.URLField(default='https://filestore.community.support.microsoft.com/api/images/6061bd47-2818-4f2b-b04a-5a9ddb6f6467?upload=true')

    def to_dict_json(self):
        return {
            'id': self.id,
            'name': self.get_full_name(),
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'permissions': {
                'ADMIN': self.is_superuser,
                'STAFF': self.is_staff,
            },
            'avatar': self.avatar,
            'disponivel': self.disponivel,
            'is_atendente': self.is_atendente
        }

class Atendimento(models.Model):
    atendido = models.ForeignKey(Usuario, related_name='atendendo', on_delete=models.CASCADE)
    atendente = models.ForeignKey(Usuario, related_name='atendente', on_delete=models.CASCADE)
    link = models.CharField(max_length=254)
    ativo = models.BooleanField(default=True)


class Group(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=254)


class Message(models.Model):
    text = models.TextField()
    time = models.TimeField(auto_now=True)

    def to_dict_json(self):
        return {
            'text': self.text,
            'time': self.time.strftime('%H:%M')
        }


class AtendimentoMessage(models.Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)
    remetente = models.CharField(max_length=20)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def to_dict_json(self):
        m = self.message.to_dict_json()
        m.update({
            'remetente': self.remetente,
        })
        return m


class GroupMessage(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Group, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def to_dict_json(self):
        return {
            'name': self.usuario.username,
            'avatar': self.usuario.avatar,
            'message': self.message.to_dict_json()
        }
