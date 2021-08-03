from django.contrib import admin

from core.models import ActivityLog, Todo, Atendimento, Group, Usuario, GroupMessage, AtendimentoMessage, Message


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'done')

class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('atendido', 'atendente', 'link', 'ativo')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'time')

class AtendimentoMessageAdmin(admin.ModelAdmin):
    list_display = ('atendimento', 'remetente', 'message')

class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'grupo', 'message')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username','is_atendente', 'disponivel', 'avatar')



admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Atendimento, AtendimentoAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(AtendimentoMessage, AtendimentoMessageAdmin)
admin.site.register(GroupMessage, GroupMessageAdmin)
admin.site.register(Usuario, UsuarioAdmin)
