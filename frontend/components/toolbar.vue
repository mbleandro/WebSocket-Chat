<template>
  <v-toolbar color="pink" dark fixed >
    <v-toolbar-title>MEU CHAT</v-toolbar-title>
    <v-btn text dark ripple @click="chat_grupo" class="ma-0 ml-5">Grupo</v-btn>
    <v-btn text dark ripple v-if="user && user_type == 'CLIENTE'" @click="chat_atendimento" class="ma-0 ml-5">Atendente</v-btn>
    <v-btn text dark ripple v-if="user && user_type == 'ATENDENTE'" @click="chat_atendimento" class="ma-0 ml-5">Cliente</v-btn>
    <v-spacer />
    <v-btn text dark ripple v-if="!user" class="ma-0 ml-5" @click="open_login_dialog($event)">Login</v-btn>
    <v-btn text dark ripple v-if="user" class="ma-0 ml-5" @click="logout($event)">Logout</v-btn>
    <v-btn text dark ripple v-if="user && user_type == 'CLIENTE'" @click="antender" class="ma-0 ml-5">Acessar como atendente</v-btn>
    <v-btn text dark ripple v-if="user && user_type == 'ATENDENTE'" @click="ser_atendido" class="ma-0 ml-5">Ser atendido</v-btn>
    <login-dialog ref="login_dialog" />
  </v-toolbar>
</template>

<script>
import loginDialog from '~/components/login-dialog.vue'
import Snacks from '~/helpers/Snacks.js'
import api from '~api'

export default {
  components: {
    loginDialog
  },
  props: ['state'],
  computed: {
    user_type () {
      return this.$store.state.chat.user_type
    },
    user () {
      return this.$store.state.chat.user
    }
  },
  methods: {
    antender (evt) {
      api.change_user_mode('ATENDENTE').then((result) => {
        if (result.error) {
          Snacks.show(this.$store, {text: result.error})
        } else {
          this.$store.commit('chat/SET_USER_ATENDENTE')
          this.$store.commit('chat/SET_CHAT_GRUPO')
        }
      })
    },
    ser_atendido (evt) {
      api.change_user_mode('CLIENTE').then((result) => {
        if (result.error) {
          Snacks.show(this.$store, {text: result.error})
        } else {
          this.$store.commit('chat/SET_USER_CLIENTE')
          this.$store.commit('chat/SET_CHAT_GRUPO')
        }
      })
    },
    chat_grupo (evt) {
      this.$store.commit('chat/SET_CHAT_GRUPO')
    },
    chat_atendimento (evt) {
      this.$store.commit('chat/SET_CHAT_ATENDIMENTO')
    },
    async logout () {
      await api.logout()
      this.$store.commit('chat/setCurrentUser', null)
      this.$store.commit('chat/SET_CHAT_GRUPO')
      Snacks.show(this.$store, {text: 'Até logo!'})
    },
    open_login_dialog (evt) {
      this.$refs.login_dialog.open()
      evt.stopPropagation()
    }
  }
}
</script>
